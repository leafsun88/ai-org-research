"""Semi-public channel scaffolding that mirrors the existing collect skill."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from .common import SEMI_PUBLIC_DIRS, PublicCompanyTarget, write_json, write_markdown, write_probe_report


DEFAULT_CHANNEL_QUERIES = {
    "podcasts": ["{company} CEO podcast", "{ticker} earnings podcast", "{company} industry podcast"],
    "youtube": ["{company} CEO interview", "{ticker} earnings call", "{company} investor day"],
    "substack": ["{ticker} {company} Substack", "{company} industry analysis"],
    "official": ["{company} investor relations", "{company} annual report"],
    "jobs_org": ["{company} careers engineering", "{company} jobs organization"],
    "founder_voice": ["{company} founder interview", "{company} CEO interview"],
    "web_longform": ["{company} longform analysis", "{ticker} deep dive"],
    "social_community": ["{ticker} reddit investing", "{company} hacker news"],
    "investor_views": ["{ticker} investor letter", "{ticker} hedge fund position"],
    "short_seller_reports": ["{ticker} short seller report", "{company} short report"],
}


def _configured_queries(target: PublicCompanyTarget, channel: str) -> list[str]:
    cfg = (target.config.get("channels") or {}).get(channel) or {}
    queries = cfg.get("queries") or []
    if queries:
        return [str(item) for item in queries]
    return [item.format(company=target.company_name, ticker=target.ticker) for item in DEFAULT_CHANNEL_QUERIES.get(channel, [])]


def scaffold_semi_public(target: PublicCompanyTarget) -> dict[str, Any]:
    root = target.public_company_root / "semi_public"
    status: dict[str, Any] = {"status": "ok", "channels": {}, "items": [], "gaps": []}
    for channel in SEMI_PUBLIC_DIRS:
        channel_dir = root / channel
        queries = _configured_queries(target, channel)
        payload = {
            "company": target.company_name,
            "ticker": target.ticker,
            "channel": channel,
            "status": "scaffolded",
            "queries": queries,
            "source_rule": "Save real URLs and source artifacts only; summaries are stored separately and never labeled as originals.",
            "recommended_existing_collect_command": (
                f"python3 scripts/discovery/collect_target.py {target.ticker} --channels {channel} "
                "--skip-transcript --web-max-queries 8"
                if channel not in {"investor_views", "short_seller_reports"}
                else None
            ),
            "updated_at": datetime.now().isoformat(timespec="seconds"),
        }
        write_json(channel_dir / "_collection_status.json", payload)
        write_json(channel_dir / "_query_map.json", {"queries": queries, "updated_at": payload["updated_at"]})
        write_markdown(
            channel_dir / "_query_map.md",
            [
                f"# {target.company_name} {channel} Query Map",
                "",
                *[f"- {query}" for query in queries],
            ],
        )
        status["channels"][channel] = {"queries": len(queries), "path": str(channel_dir)}
        status["items"].append({"channel": channel, "queries": len(queries)})
    write_probe_report(target, "semi_public_scaffold", status)
    return status

