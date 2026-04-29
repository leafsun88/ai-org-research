#!/usr/bin/env python3
"""
Retry MIDJOURNEY podcast transcription failures with standardized local audio.

This helper is intentionally MIDJOURNEY-scoped. It reads the existing
_podcast_transcription_failures.json, converts cached source audio to a simple
single-channel WAV file, uploads that file to DashScope OSS, then submits the
oss:// URL through the REST API. The REST path is required because DashScope's
Python SDK does not support oss:// temporary URLs for recorded-file ASR.
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import requests

WORKSPACE = Path(__file__).resolve().parents[2]
DISCOVERY_DIR = WORKSPACE / "scripts" / "discovery"
sys.path.insert(0, str(DISCOVERY_DIR))

import fetch_podcast_transcript as base  # noqa: E402

TICKER = "MIDJOURNEY"
TRANSCRIPT_DIR = WORKSPACE / "scripts" / TICKER / "sources" / "podcasts_transcripts"
CACHE_DIR = TRANSCRIPT_DIR / "_audio_cache"
STANDARD_AUDIO_DIR = TRANSCRIPT_DIR / "_standard_audio"
STATUS_PATH = TRANSCRIPT_DIR / "_podcast_transcription_status.json"
FAILURES_PATH = TRANSCRIPT_DIR / "_podcast_transcription_failures.json"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def real_transcription_failures(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        item
        for item in items
        if item.get("status") not in ("success", "existing_success")
        and item.get("stage") == "dashscope_transcription"
        and item.get("error") != "max_episodes_limit_30"
    ]


def find_cached_audio(item: dict[str, Any]) -> Path | None:
    date = (item.get("date") or "")[:10]
    title = item.get("title") or ""
    stem = base.safe_title(title)
    if not date or not stem:
        return None
    matches = sorted(CACHE_DIR.glob(f"{date}_{stem}.*"))
    return matches[0] if matches else None


def convert_to_standard_wav(source: Path, item: dict[str, Any]) -> Path:
    STANDARD_AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    date = (item.get("date") or "")[:10]
    title = item.get("title") or source.stem
    output = STANDARD_AUDIO_DIR / f"{date}_{base.safe_title(title)}.wav"
    if output.exists() and output.stat().st_size > 0:
        return output

    cmd = [
        "afconvert",
        "-f",
        "WAVE",
        "-d",
        "LEI16@16000",
        "-c",
        "1",
        str(source),
        str(output),
    ]
    subprocess.run(cmd, check=True)
    if not output.exists() or output.stat().st_size == 0:
        raise RuntimeError(f"standard audio was not created: {output}")
    return output


def submit_rest_transcription(file_url: str, language: str = "auto") -> dict[str, Any]:
    api_key = os.environ.get("DASHSCOPE_API_KEY")
    if not api_key:
        raise RuntimeError("DASHSCOPE_API_KEY is not set")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "X-DashScope-Async": "enable",
        "X-DashScope-OssResourceResolve": "enable",
    }
    payload: dict[str, Any] = {
        "model": "paraformer-v2",
        "input": {"file_urls": [file_url]},
    }
    if language != "auto":
        payload["parameters"] = {"language_hints": language.split(",")}

    response = requests.post(
        "https://dashscope.aliyuncs.com/api/v1/services/audio/asr/transcription",
        headers=headers,
        data=json.dumps(payload),
        timeout=30,
    )
    if response.status_code != 200:
        return {"success": False, "error": f"REST submit failed: {response.text[:500]}"}

    task_id = response.json().get("output", {}).get("task_id")
    if not task_id:
        return {"success": False, "error": "REST submit returned no task_id"}

    max_poll_seconds = int(os.environ.get("PODCAST_MAX_POLL_SECONDS", "900"))
    started = time.time()
    result: dict[str, Any] | None = None
    while time.time() - started < max_poll_seconds:
        poll = requests.post(
            f"https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}",
            headers=headers,
            timeout=30,
        )
        if poll.status_code != 200:
            return {"success": False, "error": f"REST fetch failed: {poll.text[:500]}"}
        result = poll.json().get("output", {})
        task_status = result.get("task_status")
        if task_status in ("SUCCEEDED", "FAILED"):
            break
        time.sleep(5)

    if result is None:
        return {"success": False, "error": "REST polling returned no result"}
    if result.get("task_status") not in ("SUCCEEDED", "FAILED"):
        return {"success": False, "error": f"REST polling timeout after {max_poll_seconds}s"}

    subtasks = result.get("results") or []
    if not subtasks:
        return {"success": False, "error": f"No REST results returned ({result.get('task_status')})"}
    subtask = subtasks[0]
    if subtask.get("subtask_status") != "SUCCEEDED":
        code = subtask.get("code", "unknown")
        message = subtask.get("message", "")
        return {"success": False, "error": f"REST subtask failed: {code} {message}".strip()}

    transcription_url = subtask.get("transcription_url")
    if not transcription_url:
        return {"success": False, "error": "REST result returned no transcription_url"}

    transcript_response = requests.get(transcription_url, timeout=30)
    transcript_response.raise_for_status()
    transcript_data = transcript_response.json()
    transcripts = transcript_data.get("transcripts") or []
    text = "\n".join(part.get("text", "") for part in transcripts).strip()
    if not text:
        return {"success": False, "error": "REST transcript was empty", "task_id": task_id}

    return {
        "success": True,
        "text": text,
        "chars": len(text),
        "task_id": task_id,
        "dashscope_file_url": subtask.get("file_url", file_url),
    }


def write_transcript(item: dict[str, Any], standard_audio: Path, result: dict[str, Any]) -> Path:
    title = item.get("title", "")
    date = (item.get("date") or "")[:10]
    podcast_name = item.get("podcast", "")
    source_audio_url = item.get("source_audio_url") or item.get("audio_url", "")
    filename = f"{date}_{base.safe_title(title)}.md"
    path = TRANSCRIPT_DIR / filename
    md = f"""---
ticker: {TICKER}
type: podcast_transcript
title: {json.dumps(title, ensure_ascii=False)}
podcast: {json.dumps(podcast_name, ensure_ascii=False)}
date: {date}
audio_url: {json.dumps(result.get("dashscope_file_url", ""), ensure_ascii=False)}
source_audio_url: {json.dumps(source_audio_url, ensure_ascii=False)}
local_audio_path: {json.dumps(str(standard_audio), ensure_ascii=False)}
{base.target_frontmatter(TICKER)}source: podcast_audio
language: auto
chars: {result["chars"]}
credibility: S2-S3
evidence: E2
transcription_engine: dashscope_paraformer_v2_rest_standard_audio
---

# {title}

**Podcast**: {podcast_name}
**Date**: {date}

---

## Transcript

{result["text"]}
"""
    path.write_text(md, encoding="utf-8")
    if path.stat().st_size == 0 or "## Transcript" not in path.read_text(encoding="utf-8", errors="ignore"):
        raise RuntimeError(f"transcript validation failed: {path}")
    return path


def rewrite_status(status_doc: dict[str, Any]) -> list[dict[str, Any]]:
    statuses = status_doc.get("statuses", [])
    failures = [
        item
        for item in statuses
        if item.get("status") not in ("success", "existing_success")
    ]
    status_doc["generated_at"] = datetime.now().isoformat(timespec="seconds")
    status_doc["success_records"] = len(statuses) - len(failures)
    status_doc["failure_records"] = len(failures)
    dump_json(STATUS_PATH, status_doc)
    dump_json(FAILURES_PATH, failures)
    return failures


def main() -> int:
    if not STATUS_PATH.exists() or not FAILURES_PATH.exists():
        print("Missing transcription status/failure files. Run the main script first.")
        return 1

    status_doc = load_json(STATUS_PATH)
    statuses = status_doc.get("statuses", [])
    by_identity = {
        ((item.get("date") or "")[:10], base.normalize_identity_text(item.get("title", ""))): item
        for item in statuses
    }
    failures = real_transcription_failures(load_json(FAILURES_PATH))
    print(f"Retrying {len(failures)} real failures with standardized audio...")

    ok_count = 0
    fail_count = 0
    for index, item in enumerate(failures, 1):
        title = item.get("title", "")
        identity = ((item.get("date") or "")[:10], base.normalize_identity_text(title))
        status_item = by_identity.get(identity, item)
        print(f"[{index}/{len(failures)}] {title[:80]}")

        cached_audio = find_cached_audio(item)
        if not cached_audio:
            fail_count += 1
            status_item.update({
                "status": "failed",
                "error": "standard_audio_retry_missing_cached_audio",
                "stage": "standard_audio_retry",
            })
            rewrite_status(status_doc)
            print("  missing cached audio")
            continue

        try:
            standard_audio = convert_to_standard_wav(cached_audio, item)
            oss_url = base.upload_local_audio_to_oss(standard_audio)
            result = submit_rest_transcription(oss_url)
            if not result.get("success"):
                raise RuntimeError(result.get("error", "unknown standard-audio retry failure"))

            transcript_path = write_transcript(item, standard_audio, result)
            status_item.update({
                "status": "success",
                "title": title,
                "date": item.get("date", ""),
                "podcast": item.get("podcast", ""),
                "audio_url": result.get("dashscope_file_url", oss_url),
                "source_audio_url": item.get("source_audio_url") or item.get("audio_url", ""),
                "local_audio_path": str(standard_audio),
                "source_local_audio_path": str(cached_audio),
                "transcript_path": str(transcript_path),
                "chars": result["chars"],
                "task_id": result.get("task_id", ""),
                "attempt_round": "standard_audio_rest",
                "stage": "standard_audio_retry",
            })
            rewrite_status(status_doc)
            cached_audio.unlink(missing_ok=True)
            ok_count += 1
            print(f"  success: {result['chars']:,} chars -> {transcript_path.name}")
        except Exception as exc:
            fail_count += 1
            status_item.update({
                "status": "failed",
                "title": title,
                "date": item.get("date", ""),
                "podcast": item.get("podcast", ""),
                "audio_url": item.get("audio_url", ""),
                "error": f"standard_audio_retry_failed: {exc}",
                "stage": "standard_audio_retry",
            })
            rewrite_status(status_doc)
            print(f"  failed: {str(exc)[:200]}")

    print(f"Done. standard audio retry successes={ok_count}, failures={fail_count}")
    return 0 if fail_count == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
