"""Shared target manifest helpers for discovery scripts.

Company-specific names, aliases, channels, and output paths live in
config/company_targets.json. Discovery scripts should read from this module
instead of hard-coding company names into Python files.
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PROJECT_ROOT / "config" / "company_targets.json"
DEFAULT_SCRIPT_DB_DIR = Path(os.environ.get("ALIKE_DB_DIR", str(PROJECT_ROOT / "scripts")))


def load_targets(config_path: Path | None = None) -> dict[str, dict[str, Any]]:
    """Load all configured research targets keyed by upper-case research key."""
    path = config_path or CONFIG_PATH
    if not path.exists():
        raise FileNotFoundError(f"Target config not found: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    targets = data.get("targets", {})
    if not isinstance(targets, dict):
        raise ValueError(f"Invalid target config: {path}")
    return {str(key).upper(): value for key, value in targets.items()}


def load_target(key: str, config_path: Path | None = None) -> dict[str, Any]:
    """Load a single configured research target by key, ticker, or slug."""
    lookup_key = str(key).upper()
    targets = load_targets(config_path)
    target_key = lookup_key
    if target_key not in targets:
        for candidate_key, candidate in targets.items():
            aliases = {
                str(candidate_key).upper(),
                str(candidate.get("research_key", "")).upper(),
                str(candidate.get("ticker", "")).upper(),
                str(candidate.get("slug", "")).upper(),
            }
            if lookup_key in aliases:
                target_key = candidate_key
                break
    if target_key not in targets:
        available = ", ".join(sorted(targets))
        raise KeyError(f"Unknown target {key!r}. Available targets: {available}")
    target = dict(targets[target_key])
    target.setdefault("research_key", target_key)
    target.setdefault("ticker", target["research_key"])
    target.setdefault("slug", slugify(target.get("company_name") or target_key))
    target.setdefault("aliases", [])
    target.setdefault("founders", [])
    target.setdefault("executives", [])
    target.setdefault("channels", {})
    target.setdefault("output_paths", {})
    return target


def slugify(value: str) -> str:
    """Create a filesystem-safe lower-case slug."""
    value = re.sub(r"[^A-Za-z0-9]+", "-", value.strip()).strip("-")
    return value.lower() or "target"


def unique_strings(values: list[str]) -> list[str]:
    """Return non-empty strings preserving first-seen order case-insensitively."""
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        if not value:
            continue
        clean = str(value).strip()
        key = clean.lower()
        if clean and key not in seen:
            seen.add(key)
            result.append(clean)
    return result


def build_alias_query_terms(target: dict[str, Any], include_people: bool = True) -> list[str]:
    """Build query terms from company, aliases, founders, and executives."""
    terms = [target.get("company_name", ""), target.get("ticker", ""), target.get("research_key", "")]
    terms.extend(target.get("aliases", []))
    if include_people:
        terms.extend(target.get("founders", []))
        terms.extend(target.get("executives", []))
    return unique_strings(terms)


def get_channel(target: dict[str, Any], channel: str) -> dict[str, Any]:
    """Return a channel config, defaulting to an empty disabled dict."""
    channels = target.get("channels", {})
    value = channels.get(channel, {})
    return value if isinstance(value, dict) else {}


def get_channel_queries(target: dict[str, Any], channel: str) -> list[str]:
    """Return configured queries for a channel."""
    cfg = get_channel(target, channel)
    return unique_strings([str(q) for q in cfg.get("queries", [])])


def get_channel_seed_urls(target: dict[str, Any], channel: str) -> list[str]:
    """Return configured seed URLs for a channel."""
    cfg = get_channel(target, channel)
    return unique_strings([str(url) for url in cfg.get("seed_urls", [])])


def target_script_root(target: dict[str, Any]) -> Path:
    """Return company-local staging root for a target."""
    configured = target.get("output_paths", {}).get("script_root")
    if configured:
        path = Path(configured)
        return path if path.is_absolute() else PROJECT_ROOT / path
    return target_company_root(target) / "_staging"


def target_staging_source_root(target: dict[str, Any], channel: str) -> Path:
    """Return the staging source root for a channel."""
    return target_script_root(target) / "sources" / channel


def target_staging_source_subdir(target: dict[str, Any], channel: str, subdir: str) -> Path:
    """Return a staging source subdirectory such as metadata or transcripts."""
    return target_staging_source_root(target, channel) / subdir


def target_company_root(target: dict[str, Any]) -> Path:
    """Return company research root for a target."""
    configured = target.get("output_paths", {}).get("company_root")
    if configured:
        path = Path(configured)
        return path if path.is_absolute() else PROJECT_ROOT / path
    return PROJECT_ROOT / "companies" / target.get("slug", slugify(target.get("company_name", "target")))


def target_vault_root(target: dict[str, Any]) -> Path:
    """Return company vault root for a target."""
    configured = target.get("output_paths", {}).get("vault")
    if configured:
        path = Path(configured)
        return path if path.is_absolute() else PROJECT_ROOT / path
    return target_company_root(target) / "vault"


def target_analysis_root(target: dict[str, Any]) -> Path:
    """Return company analysis root for a target."""
    configured = target.get("output_paths", {}).get("analysis")
    if configured:
        path = Path(configured)
        return path if path.is_absolute() else PROJECT_ROOT / path
    return target_company_root(target) / "analysis"


def resolve_target_path(target: dict[str, Any], area: str, channel: str | None = None) -> Path:
    """Resolve a standard target path.

    area can be: script_root, company_root, vault, analysis, script_channel,
    or vault_channel.
    """
    if area == "script_root":
        return target_script_root(target)
    if area == "company_root":
        return target_company_root(target)
    if area == "vault":
        return target_vault_root(target)
    if area == "analysis":
        return target_analysis_root(target)
    if area == "script_channel":
        if not channel:
            raise ValueError("channel is required for script_channel")
        return target_staging_source_root(target, channel)
    if area == "vault_channel":
        if not channel:
            raise ValueError("channel is required for vault_channel")
        return target_vault_root(target) / vault_channel_path(channel)
    raise ValueError(f"Unknown target path area: {area}")


def vault_channel_path(channel: str) -> str:
    """Map script channel names to company vault subpaths."""
    mapping = {
        "podcasts": "podcasts/metadata",
        "youtube": "youtube",
        "substack": "substack",
        "financials": "financials",
        "official": "official",
        "web_longform": "web",
        "founder_voice": "web/founder_voice",
        "research_safety": "web/research_safety",
        "longform_analysis": "web/longform_analysis",
        "social_community": "social",
        "enterprise_partnerships": "partnerships",
        "funding_compute": "funding",
        "jobs_org": "jobs",
    }
    return mapping.get(channel, channel)


def target_key(target: dict[str, Any]) -> str:
    """Canonical staging key used by existing scripts."""
    return target.get("research_key") or target.get("ticker")


def ensure_target_dirs(target: dict[str, Any]) -> list[Path]:
    """Create standard directories for a target and return them."""
    dirs = [
        target_company_root(target),
        target_vault_root(target),
        target_analysis_root(target),
        target_script_root(target),
    ]
    for sub in [
        "podcasts/metadata",
        "podcasts/transcripts",
        "podcasts/essence",
        "youtube/metadata",
        "youtube/transcripts",
        "youtube/essence",
        "substack/metadata",
        "substack/transcripts",
        "substack/essence",
        "financials/metadata",
        "financials/reports",
        "financials/essence",
        "_optional",
    ]:
        dirs.append(target_vault_root(target) / sub)
    for sub in [
        "sources/podcasts/metadata",
        "sources/podcasts/transcripts",
        "sources/youtube/metadata",
        "sources/youtube/transcripts",
        "sources/substack/metadata",
        "sources/substack/transcripts",
        "sources/financials/metadata",
        "sources/financials/reports",
    ]:
        dirs.append(target_script_root(target) / sub)
    for path in dirs:
        path.mkdir(parents=True, exist_ok=True)
    return dirs
