"""Target-driven public web source discovery.

This script uses the shared target manifest to search for source URLs, fetch
public full text when accessible, and leave explicit status/failure files. It
is intentionally generic: company names and search terms come from config.
"""

from __future__ import annotations

import argparse
import json
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Any

from fetch_perplexity import fetch_full_text, query_perplexity_urls
from target_config import (
    build_alias_query_terms,
    get_channel_queries,
    get_channel_seed_urls,
    load_target,
    resolve_target_path,
    target_key,
    target_script_root,
    target_vault_root,
)


PAYWALL_DOMAINS = {
    "bloomberg.com",
    "wsj.com",
    "ft.com",
    "theinformation.com",
    "stratechery.com",
    "nytimes.com",
}


def safe_filename(value: str, fallback: str) -> str:
    clean = re.sub(r"[^A-Za-z0-9\s-]", "", value or "")[:80].strip()
    clean = re.sub(r"\s+", "_", clean).lower()
    return clean or fallback


def infer_title(item: dict[str, Any], url: str, index: int) -> str:
    title = item.get("title") or item.get("brief") or ""
    if title:
        return str(title)[:160]
    tail = url.rstrip("/").split("/")[-1]
    return tail[:100] or f"source_{index}"


def source_domain(url: str) -> str:
    match = re.match(r"https?://([^/]+)", url)
    return match.group(1).lower() if match else ""


def is_paywall(url: str) -> bool:
    domain = source_domain(url)
    return any(domain == d or domain.endswith(f".{d}") for d in PAYWALL_DOMAINS)


def unique_strings(values: list[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        clean = str(value or "").strip()
        key = clean.lower()
        if clean and key not in seen:
            seen.add(key)
            result.append(clean)
    return result


def parse_podcast_query_map(path: Path) -> list[str]:
    """Extract bullet queries from the generated podcast query map."""
    if not path.exists():
        return []
    queries: list[str] = []
    in_query_section = False
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            in_query_section = stripped in {"## 搜索 Query", "## Search Queries"}
            continue
        if in_query_section and stripped.startswith("- "):
            value = stripped[2:].strip()
            if value and value != "N/A":
                queries.append(value)
    return unique_strings(queries)


def read_podcast_query_map(target: dict[str, Any]) -> tuple[list[str], str]:
    candidates = [
        target_script_root(target) / "sources" / "podcasts" / "metadata" / "_podcast_query_map.md",
        target_script_root(target) / "_podcast_query_map.md",
        target_script_root(target) / "sources" / "podcasts" / "_podcast_query_map.md",
        target_vault_root(target) / "podcasts" / "metadata" / "_podcast_query_map.md",
        target_vault_root(target) / "podcasts" / "_podcast_query_map.md",
    ]
    for path in candidates:
        queries = parse_podcast_query_map(path)
        if queries:
            return queries, str(path)
    return [], ""


def build_channel_queries(target: dict[str, Any], channel: str, max_queries: int = 0) -> tuple[list[str], str, list[str]]:
    inherited_queries, inherited_path = read_podcast_query_map(target)
    configured_queries = get_channel_queries(target, channel)
    fallback_queries = []
    if not inherited_queries and not configured_queries:
        fallback_queries = build_alias_query_terms(target)

    queries = unique_strings(inherited_queries + configured_queries + fallback_queries)
    if max_queries > 0:
        queries = queries[:max_queries]
    return queries, inherited_path, inherited_queries


def query_map_name(channel: str) -> str:
    if channel == "web_longform":
        return "_web_query_map.md"
    return f"_{channel}_query_map.md"


def source_metadata_dir(output_dir: Path) -> Path:
    path = output_dir / "metadata"
    path.mkdir(parents=True, exist_ok=True)
    return path


def source_transcripts_dir(output_dir: Path) -> Path:
    path = output_dir / "transcripts"
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_query_map(
    output_dir: Path,
    target: dict[str, Any],
    channel: str,
    queries: list[str],
    inherited_path: str,
    inherited_queries: list[str],
) -> Path:
    output_dir = source_metadata_dir(output_dir)
    path = output_dir / query_map_name(channel)
    lines = [
        "---",
        f"company: {json.dumps(target.get('company_name', ''))}",
        f"research_key: {target_key(target)}",
        f"type: {channel}_query_map",
        f"channel: {channel}",
        f"generated_at: {datetime.now().isoformat(timespec='seconds')}",
        "---",
        "",
        f"# {channel} Query Map: {target.get('company_name', target_key(target))}",
        "",
        "## Inherited Podcast Query Map",
        "",
        f"- path: {inherited_path or 'none'}",
        f"- inherited_query_count: {len(inherited_queries)}",
        "",
        "## Final Queries",
        "",
    ]
    lines.extend(f"- {query}" for query in queries)
    if not queries:
        lines.append("- N/A")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def build_prompt(target: dict[str, Any], channel: str, query: str) -> str:
    company = target.get("company_name", target_key(target))
    aliases = ", ".join(build_alias_query_terms(target)[:24])
    people = ", ".join((target.get("founders", []) + target.get("executives", []))[:16])
    category = target.get("category", "company")
    public_or_private = "private AI lab" if not target.get("is_public", True) else "public company"

    return f"""You are a search engine. Find real public URLs for research on this {public_or_private}: {company}.

Research channel: {channel}
Specific search focus: {query}
Company category: {category}
Known aliases/products/terms: {aliases}
Key people: {people}

Return ONLY a valid JSON array. Each element must use this shape:
{{"url":"https://...","title":"exact title if known","source":"publication or site","date":"YYYY-MM-DD or unknown","brief":"12 words max","paywall":false}}

Rules:
- Include only real URLs that actually exist.
- Prefer primary sources, founder/executive interviews, official docs, long-form analysis, transcript pages, and high-signal community discussions.
- It is okay to include paywalled URLs, but set paywall=true when likely paywalled.
- Do not invent URLs, titles, dates, or quotes.
- No markdown, no explanation, no code fence.
- Return [] if you cannot find reliable URLs."""


def dedupe_items(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen = set()
    result = []
    for item in items:
        url = str(item.get("url", "")).strip()
        if not url.startswith("http") or url in seen:
            continue
        seen.add(url)
        result.append(item)
    return result


def seed_url_items(target: dict[str, Any], channel: str) -> list[dict[str, Any]]:
    return [
        {
            "url": url,
            "title": url.rstrip("/").split("/")[-1] or target.get("company_name", ""),
            "source": source_domain(url),
            "date": "unknown",
            "brief": f"configured seed for {channel}",
            "seed": True,
        }
        for url in get_channel_seed_urls(target, channel)
    ]


def discover_urls(
    target: dict[str, Any],
    channel: str,
    max_queries: int = 0,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str], str, list[str]]:
    items = seed_url_items(target, channel)
    query_statuses: list[dict[str, Any]] = []
    queries, inherited_path, inherited_queries = build_channel_queries(target, channel, max_queries=max_queries)

    for index, query in enumerate(queries, 1):
        print(f"  [{channel}] query {index}/{len(queries)}: {query}")
        found = query_perplexity_urls(build_prompt(target, channel, query))
        query_statuses.append({
            "query": query,
            "provider": "perplexity",
            "returned_urls": len(found),
            "status": "success" if found else "no_results_or_provider_failed",
        })
        for item in found:
            if isinstance(item, dict):
                item.setdefault("query", query)
                items.append(item)
        time.sleep(0.5)

    return dedupe_items(items), query_statuses, queries, inherited_path, inherited_queries


def save_index(output_dir: Path, items: list[dict[str, Any]]) -> None:
    output_dir = source_metadata_dir(output_dir)
    (output_dir / "_url_index.json").write_text(
        json.dumps(items, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_status(output_dir: Path, target: dict[str, Any], channel: str, statuses: list[dict[str, Any]]) -> None:
    failures = [item for item in statuses if item.get("status") != "success"]
    status_doc = {
        "research_key": target_key(target),
        "company": target.get("company_name", ""),
        "channel": channel,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total_records": len(statuses),
        "success_records": len(statuses) - len(failures),
        "failure_records": len(failures),
        "statuses": statuses,
    }
    output_dir = source_metadata_dir(output_dir)
    (output_dir / "_collection_status.json").write_text(
        json.dumps(status_doc, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (output_dir / "_collection_failures.json").write_text(
        json.dumps(failures, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_search_status(
    output_dir: Path,
    target: dict[str, Any],
    channel: str,
    query_statuses: list[dict[str, Any]],
    query_map_path: Path,
    inherited_path: str,
) -> None:
    output_dir = source_metadata_dir(output_dir)
    payload = {
        "research_key": target_key(target),
        "company": target.get("company_name", ""),
        "channel": channel,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "query_map": str(query_map_path),
        "inherited_podcast_query_map": inherited_path,
        "query_count": len(query_statuses),
        "total_returned_urls": sum(int(item.get("returned_urls", 0)) for item in query_statuses),
        "statuses": query_statuses,
    }
    (output_dir / "_search_status.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def save_markdown(output_dir: Path, target: dict[str, Any], channel: str, item: dict[str, Any], text: str, index: int) -> Path:
    output_dir = source_transcripts_dir(output_dir)
    url = item.get("url", "")
    title = infer_title(item, url, index)
    date = item.get("date") or "unknown"
    source = item.get("source") or source_domain(url)
    filename = f"{safe_filename(str(date), 'unknown')}_{safe_filename(title, f'source_{index}')}.md"
    path = output_dir / filename
    content = f"""---
company: {json.dumps(target.get("company_name", ""))}
research_key: {target_key(target)}
type: {channel}
source: {json.dumps(source)}
title: {json.dumps(title)}
url: {url}
date: {date}
fetched_at: {datetime.now().isoformat(timespec="seconds")}
credibility: S2-S4
evidence: E2-E3
chars: {len(text)}
---

# {title}

**Source**: {url}
**Channel**: {channel}

---

{text}
"""
    path.write_text(content, encoding="utf-8")
    return path


def fetch_channel(target: dict[str, Any], channel: str, skip_fetch: bool = False, max_queries: int = 0) -> dict[str, Any]:
    key = target_key(target)
    output_dir = resolve_target_path(target, "script_channel", channel)
    print(f"\n[{channel}] discovering sources for {key}")
    items, query_statuses, queries, inherited_path, inherited_queries = discover_urls(
        target,
        channel,
        max_queries=max_queries,
    )
    query_map_path = write_query_map(output_dir, target, channel, queries, inherited_path, inherited_queries)
    write_search_status(output_dir, target, channel, query_statuses, query_map_path, inherited_path)
    save_index(output_dir, items)
    if skip_fetch:
        statuses = [
            {"status": "indexed_only", "url": item.get("url", ""), "title": infer_title(item, item.get("url", ""), i + 1)}
            for i, item in enumerate(items)
        ]
        write_status(output_dir, target, channel, statuses)
        return {"channel": channel, "urls": len(items), "fetched": 0, "failures": len(statuses)}

    statuses: list[dict[str, Any]] = []
    for index, item in enumerate(items, 1):
        url = str(item.get("url", ""))
        title = infer_title(item, url, index)
        if is_paywall(url) or item.get("paywall") is True:
            statuses.append({"status": "indexed_paywall", "url": url, "title": title, "stage": "paywall_filter"})
            continue
        result = fetch_full_text(url)
        if result.get("success"):
            path = save_markdown(output_dir, target, channel, item, result.get("text", ""), index)
            statuses.append({
                "status": "success",
                "url": url,
                "title": title,
                "chars": result.get("chars", 0),
                "path": str(path),
            })
        else:
            statuses.append({
                "status": "failed",
                "url": url,
                "title": title,
                "error": result.get("error", "unknown"),
                "stage": "fetch_full_text",
            })
        time.sleep(0.35)
    write_status(output_dir, target, channel, statuses)
    failures = [s for s in statuses if s.get("status") != "success"]
    return {"channel": channel, "urls": len(items), "fetched": len(statuses) - len(failures), "failures": len(failures)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    parser.add_argument("--channels", default="substack")
    parser.add_argument("--skip-fetch", action="store_true")
    parser.add_argument("--max-queries", type=int, default=0)
    args = parser.parse_args()

    target = load_target(args.target)
    channels = [c.strip() for c in args.channels.split(",") if c.strip()]
    if channels == ["all"]:
        channels = ["substack"]
    elif channels == ["all_sources"]:
        channels = [
            "substack",
            "web_longform",
            "official",
            "founder_voice",
            "enterprise_partnerships",
            "jobs_org",
            "social_community",
            "funding_compute",
        ]

    summaries = []
    for channel in channels:
        summaries.append(fetch_channel(target, channel, skip_fetch=args.skip_fetch, max_queries=args.max_queries))

    print("\nWeb source collection summary:")
    for item in summaries:
        print(f"  {item['channel']}: {item['fetched']} fetched, {item['failures']} non-fetched, {item['urls']} indexed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
