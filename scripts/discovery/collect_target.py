"""Target-driven discovery orchestrator.

Runs configured channels for a target manifest entry, keeps scripts/ as staging,
syncs collected artifacts into companies/{slug}/vault, and writes lightweight
analysis inventories. By default, --channels all only runs the four core,
low-entropy sources: podcasts, financials, substack, and youtube. Use
--channels all_sources for the older maximum-surface collection mode.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from target_config import (
    PROJECT_ROOT,
    build_alias_query_terms,
    ensure_target_dirs,
    get_channel,
    get_channel_queries,
    get_channel_seed_urls,
    load_target,
    resolve_target_path,
    target_analysis_root,
    target_key,
    target_script_root,
    target_vault_root,
    vault_channel_path,
)


WEB_CHANNELS = {
    "substack",
    "official",
    "founder_voice",
    "web_longform",
    "enterprise_partnerships",
    "jobs_org",
    "social_community",
    "funding_compute",
}
CORE_CHANNELS = [
    "podcasts",
    "financials",
    "substack",
    "youtube",
]

OPTIONAL_CHANNELS = [
    "official",
    "founder_voice",
    "web_longform",
    "enterprise_partnerships",
    "jobs_org",
    "social_community",
    "funding_compute",
]

ALL_CHANNELS = CORE_CHANNELS


def parse_channels(value: str) -> list[str]:
    if value == "all":
        return ALL_CHANNELS
    if value in {"all_sources", "all-sources", "max", "maximum"}:
        return CORE_CHANNELS + OPTIONAL_CHANNELS
    channels = [chunk.strip() for chunk in value.split(",") if chunk.strip()]
    aliases = {
        "web": "web_longform",
        "social": "social_community",
        "jobs": "jobs_org",
        "partnerships": "enterprise_partnerships",
        "funding": "funding_compute",
        "finance": "financials",
        "financial": "financials",
    }
    return [aliases.get(channel, channel) for channel in channels]


def child_env() -> dict[str, str]:
    env = os.environ.copy()
    return env


def run_command(args: list[str], env_extra: dict[str, str] | None = None) -> dict[str, Any]:
    started = datetime.now()
    print(f"  $ {' '.join(args)}")
    env = child_env()
    if env_extra:
        env.update(env_extra)
    proc = subprocess.run(
        args,
        cwd=str(PROJECT_ROOT),
        env=env,
        text=True,
        capture_output=True,
    )
    if proc.stdout:
        print(proc.stdout)
    if proc.stderr:
        print(proc.stderr, file=sys.stderr)
    return {
        "command": args,
        "returncode": proc.returncode,
        "started_at": started.isoformat(timespec="seconds"),
        "finished_at": datetime.now().isoformat(timespec="seconds"),
        "stdout_tail": proc.stdout[-4000:] if proc.stdout else "",
        "stderr_tail": proc.stderr[-4000:] if proc.stderr else "",
    }


def sync_tree(src: Path, dst: Path, skip_dirs: set[str] | None = None) -> list[str]:
    copied: list[str] = []
    skip_dirs = skip_dirs or set()
    if not src.exists():
        return copied
    dst.mkdir(parents=True, exist_ok=True)
    for path in src.rglob("*"):
        if path.is_dir():
            continue
        if any(part in skip_dirs for part in path.parts):
            continue
        rel = path.relative_to(src)
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        copied.append(str(target))
    return copied


def copy_file(src: Path, dst: Path) -> str:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return str(dst)


def sync_flat_source_files(src: Path, dst_by_kind: dict[str, Path], default_kind: str = "metadata") -> list[str]:
    """Sync direct files from an old flat source dir into metadata/transcripts buckets."""
    copied: list[str] = []
    if not src.exists():
        return copied
    for path in src.iterdir():
        if not path.is_file() or path.name == ".DS_Store":
            continue
        name = path.name
        suffix = path.suffix.lower()
        if suffix == ".md" and not name.startswith("_"):
            kind = "transcripts"
        elif suffix in {".md", ".json", ".csv"} or name.startswith("_"):
            kind = "metadata"
        else:
            kind = default_kind
        copied.append(copy_file(path, dst_by_kind[kind] / name))
    return copied


def sync_outputs(target: dict[str, Any], channels: list[str]) -> dict[str, Any]:
    key = target_key(target)
    script_root = target_script_root(target)
    vault_root = target_vault_root(target)
    sync_status: dict[str, Any] = {}

    for channel in channels:
        copied: list[str] = []
        if channel == "podcasts":
            podcast_meta_new = script_root / "sources" / "podcasts" / "metadata"
            podcast_meta_old = script_root / "sources" / "podcasts"
            copied.extend(sync_tree(podcast_meta_new, vault_root / "podcasts" / "metadata"))
            if not podcast_meta_new.exists():
                copied.extend(sync_tree(podcast_meta_old, vault_root / "podcasts" / "metadata"))
            copied.extend(sync_tree(
                script_root / "sources" / "podcasts" / "transcripts",
                vault_root / "podcasts" / "transcripts",
                skip_dirs={"_audio_cache", "_standard_audio"},
            ))
            for filename in ["_podcast_query_map.md", "_podcast_episodes.json", "_podcast_episodes_org_curated.json"]:
                for src in [
                    script_root / filename,
                    script_root / "sources" / "podcasts" / "metadata" / filename,
                    script_root / "sources" / "podcasts" / filename,
                ]:
                    if src.exists():
                        copied.append(copy_file(src, vault_root / "podcasts" / "metadata" / filename))
                        break
        elif channel == "youtube":
            youtube_root = script_root / "sources" / "youtube"
            copied.extend(sync_tree(youtube_root / "metadata", vault_root / "youtube" / "metadata"))
            copied.extend(sync_tree(youtube_root / "transcripts", vault_root / "youtube" / "transcripts"))
            copied.extend(sync_tree(youtube_root / "essence", vault_root / "youtube" / "essence"))
            copied.extend(sync_flat_source_files(
                youtube_root,
                {
                    "metadata": vault_root / "youtube" / "metadata",
                    "transcripts": vault_root / "youtube" / "transcripts",
                },
            ))
        elif channel == "substack":
            substack_root = script_root / "sources" / "substack"
            copied.extend(sync_tree(substack_root / "metadata", vault_root / "substack" / "metadata"))
            copied.extend(sync_tree(substack_root / "transcripts", vault_root / "substack" / "transcripts"))
            copied.extend(sync_tree(substack_root / "essence", vault_root / "substack" / "essence"))
            copied.extend(sync_flat_source_files(
                substack_root,
                {
                    "metadata": vault_root / "substack" / "metadata",
                    "transcripts": vault_root / "substack" / "transcripts",
                },
            ))
        elif channel == "financials":
            financial_root = script_root / "sources" / "financials"
            financial_dst = vault_root / "financials"
            copied.extend(sync_tree(financial_root / "metadata", financial_dst / "metadata"))
            copied.extend(sync_tree(financial_root / "reports", financial_dst / "reports"))
            copied.extend(sync_tree(financial_root / "sec_filings", financial_dst / "reports" / "sec_filings"))
            for path in (financial_root.iterdir() if financial_root.exists() else []):
                if not path.is_file() or path.name == ".DS_Store":
                    continue
                if path.suffix.lower() == ".md":
                    copied.append(copy_file(path, financial_dst / "reports" / path.name))
                elif path.suffix.lower() in {".json", ".csv"} or path.name.startswith("_"):
                    copied.append(copy_file(path, financial_dst / "metadata" / path.name))
        else:
            copied.extend(sync_tree(script_root / "sources" / channel, vault_root / "_optional" / vault_channel_path(channel)))
        sync_status[channel] = {"copied": len(copied), "files": copied[:50]}

    status_path = script_root / "_sync_status.json"
    status_path.parent.mkdir(parents=True, exist_ok=True)
    status_path.write_text(json.dumps({"research_key": key, "channels": sync_status}, ensure_ascii=False, indent=2), encoding="utf-8")
    return sync_status


def channel_plan_summary(target: dict[str, Any], channels: list[str]) -> dict[str, Any]:
    summary = {}
    for channel in channels:
        cfg = get_channel(target, channel)
        if channel == "financials":
            ticker = str(target.get("ticker") or target_key(target))
            summary[channel] = {
                "enabled": bool(target.get("is_public", True)),
                "queries": [],
                "seed_urls": [],
                "output_script": str(target_script_root(target) / "sources" / "financials"),
                "output_vault": str(target_vault_root(target) / "financials"),
            }
            continue
        summary[channel] = {
            "enabled": cfg.get("enabled", True),
            "queries": get_channel_queries(target, channel),
            "seed_urls": get_channel_seed_urls(target, channel),
            "output_script": str(resolve_target_path(target, "script_channel", "podcasts" if channel == "podcasts" else channel)),
            "output_vault": str(resolve_target_path(target, "vault_channel", "podcasts" if channel == "podcasts" else channel)),
        }
    return summary


def run_channel(target: dict[str, Any], channel: str, skip_transcript: bool, web_max_queries: int = 0) -> dict[str, Any]:
    if channel in WEB_CHANNELS:
        return run_command([
            sys.executable,
            "scripts/discovery/fetch_web_sources.py",
            "--target",
            target_key(target),
            "--channels",
            channel,
            "--max-queries",
            str(web_max_queries),
        ])
    if channel == "youtube":
        return run_command([
            sys.executable,
            "scripts/discovery/fetch_youtube.py",
            "--target",
            target_key(target),
        ])
    if channel == "podcasts":
        result = run_command([
            sys.executable,
            "scripts/discovery/fetch_podcasts.py",
            "--target",
            target_key(target),
        ])
        if skip_transcript:
            result["transcript_skipped"] = True
            return result
        cfg = get_channel(target, "podcasts")
        max_episodes = int(cfg.get("max_episodes", 50))
        curated_path = target_script_root(target) / "sources" / "podcasts" / "metadata" / "_podcast_episodes_org_curated.json"
        transcript = run_command([
            sys.executable,
            "scripts/discovery/fetch_podcast_transcript.py",
            target_key(target),
            str(max_episodes),
            "auto",
            str(curated_path),
        ])
        result["transcript"] = transcript
        return result
    if channel == "financials":
        if not target.get("is_public", True):
            return {
                "returncode": 0,
                "skipped": True,
                "reason": "private_target_skip_public_financial_scripts",
            }
        ticker = str(target.get("ticker") or target_key(target))
        commands = [
            [sys.executable, "scripts/discovery/fetch_financials.py", ticker],
            [sys.executable, "scripts/discovery/fetch_sec_edgar.py", ticker, "10-K", "3"],
            [sys.executable, "scripts/discovery/fetch_sec_edgar.py", ticker, "10-Q", "4"],
            [sys.executable, "scripts/discovery/fetch_xbrl.py", ticker],
        ]
        financial_output = target_script_root(target) / "sources" / "financials"
        results = [run_command(command, env_extra={"ALIKE_OUTPUT_DIR": str(financial_output)}) for command in commands]
        return {
            "returncode": 0 if all(item["returncode"] == 0 for item in results) else 1,
            "commands": results,
        }
    return {"returncode": 2, "error": f"Unknown channel: {channel}"}


def source_inventory(target: dict[str, Any]) -> Path:
    vault = target_vault_root(target)
    analysis = target_analysis_root(target)
    analysis.mkdir(parents=True, exist_ok=True)
    date = datetime.now().strftime("%Y-%m-%d")
    path = analysis / f"{target.get('company_name', target_key(target))}_source_inventory_{date}.md"

    lines = [
        "---",
        f"company: {target.get('company_name', '')}",
        f"research_key: {target_key(target)}",
        "type: source_inventory",
        f"date: {date}",
        "---",
        "",
        f"# {target.get('company_name', target_key(target))} Source Inventory",
        "",
    ]
    if not vault.exists():
        lines.append("Vault not found.")
    else:
        grouped: dict[str, list[Path]] = {}
        for file in sorted(vault.rglob("*")):
            if file.is_file() and file.name != ".DS_Store":
                top = file.relative_to(vault).parts[0]
                grouped.setdefault(top, []).append(file)
        for top, files in grouped.items():
            lines.append(f"## {top} ({len(files)} files)")
            for file in files[:80]:
                rel = file.relative_to(vault)
                size = file.stat().st_size
                lines.append(f"- `{rel}` ({size // 1024} KB)")
            if len(files) > 80:
                lines.append(f"- ... {len(files) - 80} more")
            lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def evidence_map(target: dict[str, Any]) -> Path:
    analysis = target_analysis_root(target)
    analysis.mkdir(parents=True, exist_ok=True)
    date = datetime.now().strftime("%Y-%m-%d")
    path = analysis / f"{target.get('company_name', target_key(target))}_evidence_map_{date}.md"
    if path.exists():
        return path
    company = target.get("company_name", target_key(target))
    lines = [
        "---",
        f"company: {company}",
        f"research_key: {target_key(target)}",
        "type: evidence_map",
        f"date: {date}",
        "status: source_collection_first_pass",
        "---",
        "",
        f"# {company} Evidence Map",
        "",
        "## Founder 认知",
        "- 优先从 podcasts / YouTube / Substack essence 中抽取：Founder world model、AI 能力边界、组织设计、商业化取舍。",
        "",
        "## 组织动作",
        "- 优先从 podcast / YouTube / Substack essence 中抽取：招聘、角色设计、节奏、反馈链、AI workflow、管理工具变化。",
        "",
        "## 业务影响",
        "- 优先从 financials / Substack / customer cases / transcript essence 中抽取：收入、利润、产品速度、客户采用、GTM、单位经济。",
        "",
        "## 竞争与风险",
        "- 优先从 Substack / YouTube / podcast 反方观点和财务材料中抽取：竞争压力、商业化不确定性、组织转型副作用。",
        "",
        "## 下一步",
        "- 先补齐高相关 source 的 essence，再写 fact pack / complex report；付费墙只作为 URL 线索，不直接当事实。",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    parser.add_argument("--channels", default="all")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-transcript", action="store_true")
    parser.add_argument("--web-max-queries", type=int, default=0)
    args = parser.parse_args()

    target = load_target(args.target)
    channels = parse_channels(args.channels)
    ensure_target_dirs(target)
    plan = {
        "research_key": target_key(target),
        "company": target.get("company_name", ""),
        "is_public": target.get("is_public", True),
        "aliases": build_alias_query_terms(target),
        "channels": channel_plan_summary(target, channels),
    }
    print(json.dumps(plan, ensure_ascii=False, indent=2))
    if args.dry_run:
        return 0

    run_status: dict[str, Any] = {
        "research_key": target_key(target),
        "started_at": datetime.now().isoformat(timespec="seconds"),
        "channels": {},
    }
    for channel in channels:
        print(f"\n=== Running channel: {channel} ===")
        run_status["channels"][channel] = run_channel(target, channel, args.skip_transcript, web_max_queries=args.web_max_queries)
        sync_outputs(target, [channel])

    run_status["sync"] = sync_outputs(target, channels)
    run_status["source_inventory"] = str(source_inventory(target))
    run_status["evidence_map"] = str(evidence_map(target))
    run_status["finished_at"] = datetime.now().isoformat(timespec="seconds")

    status_path = target_script_root(target) / "_collect_target_status.json"
    status_path.parent.mkdir(parents=True, exist_ok=True)
    status_path.write_text(json.dumps(run_status, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nWrote status: {status_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
