"""Build a lightweight cross-source dedupe index for a company.

The index lets later collectors, especially YouTube, compare candidates
against already-collected podcast sources without reading every transcript or
essence file. It stores metadata plus essence headings only.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from target_config import load_target, target_vault_root


FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip("\"'")
    return result


def normalize_title(value: str) -> str:
    value = value.lower()
    value = re.sub(r"https?://\S+", " ", value)
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", value)
    stop = {
        "the",
        "and",
        "with",
        "podcast",
        "episode",
        "ep",
        "bonus",
        "interview",
    }
    tokens = [token for token in value.split() if token not in stop]
    return " ".join(tokens)


def date_bucket(value: str) -> str:
    match = re.search(r"\d{4}-\d{2}-\d{2}", value or "")
    return match.group(0) if match else ""


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def md_headings(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return []
    headings: list[str] = []
    for line in text.splitlines():
        if line.startswith("## "):
            headings.append(line[3:].strip())
    return headings


def md_record(path: Path, source_type: str) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    fm = parse_frontmatter(text)
    title = fm.get("title") or fm.get("source_title") or re.sub(r"^\d{4}-\d{2}-\d{2}_", "", path.stem).replace("-", " ")
    date = fm.get("date") or fm.get("source_date") or date_bucket(path.name)
    return {
        "source_type": source_type,
        "title": title,
        "normalized_title": normalize_title(title),
        "date": date_bucket(date),
        "show": fm.get("show") or fm.get("podcast") or "",
        "speaker": fm.get("speaker") or "",
        "duration_min": fm.get("duration") or "",
        "url": fm.get("url") or fm.get("episode_url") or fm.get("source_url") or "",
        "audio_url": fm.get("audio_url") or fm.get("source_audio_url") or "",
        "path": str(path),
        "chars": len(text),
    }


def collect_podcast_records(vault: Path) -> list[dict[str, Any]]:
    root = vault / "podcasts"
    records: list[dict[str, Any]] = []

    for json_path in sorted((root / "metadata").glob("_podcast_episodes*.json")):
        data = read_json(json_path)
        if not isinstance(data, list):
            continue
        for item in data:
            if not isinstance(item, dict):
                continue
            title = str(item.get("title") or "")
            if not title:
                continue
            records.append(
                {
                    "source_type": "podcast_metadata",
                    "title": title,
                    "normalized_title": normalize_title(title),
                    "date": date_bucket(str(item.get("date") or item.get("releaseDate") or "")),
                    "show": item.get("show") or item.get("collectionName") or "",
                    "speaker": "",
                    "duration_min": item.get("duration_min") or "",
                    "url": item.get("episode_url") or item.get("url") or "",
                    "audio_url": item.get("audio_url") or "",
                    "path": str(json_path),
                    "chars": 0,
                }
            )

    for path in sorted((root / "metadata").glob("*.md")):
        if path.name.startswith("_"):
            continue
        records.append(md_record(path, "podcast_metadata_md"))

    transcripts_by_key: dict[tuple[str, str], dict[str, Any]] = {}
    for path in sorted((root / "transcripts").glob("*.md")):
        if path.name.startswith("_"):
            continue
        record = md_record(path, "podcast_transcript")
        transcripts_by_key[(record["normalized_title"], record["date"])] = record
        records.append(record)

    for path in sorted((root / "essence").glob("*.md")):
        if path.name.startswith("_"):
            continue
        record = md_record(path, "podcast_essence")
        record["essence_headings"] = md_headings(path)
        records.append(record)

    return records


def compact_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], dict[str, Any]] = {}
    for record in records:
        key = (record.get("normalized_title") or "", record.get("date") or "")
        if not key[0]:
            continue
        current = grouped.setdefault(
            key,
            {
                "normalized_title": key[0],
                "date": key[1],
                "titles": [],
                "shows": [],
                "speakers": [],
                "duration_min": "",
                "urls": [],
                "audio_urls": [],
                "metadata_paths": [],
                "transcript_paths": [],
                "essence_paths": [],
                "essence_headings": [],
                "max_chars": 0,
            },
        )
        for field, target in [
            ("title", "titles"),
            ("show", "shows"),
            ("speaker", "speakers"),
            ("url", "urls"),
            ("audio_url", "audio_urls"),
        ]:
            value = str(record.get(field) or "").strip()
            if value and value not in current[target]:
                current[target].append(value)
        if record.get("duration_min") and not current["duration_min"]:
            current["duration_min"] = record["duration_min"]
        path = record.get("path")
        if path:
            if record["source_type"].startswith("podcast_metadata"):
                bucket = "metadata_paths"
            elif record["source_type"] == "podcast_transcript":
                bucket = "transcript_paths"
            else:
                bucket = "essence_paths"
            if path not in current[bucket]:
                current[bucket].append(path)
        for heading in record.get("essence_headings") or []:
            if heading not in current["essence_headings"]:
                current["essence_headings"].append(heading)
        current["max_chars"] = max(int(current["max_chars"]), int(record.get("chars") or 0))

    return sorted(grouped.values(), key=lambda r: (r["date"], r["normalized_title"]))


def write_markdown(path: Path, records: list[dict[str, Any]], target_key: str) -> None:
    lines = [
        "---",
        "type: source_dedupe_index",
        f"target: {target_key}",
        f"created_at: {datetime.now(timezone.utc).isoformat()}",
        "---",
        "",
        f"# {target_key} Source Dedupe Index",
        "",
        "This file is a lightweight lookup table for cross-source dedupe. It stores metadata and essence headings only; collectors should not read every transcript or essence file for dedupe.",
        "",
        "| date | title | show | transcript | essence | headings |",
        "|---|---|---|---:|---:|---|",
    ]
    for record in records:
        title = (record.get("titles") or [""])[0].replace("|", "\\|")
        show = (record.get("shows") or [""])[0].replace("|", "\\|")
        headings = "; ".join(record.get("essence_headings") or [])[:220].replace("|", "\\|")
        lines.append(
            f"| {record.get('date','')} | {title} | {show} | {len(record.get('transcript_paths') or [])} | {len(record.get('essence_paths') or [])} | {headings} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="Research key, ticker, or slug")
    parser.add_argument("--source", default="podcasts", choices=["podcasts"], help="Source family to index")
    args = parser.parse_args()

    target = load_target(args.target)
    vault = target_vault_root(target)
    records = compact_records(collect_podcast_records(vault))

    out_json = vault / args.source / "metadata" / "_source_dedupe_index.json"
    out_md = vault / args.source / "metadata" / "_source_dedupe_index.md"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "target": target.get("research_key") or args.target,
        "slug": target.get("slug"),
        "source": args.source,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "record_count": len(records),
        "records": records,
    }
    out_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(out_md, records, str(target.get("research_key") or args.target))
    print(json.dumps({"json": str(out_json), "markdown": str(out_md), "record_count": len(records)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
