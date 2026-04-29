#!/usr/bin/env python3
"""One-off project structure migration.

Default mode is a dry run. Use --apply to move files. The script is deliberately
conservative: it never deletes evidence, preserves name collisions, and writes a
machine-readable migration report.
"""

from __future__ import annotations

import argparse
import json
import shutil
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]
COMPANIES_ROOT = PROJECT_ROOT / "companies"
SCRIPTS_ROOT = PROJECT_ROOT / "scripts"
SKILLS_ROOT = PROJECT_ROOT / "学习" / "skills"
LEGACY_ROOT = COMPANIES_ROOT / "_legacy"
REPORT_PATH = COMPANIES_ROOT / "_meta" / "migrations" / "project_structure_migration_2026-04-21.json"
PREVIEW_REPORT_PATH = COMPANIES_ROOT / "_meta" / "migrations" / "project_structure_migration_preview_2026-04-21.json"
CONFIG_PATH = PROJECT_ROOT / "config" / "company_targets.json"

ACTIVE_SKILLS = {"collect", "analysis"}
STANDARD_VAULT_DIRS = {"podcasts", "youtube", "substack", "financials", "_optional"}
STANDARD_SOURCE_DIRS = {
    "podcasts": {"metadata", "transcripts", "essence"},
    "youtube": {"metadata", "transcripts", "essence"},
    "substack": {"metadata", "transcripts", "essence"},
    "financials": {"metadata", "reports", "essence"},
}
EMPTY_LEGACY_DIR_NAMES = {
    "youtube-essence",
    "podcast-essence",
    "source-essence",
    "financials-essence",
    "_stale_rejected",
    "podcasts_transcripts",
}


@dataclass
class MoveOp:
    src: str
    dst: str
    reason: str
    kind: str = "move"
    status: str = "planned"
    final_dst: str = ""
    error: str = ""


def unique_destination(path: Path) -> Path:
    """Return a non-existing destination path, preserving both collisions."""
    if not path.exists():
        return path

    if path.suffix:
        stem = path.with_suffix("")
        suffix = path.suffix
        index = 2
        while True:
            candidate = Path(f"{stem}_{index}{suffix}")
            if not candidate.exists():
                return candidate
            index += 1

    index = 2
    while True:
        candidate = path.parent / f"{path.name}_{index}"
        if not candidate.exists():
            return candidate
        index += 1


def classify_vault_child(source: str, child: Path, source_root: Path) -> Path | None:
    """Return the new destination for a vault child, or None if it is already canonical."""
    rel = child.relative_to(source_root)
    parts = rel.parts
    name = child.name

    if not parts or name == ".DS_Store":
        return None
    if parts[0] in STANDARD_SOURCE_DIRS.get(source, set()):
        return None

    if source == "youtube":
        if parts[0] == "youtube-essence":
            return source_root / "essence" / Path(*parts[1:])
        if parts[0] == "_stale_rejected":
            return source_root / "metadata" / "rejected_archive" / Path(*parts[1:])
        if len(parts) == 1:
            if name.startswith("_youtube_") or name.startswith("_") or name.endswith((".json", ".segments.json", ".providers.json")):
                return source_root / "metadata" / name
            if child.suffix.lower() == ".md":
                return source_root / "transcripts" / name
        return None

    if source == "substack":
        if parts[0] == "source-essence":
            return source_root / "essence" / Path(*parts[1:])
        if len(parts) == 1:
            if name.startswith("_") or child.suffix.lower() == ".json":
                return source_root / "metadata" / name
            if child.suffix.lower() == ".md":
                return source_root / "transcripts" / name
        return None

    if source == "podcasts":
        if parts[0] == "podcast-essence":
            return source_root / "essence" / Path(*parts[1:])
        if len(parts) == 1 and (name.startswith("_podcast_") or child.suffix.lower() == ".json"):
            return source_root / "metadata" / name
        if len(parts) == 1 and child.suffix.lower() == ".md":
            return source_root / "metadata" / name
        return None

    if source == "financials":
        if parts[0] == "financials-essence":
            return source_root / "essence" / Path(*parts[1:])
        if parts[0] in {"sec_filings", "earnings"}:
            return source_root / "reports" / "sec_filings" / Path(*parts[1:])
        if len(parts) == 1:
            if child.suffix.lower() in {".json", ".csv"} or name.startswith("_"):
                return source_root / "metadata" / name
            if child.suffix.lower() in {".md", ".pdf", ".html", ".txt"}:
                return source_root / "reports" / name
        return None

    return None


def iter_files(path: Path) -> Iterable[Path]:
    if path.is_file():
        yield path
        return
    if path.is_dir():
        for item in path.rglob("*"):
            if item.is_file() and item.name != ".DS_Store":
                yield item


def add_move(ops: list[MoveOp], src: Path, dst: Path, reason: str) -> None:
    if src == dst or not src.exists():
        return
    ops.append(MoveOp(str(src), str(dst), reason))


def load_config_targets() -> dict[str, dict[str, str]]:
    if not CONFIG_PATH.exists():
        return {}
    data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    result: dict[str, dict[str, str]] = {}
    for key, target in data.get("targets", {}).items():
        slug = target.get("slug") or str(key).lower()
        ticker = target.get("ticker") or key
        result[str(key).upper()] = {"slug": slug, "ticker": str(ticker)}
        result[str(ticker).upper()] = {"slug": slug, "ticker": str(ticker)}
    return result


def existing_company_slugs() -> set[str]:
    if not COMPANIES_ROOT.exists():
        return set()
    return {
        child.name
        for child in COMPANIES_ROOT.iterdir()
        if child.is_dir() and not child.name.startswith("_")
    }


def plan_standard_vault_moves(ops: list[MoveOp]) -> None:
    for slug in sorted(existing_company_slugs()):
        vault = COMPANIES_ROOT / slug / "vault"
        if not vault.exists():
            continue

        for source in ["podcasts", "youtube", "substack", "financials"]:
            source_root = vault / source
            if not source_root.exists():
                continue
            for child in list(source_root.iterdir()):
                if child.name == ".DS_Store":
                    continue
                for file in iter_files(child):
                    dst = classify_vault_child(source, file, source_root)
                    if dst:
                        add_move(ops, file, dst, f"normalize_{source}_vault")

        for child in list(vault.iterdir()):
            if child.name == ".DS_Store" or not child.is_dir():
                continue
            if child.name not in STANDARD_VAULT_DIRS:
                add_move(ops, child, vault / "_optional" / child.name, "archive_optional_vault_source")


def plan_standard_staging_moves(ops: list[MoveOp]) -> None:
    for slug in sorted(existing_company_slugs()):
        sources = COMPANIES_ROOT / slug / "_staging" / "sources"
        if not sources.exists():
            continue

        old_podcast_transcripts = sources / "podcasts_transcripts"
        if old_podcast_transcripts.exists():
            for file in iter_files(old_podcast_transcripts):
                add_move(
                    ops,
                    file,
                    sources / "podcasts" / "transcripts" / file.relative_to(old_podcast_transcripts),
                    "normalize_staging_podcast_transcripts",
                )

        for source in ["podcasts", "youtube", "substack", "financials"]:
            source_root = sources / source
            if not source_root.exists():
                continue
            for child in list(source_root.iterdir()):
                if child.name == ".DS_Store":
                    continue
                for file in iter_files(child):
                    dst = classify_vault_child(source, file, source_root)
                    if dst:
                        add_move(ops, file, dst, f"normalize_staging_{source}")


def plan_script_moves(ops: list[MoveOp]) -> None:
    target_map = load_config_targets()
    target_map.update(
        {
            "SQ": {"slug": "block", "ticker": "SQ"},
            "BLOCK": {"slug": "block", "ticker": "SQ"},
            "PERPLEXITY": {"slug": "perplexity", "ticker": "PERPLEXITY"},
            "PERPLEXITY_FALLBACK": {"slug": "perplexity", "ticker": "PERPLEXITY"},
        }
    )
    public_samples = {"BZ", "CRM", "DDOG", "HUBS", "MELI", "NET", "NOW", "PLTR", "SE", "SNOW"}

    if not SCRIPTS_ROOT.exists():
        return

    for child in sorted(SCRIPTS_ROOT.iterdir(), key=lambda p: p.name.lower()):
        if child.name in {".DS_Store", "discovery"}:
            continue
        if child.is_file():
            add_move(ops, child, LEGACY_ROOT / "root_scripts_legacy" / child.name, "archive_root_script")
        elif child.is_dir():
            key = child.name.upper()
            if key == "__PYCACHE__":
                add_move(ops, child, LEGACY_ROOT / "root_scripts_legacy" / child.name, "archive_root_script_cache")
            elif key == "PERPLEXITY_FALLBACK":
                add_move(ops, child, COMPANIES_ROOT / "perplexity" / "_staging" / "fallback", "move_company_staging_fallback")
            elif key in target_map:
                slug = target_map[key]["slug"]
                add_move(ops, child, COMPANIES_ROOT / slug / "_staging", "move_company_staging")
            elif key in public_samples:
                add_move(ops, child, LEGACY_ROOT / "public_company_samples" / child.name.lower(), "archive_public_company_sample")
            else:
                add_move(ops, child, LEGACY_ROOT / "unknown_script_outputs" / child.name, "archive_unknown_script_output")


def plan_legacy_moves(ops: list[MoveOp]) -> None:
    alike = PROJECT_ROOT / "Alike-Investment"
    if alike.exists():
        add_move(ops, alike, LEGACY_ROOT / "external_repos" / "alike-investment", "archive_external_repo")

    if SKILLS_ROOT.exists():
        for child in sorted(SKILLS_ROOT.iterdir(), key=lambda p: p.name.lower()):
            if child.is_dir() and child.name not in ACTIVE_SKILLS:
                add_move(ops, child, PROJECT_ROOT / "学习" / "_legacy" / "skills" / child.name, "archive_inactive_skill")


def build_operations() -> list[MoveOp]:
    ops: list[MoveOp] = []
    plan_standard_vault_moves(ops)
    plan_standard_staging_moves(ops)
    plan_script_moves(ops)
    plan_legacy_moves(ops)
    return ops


def ensure_standard_dirs() -> None:
    for slug in sorted(existing_company_slugs()):
        root = COMPANIES_ROOT / slug
        for rel in [
            "_staging",
            "analysis",
            "vault/podcasts/metadata",
            "vault/podcasts/transcripts",
            "vault/podcasts/essence",
            "vault/youtube/metadata",
            "vault/youtube/transcripts",
            "vault/youtube/essence",
            "vault/substack/metadata",
            "vault/substack/transcripts",
            "vault/substack/essence",
            "vault/financials/metadata",
            "vault/financials/reports",
            "vault/financials/essence",
            "vault/_optional",
        ]:
            (root / rel).mkdir(parents=True, exist_ok=True)

    for rel in [
        "root_scripts_legacy",
        "external_repos",
        "unknown_script_outputs",
        "public_company_samples",
    ]:
        (LEGACY_ROOT / rel).mkdir(parents=True, exist_ok=True)
    (PROJECT_ROOT / "学习" / "_legacy" / "skills").mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)


def apply_operations(ops: list[MoveOp]) -> list[MoveOp]:
    ensure_standard_dirs()
    applied: list[MoveOp] = []
    for op in ops:
        src = Path(op.src)
        planned_dst = Path(op.dst)
        dst = planned_dst
        if not src.exists():
            op.status = "missing_source"
            op.final_dst = str(dst)
            applied.append(op)
            continue
        try:
            if src.is_dir() and planned_dst.exists() and planned_dst.is_dir():
                planned_dst.mkdir(parents=True, exist_ok=True)
                for child in list(src.iterdir()):
                    child_dst = unique_destination(planned_dst / child.name)
                    shutil.move(str(child), str(child_dst))
                src.rmdir()
                op.status = "moved_merged"
                dst = planned_dst
            else:
                dst = unique_destination(planned_dst)
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src), str(dst))
                op.status = "moved"
            op.final_dst = str(dst)
        except Exception as exc:  # pragma: no cover - exercised in real migration
            op.status = "failed"
            op.error = repr(exc)
            op.final_dst = str(dst)
        applied.append(op)
    return applied


def cleanup_empty_legacy_dirs(apply: bool) -> list[MoveOp]:
    """Remove empty legacy directory shells after their files have moved."""
    cleanup_ops: list[MoveOp] = []
    roots: list[Path] = []
    for base in [COMPANIES_ROOT, PROJECT_ROOT / "学习"]:
        if not base.exists():
            continue
        roots.extend(path for path in base.rglob("*") if path.is_dir() and path.name in EMPTY_LEGACY_DIR_NAMES)

    for root in sorted(roots, key=lambda p: len(p.parts), reverse=True):
        candidates = sorted([p for p in root.rglob("*") if p.is_dir()] + [root], key=lambda p: len(p.parts), reverse=True)
        for path in candidates:
            if not path.exists() or not path.is_dir():
                continue
            try:
                next(path.iterdir())
            except StopIteration:
                op = MoveOp(str(path), "", "remove_empty_legacy_dir", kind="remove_empty_dir")
                if apply:
                    try:
                        path.rmdir()
                        op.status = "removed_empty_dir"
                    except Exception as exc:  # pragma: no cover - exercised in real cleanup
                        op.status = "failed"
                        op.error = repr(exc)
                else:
                    op.status = "planned"
                cleanup_ops.append(op)
    return cleanup_ops


def write_report(ops: list[MoveOp], apply: bool) -> None:
    payload = {
        "type": "project_structure_migration",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "apply": apply,
        "operation_count": len(ops),
        "status_counts": {},
        "operations": [asdict(op) for op in ops],
    }
    for op in ops:
        payload["status_counts"][op.status] = payload["status_counts"].get(op.status, 0) + 1
    report_path = REPORT_PATH if apply else PREVIEW_REPORT_PATH
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Actually move files. Default is dry-run.")
    parser.add_argument("--dry-run", action="store_true", help="Preview moves without changing files.")
    args = parser.parse_args()

    ops = build_operations()
    if args.apply:
        ops = apply_operations(ops)
        ops.extend(cleanup_empty_legacy_dirs(apply=True))
    else:
        for op in ops:
            op.final_dst = op.dst
        ensure_standard_dirs()
        ops.extend(cleanup_empty_legacy_dirs(apply=False))
    write_report(ops, apply=args.apply)
    print(f"{'Applied' if args.apply else 'Dry-run'} operations: {len(ops)}")
    print(REPORT_PATH if args.apply else PREVIEW_REPORT_PATH)
    return 0 if not any(op.status == "failed" for op in ops) else 1


if __name__ == "__main__":
    raise SystemExit(main())
