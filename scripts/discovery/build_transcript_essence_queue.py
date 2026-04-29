#!/usr/bin/env python3
"""Build a queue for turning existing transcripts into essence files.

The script reads the markdown transcript inventory, derives the canonical
company vault path for each unique transcript, creates the needed essence
directories, and writes a machine-readable queue plus a short status report.
It does not summarize content; relevance and insight extraction are separate
research steps.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any, Optional


PROJECT_ROOT = Path(__file__).resolve().parents[2]
TRANSCRIPT_META_DIR = PROJECT_ROOT / "companies" / "_meta" / "transcripts"
DEFAULT_INVENTORY = TRANSCRIPT_META_DIR / "_transcript_inventory_2026-04-21.md"

SOURCE_OUTPUTS = {
    "podcast": ("podcasts/essence", "podcast_essence"),
    "youtube": ("youtube/essence", "youtube_essence"),
    "web": ("substack/essence", "source_essence"),
    "substack": ("substack/essence", "source_essence"),
}

CANONICAL_COMPANY = {
    "sq": "block",
    "block": "block",
    "perplexity_fallback": "perplexity",
}


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "unknown"


def canonical_company(value: str) -> str:
    key = slugify(value).replace("-", "_")
    return CANONICAL_COMPANY.get(key, slugify(value))


def relocate_transcript_path(path: Path) -> Path:
    """Map pre-refactor vault transcript paths to the current canonical layout."""
    if path.exists():
        return path
    try:
        rel = path.relative_to(PROJECT_ROOT)
    except ValueError:
        return path
    parts = rel.parts
    if len(parts) >= 5 and parts[0] == "companies" and parts[2] == "vault":
        source = parts[3]
        if source in {"podcasts", "youtube", "substack"} and parts[4] not in {
            "metadata",
            "transcripts",
            "essence",
        }:
            candidate = PROJECT_ROOT / Path(*parts[:4]) / "transcripts" / Path(*parts[4:])
            if candidate.exists():
                return candidate
    return path


def parse_inventory(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Inventory not found: {path}")

    lines = path.read_text(encoding="utf-8").splitlines()
    records: list[dict[str, Any]] = []
    current: Optional[dict[str, Any]] = None
    header_re = re.compile(
        r"^\d+\.\s+\[(?P<company>[^\]]+)\]\s+\[(?P<source_type>[^\]]+)\]\s+"
        r"(?P<date>[^—]+?)\s+—\s+(?P<title>.+)$"
    )

    for line in lines:
        match = header_re.match(line)
        if match:
            if current:
                records.append(current)
            current = {
                "company": canonical_company(match.group("company")),
                "inventory_company": match.group("company"),
                "source_type": match.group("source_type").strip().lower(),
                "date": match.group("date").strip(),
                "title": match.group("title").strip(),
            }
            continue

        if not current:
            continue

        stripped = line.strip()
        if stripped.startswith("path: `") and stripped.endswith("`"):
            raw_path = stripped[len("path: `") : -1]
            transcript_path = Path(raw_path)
            if not transcript_path.is_absolute():
                transcript_path = PROJECT_ROOT / transcript_path
            transcript_path = relocate_transcript_path(transcript_path)
            current["source_transcript"] = str(transcript_path)
        elif stripped.startswith("chars: "):
            try:
                current["chars"] = int(stripped.split(":", 1)[1].replace(",", "").strip())
            except ValueError:
                current["chars"] = None

    if current:
        records.append(current)
    return records


def target_output(record: dict[str, Any]) -> tuple[Path, str]:
    source_type = record["source_type"]
    if source_type not in SOURCE_OUTPUTS:
        raise ValueError(f"Unsupported source type: {source_type}")
    subdir, essence_type = SOURCE_OUTPUTS[source_type]
    transcript = Path(record["source_transcript"])
    company = record["company"]
    out_dir = PROJECT_ROOT / "companies" / company / "vault" / subdir
    out_file = out_dir / f"{transcript.stem}_essence.md"
    return out_file, essence_type


def build_queue(records: list[dict[str, Any]], create_dirs: bool) -> list[dict[str, Any]]:
    queue: list[dict[str, Any]] = []
    for index, record in enumerate(records, start=1):
        if record.get("source_type") not in SOURCE_OUTPUTS:
            continue
        if not record.get("source_transcript"):
            continue

        output_path, essence_type = target_output(record)
        if create_dirs:
            output_path.parent.mkdir(parents=True, exist_ok=True)

        item = dict(record)
        item.update(
            {
                "queue_id": f"TEQ-{index:04d}",
                "essence_type": essence_type,
                "essence_path": str(output_path),
                "status": "done" if output_path.exists() else "pending",
            }
        )
        queue.append(item)
    return queue


def write_outputs(queue: list[dict[str, Any]], output_json: Path, output_md: Path) -> None:
    output_json.parent.mkdir(parents=True, exist_ok=True)
    generated_at = datetime.now().isoformat(timespec="seconds")

    payload = {
        "type": "transcript_essence_queue",
        "generated_at": generated_at,
        "count": len(queue),
        "items": queue,
    }
    output_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    by_company = Counter(item["company"] for item in queue)
    by_source = Counter(item["source_type"] for item in queue)
    by_status = Counter(item["status"] for item in queue)

    lines = [
        "---",
        "type: transcript_essence_queue",
        f"date: {generated_at[:10]}",
        "status: current",
        "---",
        "",
        "# Transcript Essence Queue",
        "",
        "## Summary",
        "",
        f"- Queue items: {len(queue)}",
        f"- Pending: {by_status.get('pending', 0)}",
        f"- Done: {by_status.get('done', 0)}",
        "",
        "## By Source Type",
        "",
    ]
    for source_type, count in sorted(by_source.items()):
        lines.append(f"- {source_type}: {count}")
    lines.extend(["", "## By Company", ""])
    for company, count in sorted(by_company.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- {company}: {count}")
    lines.extend(["", "## Items", ""])
    for item in queue:
        rel_source = Path(item["source_transcript"]).relative_to(PROJECT_ROOT)
        rel_out = Path(item["essence_path"]).relative_to(PROJECT_ROOT)
        lines.append(
            f"- {item['queue_id']} [{item['company']}] [{item['source_type']}] "
            f"{item['date']} — {item['title']}"
        )
        lines.append(f"  source: `{rel_source}`")
        lines.append(f"  essence: `{rel_out}`")
        lines.append(f"  status: `{item['status']}`")
    output_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument(
        "--output-json",
        type=Path,
        default=TRANSCRIPT_META_DIR / "_transcript_essence_queue_2026-04-21.json",
    )
    parser.add_argument(
        "--output-md",
        type=Path,
        default=TRANSCRIPT_META_DIR / "_transcript_essence_queue_2026-04-21.md",
    )
    parser.add_argument("--no-create-dirs", action="store_true")
    args = parser.parse_args()

    records = parse_inventory(args.inventory)
    queue = build_queue(records, create_dirs=not args.no_create_dirs)
    write_outputs(queue, args.output_json, args.output_md)
    print(f"Wrote {len(queue)} queue items")
    print(args.output_json)
    print(args.output_md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
