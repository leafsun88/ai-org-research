#!/usr/bin/env python3
"""
Transcribe remaining MIDJOURNEY podcast episodes with controlled concurrency.

This script is MIDJOURNEY-scoped and avoids the shared discovery script's SDK
oss:// limitation by using standardized WAV audio plus DashScope REST calls.
It keeps concurrency low by default because the bottleneck is usually the
DashScope account-side ASR queue, not local upload speed.
"""

from __future__ import annotations

import concurrent.futures
import json
import os
import subprocess
import sys
import threading
import time
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

import requests

WORKSPACE = Path(__file__).resolve().parents[2]
DISCOVERY_DIR = WORKSPACE / "scripts" / "discovery"
sys.path.insert(0, str(DISCOVERY_DIR))

import fetch_podcast_transcript as base  # noqa: E402

TICKER = "MIDJOURNEY"
EPISODES_PATH = WORKSPACE / "scripts" / TICKER / "_podcast_episodes_org_curated.json"
TRANSCRIPT_DIR = WORKSPACE / "scripts" / TICKER / "sources" / "podcasts_transcripts"
WORK_DIR = TRANSCRIPT_DIR / "_controlled_concurrency_audio"
DOWNLOAD_DIR = WORK_DIR / "downloads"
STANDARD_AUDIO_DIR = WORK_DIR / "standard_wav"
STATUS_PATH = TRANSCRIPT_DIR / "_podcast_transcription_status.json"
FAILURES_PATH = TRANSCRIPT_DIR / "_podcast_transcription_failures.json"
PROGRESS_PATH = TRANSCRIPT_DIR / "_controlled_concurrency_progress.json"

STATUS_LOCK = threading.Lock()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def episode_identity(ep: dict[str, Any]) -> tuple[str, str]:
    return (
        (ep.get("date") or ep.get("releaseDate") or "")[:10],
        base.normalize_identity_text(ep.get("title") or ep.get("trackName") or ""),
    )


def existing_transcript(ep: dict[str, Any]) -> str:
    return base.existing_transcript_path(TRANSCRIPT_DIR, ep)


def select_missing_episodes(episodes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [ep for ep in episodes if not existing_transcript(ep)]


def candidate_audio_urls(ep: dict[str, Any]) -> list[str]:
    original = ep.get("audio_url") or ep.get("url") or ""
    candidates: list[str] = []
    for url in [original, base.resolve_audio_url(original), base.refresh_audio_url(ep)]:
        if url and url.startswith("http") and url not in candidates:
            candidates.append(url)
    return candidates


def download_source_audio(ep: dict[str, Any]) -> Path:
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    title = ep.get("title") or ep.get("trackName") or ""
    date = (ep.get("date") or ep.get("releaseDate") or "")[:10]
    last_error = "no candidate URLs"
    for url in candidate_audio_urls(ep):
        path = base.download_audio_to_cache(url, DOWNLOAD_DIR, title, date)
        if path and path.exists() and path.stat().st_size > 0:
            return path
        last_error = f"download failed for {url[:120]}"
    raise RuntimeError(last_error)


def convert_to_standard_wav(source: Path, ep: dict[str, Any]) -> Path:
    STANDARD_AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    date = (ep.get("date") or ep.get("releaseDate") or "")[:10]
    title = ep.get("title") or ep.get("trackName") or source.stem
    output = STANDARD_AUDIO_DIR / f"{date}_{base.safe_title(title)}.wav"
    if output.exists() and output.stat().st_size > 0:
        return output
    subprocess.run(
        [
            "afconvert",
            "-f",
            "WAVE",
            "-d",
            "LEI16@16000",
            "-c",
            "1",
            str(source),
            str(output),
        ],
        check=True,
    )
    if not output.exists() or output.stat().st_size == 0:
        raise RuntimeError(f"standard WAV was not created: {output}")
    return output


def rest_transcribe(file_url: str) -> dict[str, Any]:
    api_key = os.environ.get("DASHSCOPE_API_KEY")
    if not api_key:
        raise RuntimeError("DASHSCOPE_API_KEY is not set")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "X-DashScope-Async": "enable",
        "X-DashScope-OssResourceResolve": "enable",
    }
    response = requests.post(
        "https://dashscope.aliyuncs.com/api/v1/services/audio/asr/transcription",
        headers=headers,
        data=json.dumps({"model": "paraformer-v2", "input": {"file_urls": [file_url]}}),
        timeout=30,
    )
    if response.status_code != 200:
        raise RuntimeError(f"REST submit failed: {response.text[:500]}")
    task_id = response.json().get("output", {}).get("task_id")
    if not task_id:
        raise RuntimeError("REST submit returned no task_id")

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
            raise RuntimeError(f"REST poll failed: {poll.text[:500]}")
        result = poll.json().get("output", {})
        task_status = result.get("task_status")
        if task_status in ("SUCCEEDED", "FAILED"):
            break
        time.sleep(5)

    if result is None:
        raise RuntimeError("REST polling returned no result")
    if result.get("task_status") not in ("SUCCEEDED", "FAILED"):
        raise RuntimeError(f"REST polling timeout after {max_poll_seconds}s")

    subtasks = result.get("results") or []
    if not subtasks:
        raise RuntimeError(f"No REST results returned ({result.get('task_status')})")
    subtask = subtasks[0]
    if subtask.get("subtask_status") != "SUCCEEDED":
        code = subtask.get("code", "unknown")
        message = subtask.get("message", "")
        raise RuntimeError(f"REST subtask failed: {code} {message}".strip())

    transcription_url = subtask.get("transcription_url")
    if not transcription_url:
        raise RuntimeError("REST result returned no transcription_url")
    transcript_response = requests.get(transcription_url, timeout=30)
    transcript_response.raise_for_status()
    transcript_data = transcript_response.json()
    text = "\n".join(part.get("text", "") for part in transcript_data.get("transcripts", [])).strip()
    if not text:
        raise RuntimeError("REST transcript was empty")
    return {
        "task_id": task_id,
        "text": text,
        "chars": len(text),
        "dashscope_file_url": subtask.get("file_url", file_url),
    }


def write_transcript(ep: dict[str, Any], source_audio: Path, standard_audio: Path, result: dict[str, Any]) -> Path:
    title = ep.get("title") or ep.get("trackName") or ""
    podcast_name = ep.get("podcast") or ep.get("show") or ep.get("collectionName") or ""
    date = (ep.get("date") or ep.get("releaseDate") or "")[:10]
    source_audio_url = ep.get("audio_url") or ep.get("url") or ""
    path = TRANSCRIPT_DIR / f"{date}_{base.safe_title(title)}.md"
    md = f"""---
ticker: {TICKER}
type: podcast_transcript
title: {json.dumps(title, ensure_ascii=False)}
podcast: {json.dumps(podcast_name, ensure_ascii=False)}
date: {date}
audio_url: {json.dumps(result.get("dashscope_file_url", ""), ensure_ascii=False)}
source_audio_url: {json.dumps(source_audio_url, ensure_ascii=False)}
local_audio_path: {json.dumps(str(standard_audio), ensure_ascii=False)}
source_local_audio_path: {json.dumps(str(source_audio), ensure_ascii=False)}
{base.target_frontmatter(TICKER)}source: podcast_audio
language: auto
chars: {result["chars"]}
credibility: S2-S3
evidence: E2
transcription_engine: dashscope_paraformer_v2_rest_controlled_concurrency
---

# {title}

**Podcast**: {podcast_name}
**Date**: {date}

---

## Transcript

{result["text"]}
"""
    path.write_text(md, encoding="utf-8")
    saved = path.read_text(encoding="utf-8", errors="ignore")
    if path.stat().st_size == 0 or "## Transcript" not in saved or len(result["text"]) < 20:
        raise RuntimeError(f"transcript validation failed: {path}")
    return path


def process_episode(ep: dict[str, Any]) -> dict[str, Any]:
    title = ep.get("title") or ep.get("trackName") or ""
    date = (ep.get("date") or ep.get("releaseDate") or "")[:10]
    podcast_name = ep.get("podcast") or ep.get("show") or ep.get("collectionName") or ""
    source_audio: Path | None = None
    try:
        if existing_transcript(ep):
            return {
                "status": "existing_success",
                "title": title,
                "date": date,
                "podcast": podcast_name,
                "transcript_path": existing_transcript(ep),
            }
        source_audio = download_source_audio(ep)
        standard_audio = convert_to_standard_wav(source_audio, ep)
        oss_url = base.upload_local_audio_to_oss(standard_audio)
        result = rest_transcribe(oss_url)
        transcript_path = write_transcript(ep, source_audio, standard_audio, result)
        source_audio.unlink(missing_ok=True)
        return {
            "status": "success",
            "title": title,
            "date": date,
            "podcast": podcast_name,
            "audio_url": result.get("dashscope_file_url", oss_url),
            "source_audio_url": ep.get("audio_url") or ep.get("url") or "",
            "local_audio_path": str(standard_audio),
            "transcript_path": str(transcript_path),
            "chars": result["chars"],
            "task_id": result["task_id"],
            "attempt_round": "controlled_concurrency_rest",
            "stage": "controlled_concurrency",
        }
    except Exception as exc:
        return {
            "status": "failed",
            "title": title,
            "date": date,
            "podcast": podcast_name,
            "audio_url": ep.get("audio_url") or ep.get("url") or "",
            "source_local_audio_path": str(source_audio) if source_audio else "",
            "error": f"controlled_concurrency_failed: {exc}",
            "stage": "controlled_concurrency",
        }


def rebuild_status(episodes: list[dict[str, Any]], updates: dict[tuple[str, str], dict[str, Any]]) -> dict[str, Any]:
    statuses: list[dict[str, Any]] = []
    for ep in episodes:
        identity = episode_identity(ep)
        if identity in updates:
            statuses.append(updates[identity])
            continue
        existing = existing_transcript(ep)
        if existing:
            statuses.append({
                "status": "existing_success",
                "title": ep.get("title") or ep.get("trackName") or "",
                "date": (ep.get("date") or ep.get("releaseDate") or "")[:10],
                "podcast": ep.get("podcast") or ep.get("show") or ep.get("collectionName") or "",
                "audio_url": ep.get("audio_url") or ep.get("url") or "",
                "transcript_path": existing,
            })
        else:
            statuses.append({
                "status": "failed",
                "title": ep.get("title") or ep.get("trackName") or "",
                "date": (ep.get("date") or ep.get("releaseDate") or "")[:10],
                "podcast": ep.get("podcast") or ep.get("show") or ep.get("collectionName") or "",
                "audio_url": ep.get("audio_url") or ep.get("url") or "",
                "error": "not_processed_by_controlled_concurrency",
                "stage": "controlled_concurrency",
            })
    failures = [item for item in statuses if item.get("status") not in ("success", "existing_success")]
    return {
        "ticker": TICKER,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "retry_rounds": "controlled_concurrency_rest",
        "min_duration_min": 0,
        "total_records": len(statuses),
        "success_records": len(statuses) - len(failures),
        "failure_records": len(failures),
        "statuses": statuses,
    }


def main() -> int:
    episodes = load_json(EPISODES_PATH, [])
    if not episodes:
        print(f"No episodes found: {EPISODES_PATH}")
        return 1

    workers = int(os.environ.get("PODCAST_CONCURRENT_WORKERS", "2"))
    workers = max(1, min(workers, 2))
    missing = select_missing_episodes(episodes)
    print(f"Existing transcripts: {len(episodes) - len(missing)}")
    print(f"Missing transcripts: {len(missing)}")
    print(f"Controlled workers: {workers}")

    updates: dict[tuple[str, str], dict[str, Any]] = {}
    done = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_ep = {executor.submit(process_episode, ep): ep for ep in missing}
        for future in concurrent.futures.as_completed(future_to_ep):
            ep = future_to_ep[future]
            result = future.result()
            updates[episode_identity(ep)] = result
            done += 1
            status = result.get("status")
            title = result.get("title", "")[:70]
            extra = f" chars={result.get('chars')}" if result.get("chars") else f" error={result.get('error', '')[:120]}"
            print(f"[{done}/{len(missing)}] {status}: {title}{extra}")
            with STATUS_LOCK:
                dump_json(PROGRESS_PATH, {
                    "generated_at": datetime.now().isoformat(timespec="seconds"),
                    "workers": workers,
                    "completed": done,
                    "total_missing_at_start": len(missing),
                    "counts": dict(Counter(item.get("status") for item in updates.values())),
                    "updates": list(updates.values()),
                })

    status_doc = rebuild_status(episodes, updates)
    failures = [item for item in status_doc["statuses"] if item.get("status") not in ("success", "existing_success")]
    dump_json(STATUS_PATH, status_doc)
    dump_json(FAILURES_PATH, failures)
    print(f"Done: {status_doc['success_records']}/{status_doc['total_records']} succeeded")
    if failures:
        print("Failure reasons:")
        for reason, count in Counter(item.get("error", "unknown") for item in failures).most_common():
            print(f"  {count}x {reason[:140]}")
    return 0 if not failures else 2


if __name__ == "__main__":
    raise SystemExit(main())
