"""
Phase 2: 播客采集
- Apple iTunes Search API (免费, 无需key)
- 搜索相关episode, 获取元数据
- 保存到 companies/{slug}/_staging/sources/podcasts/metadata/
"""

import os
import sys
import re
import json
import argparse
import requests
import time
from pathlib import Path
from datetime import datetime

DB_DIR = Path(os.environ.get('ALIKE_DB_DIR', str(Path(__file__).parent.parent)))

try:
    from target_config import (
        build_alias_query_terms,
        get_channel,
        get_channel_queries,
        load_target,
        target_script_root,
        target_key,
    )
except ImportError:
    load_target = None
    target_script_root = None


def target_output_root(ticker, target=None):
    if target and target_script_root:
        return target_script_root(target)
    return DB_DIR / ticker


def podcast_metadata_dir(ticker, target=None):
    path = target_output_root(ticker, target) / "sources" / "podcasts" / "metadata"
    path.mkdir(parents=True, exist_ok=True)
    return path


def search_itunes_episodes(query, limit=30):
    """Search Apple Podcasts for episodes matching a query."""
    url = "https://itunes.apple.com/search"
    params = {
        "term": query,
        "media": "podcast",
        "entity": "podcastEpisode",
        "limit": limit,
        "lang": "en_us",
    }
    try:
        r = requests.get(url, params=params, timeout=15)
        if r.status_code == 200:
            data = r.json()
            return data.get("results", [])
    except Exception as e:
        print(f"  iTunes search error: {e}")
    return []


def search_itunes_cn(query, limit=20):
    """Search Apple Podcasts for Chinese episodes."""
    url = "https://itunes.apple.com/search"
    params = {
        "term": query,
        "media": "podcast",
        "entity": "podcastEpisode",
        "limit": limit,
        "country": "CN",
    }
    try:
        r = requests.get(url, params=params, timeout=15)
        if r.status_code == 200:
            data = r.json()
            return data.get("results", [])
    except Exception as e:
        print(f"  iTunes CN search error: {e}")
    return []


def _split_aliases(company_name, aliases_text=None):
    """Return primary name plus optional aliases.

    Aliases let us handle ambiguous names such as "Block", where the ticker
    alone is too noisy and founder/product terms are better search anchors.
    """
    names = []
    for chunk in [company_name, aliases_text or ""]:
        for part in re.split(r"[|,]", chunk or ""):
            name = part.strip()
            if name and name.lower() not in {n.lower() for n in names}:
                names.append(name)
    return names


def _keyword_in_text(keyword, text):
    keyword = (keyword or "").strip().lower()
    if not keyword:
        return False
    # Short tickers such as SQ should match as standalone tokens, not as a
    # substring inside unrelated words.
    if len(keyword) <= 3 and keyword.isalnum():
        return re.search(rf"\b{re.escape(keyword)}\b", text, re.IGNORECASE) is not None
    return keyword in text


def filter_relevant_episodes(episodes, ticker, company_name, months=12, aliases=None, min_duration_min=10):
    """Filter episodes for relevance and recency."""
    cutoff = datetime.now().timestamp() - months * 30 * 86400
    relevant = []

    keywords = [ticker, company_name] + (aliases or [])

    for ep in episodes:
        # Check date
        release_date = ep.get("releaseDate", "")
        try:
            dt = datetime.fromisoformat(release_date.replace("Z", "+00:00"))
            if dt.timestamp() < cutoff:
                continue
        except:
            pass

        duration_min = round(ep.get("trackTimeMillis", 0) / 60000, 1) if ep.get("trackTimeMillis") else 0
        if min_duration_min and duration_min and duration_min < min_duration_min:
            continue

        # Check relevance - title or description should mention company
        title = (ep.get("trackName", "") or "").lower()
        desc = (ep.get("description", "") or "").lower()
        text = title + " " + desc

        is_relevant = any(_keyword_in_text(kw, text) for kw in keywords)
        if not is_relevant:
            continue

        relevant.append({
            "title": ep.get("trackName", "Unknown"),
            "show": ep.get("collectionName", "Unknown"),
            "date": release_date[:10] if release_date else "Unknown",
            "duration_min": duration_min,
            "description": (ep.get("description", "") or "")[:500],
            "audio_url": ep.get("episodeUrl", ""),
            "episode_url": ep.get("trackViewUrl", ""),
            "feed_url": ep.get("feedUrl", ""),
            "collection_id": ep.get("collectionId", ""),
            "artwork": ep.get("artworkUrl160", ""),
        })

    # Sort by date descending
    relevant.sort(key=lambda x: x.get("date", ""), reverse=True)
    return relevant


def _frontmatter_extra(target=None):
    if not target:
        return ""
    return (
        f"company: {json.dumps(target.get('company_name', ''))}\n"
        f"research_key: {target_key(target)}\n"
        f"credibility: S2-S3\n"
        f"evidence: E2\n"
        f"fetched_at: {datetime.now().isoformat(timespec='seconds')}\n"
    )


def save_podcast_metadata(ticker, episodes, target=None):
    """Save podcast episode metadata as individual markdown files."""
    sources_dir = podcast_metadata_dir(ticker, target)

    saved = []
    for ep in episodes:
        title = ep["title"]
        safe_title = re.sub(r'[^\w\s-]', '', title)[:50].strip().replace(' ', '-')
        date_str = ep.get("date", "unknown")[:10]
        base_filename = f"{date_str}_{safe_title or 'untitled'}"
        filename = f"{base_filename}.md"
        filepath = sources_dir / filename
        collision_index = 2
        while filepath.exists():
            filename = f"{base_filename}_{collision_index}.md"
            filepath = sources_dir / filename
            collision_index += 1

        content = f"""---
ticker: {ticker}
type: podcast
title: {json.dumps(title)}
show: {json.dumps(ep['show'])}
date: {date_str}
duration: {ep['duration_min']}min
url: {json.dumps(ep.get('episode_url', ''))}
audio_url: {json.dumps(ep.get('audio_url', ''))}
{_frontmatter_extra(target)}source: apple_podcasts
source_platform: apple_podcasts
transcript_method: pending
language: unknown
relevance: medium
---

# {title}

## 节目信息
- **节目**: {ep['show']}
- **日期**: {date_str}
- **时长**: {ep['duration_min']}分钟
- **链接**: {ep.get('episode_url', 'N/A')}

## 描述
{ep.get('description', 'N/A')}

## 转录全文
*待转录 - 音频URL: {ep.get('audio_url', 'N/A')}*
"""

        filepath.write_text(content, encoding="utf-8")
        saved.append({"file": str(filepath), "title": title})

    return saved


def default_search_queries(ticker, company_name, aliases):
    """Build the legacy public-company podcast query set."""
    search_queries = []
    for name in aliases[:6]:
        search_queries.extend([
            f"{name} earnings",
            f"{name} CEO interview",
            f"{name} founder interview",
            f"{name} stock analysis",
        ])
    search_queries.extend([f"{ticker} stock", f"{company_name} podcast"])
    return list(dict.fromkeys(search_queries))


def write_podcast_query_map(ticker, company_name, aliases, search_queries, relevance_terms, min_duration_min, target=None):
    """Persist the pre-search reasoning map so coverage can be audited later."""
    path = podcast_metadata_dir(ticker, target) / "_podcast_query_map.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    target_name = target.get("company_name", company_name) if target else company_name
    content = f"""---
ticker: {ticker}
type: podcast_query_map
company: {json.dumps(target_name, ensure_ascii=False)}
generated_at: {datetime.now().isoformat(timespec='seconds')}
min_duration_min: {min_duration_min}
---

# Podcast Query Map: {target_name}

## 元思考

播客搜索前必须先列出关键词宇宙，避免只搜公司名导致 founder / C-level / 产品 / 行业访谈漏抓。

## 公司与别名

{chr(10).join(f"- {name}" for name in aliases) if aliases else "- N/A"}

## 搜索 Query

{chr(10).join(f"- {query}" for query in search_queries) if search_queries else "- N/A"}

## Relevance Terms

{chr(10).join(f"- {term}" for term in relevance_terms) if relevance_terms else "- N/A"}

## 过滤规则

- 已知时长小于 {min_duration_min} 分钟的 episode 默认跳过。
- 未知时长不直接丢弃，后续在转录和 relevance review 中再判断。
- 搜索完整性需要覆盖：公司名、别名、Founder/C-level、核心产品、行业关键词、重要客户/伙伴、竞争对手、组织/AI 转型相关词。
"""
    path.write_text(content, encoding="utf-8")
    return path


def episode_relevance_score(ep, relevance_terms):
    """Score an episode for organization-research relevance."""
    text = f"{ep.get('title', '')} {ep.get('show', '')} {ep.get('description', '')}".lower()
    score = 0
    matched = []
    for term in relevance_terms:
        clean = str(term).strip()
        if clean and clean.lower() in text:
            score += 3 if len(clean.split()) > 1 else 1
            matched.append(clean)
    if "interview" in text:
        score += 2
    if "founder" in text or "ceo" in text:
        score += 2
    if "transcript" in text:
        score += 1
    ep["org_relevance_score"] = score
    ep["org_relevance_terms"] = matched
    return score


def write_curated_episodes(ticker, episodes, relevance_terms, max_items=None, target=None):
    """Save a relevance-ranked episode list for downstream transcription."""
    curated = [dict(ep) for ep in episodes]
    for ep in curated:
        episode_relevance_score(ep, relevance_terms)
    curated.sort(
        key=lambda ep: (ep.get("org_relevance_score", 0), ep.get("duration_min", 0), ep.get("date", "")),
        reverse=True,
    )
    if max_items and max_items > 0:
        curated = curated[:max_items]
    path = podcast_metadata_dir(ticker, target) / "_podcast_episodes_org_curated.json"
    path.write_text(json.dumps(curated, ensure_ascii=False, indent=2), encoding="utf-8")
    return curated


def fetch_podcasts_for_company(
    ticker,
    company_name,
    company_name_cn=None,
    aliases_text=None,
    search_queries=None,
    relevance_terms=None,
    query_limit=20,
    months=12,
    min_duration_min=10,
    target=None,
):
    """Search and save podcast episodes for a company."""
    print(f"[播客] Searching for {ticker} ({company_name})...")

    all_episodes = []

    aliases = _split_aliases(company_name, aliases_text)

    # English searches. Target mode supplies its own query set; positional mode
    # keeps the existing public-company defaults for backwards compatibility.
    search_queries = search_queries or default_search_queries(ticker, company_name, aliases)
    search_queries = list(dict.fromkeys(search_queries))
    relevance_terms = relevance_terms or aliases
    query_map_path = write_podcast_query_map(
        ticker,
        company_name,
        aliases,
        search_queries,
        relevance_terms,
        min_duration_min,
        target=target,
    )
    print(f"  ✓ 保存 podcast query map: {query_map_path}")

    for query in search_queries:
        print(f"  搜索: {query}")
        results = search_itunes_episodes(query, limit=query_limit)
        if results:
            filtered = filter_relevant_episodes(
                results,
                ticker,
                company_name,
                months=months,
                aliases=aliases,
                min_duration_min=min_duration_min,
            )
            print(f"    找到 {len(results)} 结果, {len(filtered)} 个相关")
            all_episodes.extend(filtered)
        time.sleep(1)  # Rate limiting

    # Chinese searches
    if company_name_cn:
        cn_queries = [f"{company_name_cn}", f"{company_name_cn} 分析"]
        for query in cn_queries:
            print(f"  搜索(中文): {query}")
            results = search_itunes_cn(query, limit=20)
            if results:
                filtered = filter_relevant_episodes(
                    results,
                    ticker,
                    company_name,
                    min_duration_min=min_duration_min,
                )
                # Also check Chinese name
                for ep in results:
                    text = (ep.get("trackName", "") + " " + ep.get("description", "")).lower()
                    duration_min = round(ep.get("trackTimeMillis", 0) / 60000, 1) if ep.get("trackTimeMillis") else 0
                    if min_duration_min and duration_min and duration_min < min_duration_min:
                        continue
                    if company_name_cn.lower() in text:
                        ep_data = {
                            "title": ep.get("trackName", "Unknown"),
                            "show": ep.get("collectionName", "Unknown"),
                            "date": (ep.get("releaseDate", "") or "")[:10],
                            "duration_min": duration_min,
                            "description": (ep.get("description", "") or "")[:500],
                            "audio_url": ep.get("episodeUrl", ""),
                            "episode_url": ep.get("trackViewUrl", ""),
                            "feed_url": ep.get("feedUrl", ""),
                            "collection_id": ep.get("collectionId", ""),
                        }
                        if ep_data not in all_episodes:
                            all_episodes.append(ep_data)
                print(f"    找到 {len(results)} 结果")
            time.sleep(1)

    # Deduplicate by title
    seen_titles = set()
    unique = []
    for ep in all_episodes:
        t = ep["title"].lower()
        if t not in seen_titles:
            seen_titles.add(t)
            unique.append(ep)

    print(f"\n  共找到 {len(unique)} 个独立相关episode")

    if unique:
        saved = save_podcast_metadata(ticker, unique, target=target)
        print(f"  ✓ 保存了 {len(saved)} 个episode元数据")

    # Save full list as JSON for later processing
    json_path = podcast_metadata_dir(ticker, target) / "_podcast_episodes.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(unique, f, ensure_ascii=False, indent=2)

    curated = write_curated_episodes(ticker, unique, relevance_terms, target=target)
    print(f"  ✓ 保存 curated episode list: {len(curated)} 条")

    return unique


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ticker", nargs="?")
    parser.add_argument("company_name", nargs="?")
    parser.add_argument("company_name_cn", nargs="?")
    parser.add_argument("aliases", nargs="?")
    parser.add_argument("--target", dest="target_name")
    parser.add_argument("--min-duration-min", type=int, default=None)
    args = parser.parse_args()

    if args.target_name:
        if not load_target:
            raise RuntimeError("target_config.py is required for --target")
        target = load_target(args.target_name)
        key = target_key(target)
        channel_cfg = get_channel(target, "podcasts")
        alias_terms = build_alias_query_terms(target)
        configured_queries = get_channel_queries(target, "podcasts")
        relevance_terms = channel_cfg.get("relevance_terms", []) + alias_terms
        fetch_podcasts_for_company(
            key,
            target.get("company_name", key),
            target.get("company_name_cn"),
            "|".join(alias_terms),
            search_queries=configured_queries,
            relevance_terms=relevance_terms,
            query_limit=int(channel_cfg.get("query_limit", 20)),
            months=int(channel_cfg.get("months", 12)),
            min_duration_min=(
                args.min_duration_min
                if args.min_duration_min is not None
                else int(channel_cfg.get("min_duration_min", os.environ.get("PODCAST_MIN_DURATION_MIN", 10)))
            ),
            target=target,
        )
    else:
        if not args.ticker:
            print("Usage: python fetch_podcasts.py TICKER [COMPANY_NAME] [COMPANY_NAME_CN] [ALIASES_PIPE_SEPARATED]")
            print("   or: python fetch_podcasts.py --target TARGET_KEY")
            sys.exit(1)

        ticker = args.ticker
        name = args.company_name if args.company_name else ticker
        name_cn = args.company_name_cn
        aliases = args.aliases

        fetch_podcasts_for_company(
            ticker,
            name,
            name_cn,
            aliases,
            min_duration_min=(
                args.min_duration_min
                if args.min_duration_min is not None
                else int(os.environ.get("PODCAST_MIN_DURATION_MIN", 10))
            ),
        )
