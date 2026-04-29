"""Shared helpers for public-company collection."""

from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[3]
TODAY = datetime.now().strftime("%Y-%m-%d")

RAW_FILING_DIRS = [
    "annual_reports",
    "quarterly_reports",
    "prospectus",
    "earnings_calls",
    "governance",
    "material_events",
]
PROCESSED_DIRS = ["mda", "earnings_calls", "books", "source_notes"]
DATA_DIRS = ["statements", "market_data", "valuation", "capital_signals"]
SEMI_PUBLIC_DIRS = [
    "podcasts",
    "youtube",
    "substack",
    "official",
    "jobs_org",
    "founder_voice",
    "web_longform",
    "social_community",
    "investor_views",
    "short_seller_reports",
]
METADATA_FILES = [
    "raw_manifest.json",
    "extraction_status.json",
    "api_probe_status.json",
    "collection_status.json",
]


@dataclass
class PublicCompanyTarget:
    ticker: str
    market: str
    slug: str
    company_name: str
    company_root: Path
    peer_tickers: list[str] = field(default_factory=list)
    cik: str | None = None
    ir_url: str | None = None
    website: str | None = None
    aliases: list[str] = field(default_factory=list)
    config: dict[str, Any] = field(default_factory=dict)

    @property
    def public_company_root(self) -> Path:
        return self.company_root / "vault" / "public_company"

    @property
    def display_name(self) -> str:
        return self.company_name or self.ticker

    @classmethod
    def from_config(cls, target: dict[str, Any]) -> "PublicCompanyTarget":
        output_paths = target.get("output_paths") or {}
        company_root = output_paths.get("company_root") or f"companies/{target.get('slug', target.get('ticker', 'target').lower())}"
        path = Path(company_root)
        if not path.is_absolute():
            path = PROJECT_ROOT / path
        public_company = target.get("public_company") or {}
        peer_tickers = public_company.get("peer_tickers") or target.get("peer_tickers") or []
        return cls(
            ticker=str(target.get("ticker") or target.get("research_key") or "").upper(),
            market=str(public_company.get("market") or target.get("market") or infer_market(target)).upper(),
            slug=str(target.get("slug") or slugify(target.get("company_name") or target.get("ticker") or "target")),
            company_name=str(target.get("company_name") or target.get("ticker") or "target"),
            company_root=path,
            peer_tickers=[str(item).upper() for item in peer_tickers if str(item).strip()],
            cik=normalize_cik(public_company.get("cik") or target.get("cik")),
            ir_url=public_company.get("ir_url") or target.get("ir_url"),
            website=target.get("website"),
            aliases=[str(item) for item in target.get("aliases", []) if str(item).strip()],
            config=target,
        )


def infer_market(target: dict[str, Any]) -> str:
    ticker = str(target.get("ticker") or "")
    if ticker.endswith(".HK") or target.get("exchange") == "HKEX":
        return "HK"
    if target.get("exchange") in {"SSE", "SZSE", "BSE"}:
        return "CN"
    return "US"


def normalize_cik(value: Any) -> str | None:
    if value is None or value == "":
        return None
    digits = re.sub(r"\D", "", str(value))
    return digits.zfill(10) if digits else None


def slugify(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "-", value.strip()).strip("-")
    return value.lower() or "target"


def safe_filename(value: str, max_length: int = 140) -> str:
    clean = re.sub(r"[^A-Za-z0-9._ -]+", "-", value.strip())
    clean = re.sub(r"\s+", "-", clean).strip("-._")
    return (clean or "artifact")[:max_length]


def ensure_public_company_dirs(target: PublicCompanyTarget) -> dict[str, Any]:
    root = target.public_company_root
    dirs: list[Path] = [root, root / "models", root / "metadata", root / "metadata" / "probes"]
    dirs.extend(root / "raw_filings" / item for item in RAW_FILING_DIRS)
    dirs.extend(root / "processed" / item for item in PROCESSED_DIRS)
    dirs.extend(root / "data" / item for item in DATA_DIRS)
    dirs.extend(root / "semi_public" / item for item in SEMI_PUBLIC_DIRS)
    for path in dirs:
        path.mkdir(parents=True, exist_ok=True)
    metadata_files = [root / "metadata" / item for item in METADATA_FILES]
    for path in metadata_files:
        if not path.exists():
            write_json(path, default_metadata(target, path.stem))
    return {"root": root, "dirs": dirs, "metadata_files": metadata_files}


def default_metadata(target: PublicCompanyTarget, kind: str) -> dict[str, Any]:
    return {
        "company": target.company_name,
        "ticker": target.ticker,
        "market": target.market,
        "kind": kind,
        "status": "initialized",
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        "items": [],
        "gaps": [],
    }


def write_json(path: Path, data: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    return path


def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = fieldnames or sorted({key for row in rows for key in row})
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return path


def write_markdown(path: Path, lines: Iterable[str]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path


def relative_to_project(path: Path) -> str:
    try:
        return str(path.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def write_probe_report(
    target: PublicCompanyTarget,
    node: str,
    status: dict[str, Any],
    lines: list[str] | None = None,
    as_of_date: str | None = None,
) -> dict[str, str]:
    date = as_of_date or TODAY
    root = target.public_company_root / "metadata" / "probes"
    json_path = root / f"{safe_filename(node)}_{date}.json"
    md_path = root / f"{safe_filename(node)}_{date}.md"
    status = {
        **status,
        "company": target.company_name,
        "ticker": target.ticker,
        "node": node,
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    write_json(json_path, status)
    md_lines = lines or [
        f"# {target.company_name} {node} Probe",
        "",
        f"- Status: `{status.get('status', 'unknown')}`",
        f"- Items: {len(status.get('items', [])) if isinstance(status.get('items'), list) else 0}",
        f"- Gaps: {len(status.get('gaps', [])) if isinstance(status.get('gaps'), list) else 0}",
    ]
    write_markdown(md_path, md_lines)
    return {"json": str(json_path), "md": str(md_path)}


def update_collection_status(target: PublicCompanyTarget, updates: dict[str, Any]) -> Path:
    path = target.public_company_root / "metadata" / "collection_status.json"
    current = read_json(path, default_metadata(target, "collection_status")) or {}
    current.update(updates)
    current["updated_at"] = datetime.now().isoformat(timespec="seconds")
    return write_json(path, current)


def record_extraction_gap(target: PublicCompanyTarget, gap: dict[str, Any]) -> None:
    path = target.public_company_root / "metadata" / "extraction_status.json"
    current = read_json(path, default_metadata(target, "extraction_status")) or default_metadata(target, "extraction_status")
    current.setdefault("gaps", []).append(gap)
    current["updated_at"] = datetime.now().isoformat(timespec="seconds")
    write_json(path, current)

