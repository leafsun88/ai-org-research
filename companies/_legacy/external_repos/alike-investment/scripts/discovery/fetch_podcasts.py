"""
Phase 2: 播客采集
- Apple iTunes Search API (免费, 无需key)
- 搜索相关episode, 获取元数据
- 保存到 {TICKER}/sources/podcasts/
"""

import os
import sys
import re
import json
import requests
import time
from pathlib import Path
from datetime import datetime

DB_DIR = Path(os.environ.get('ALIKE_DB_DIR', str(Path(__file__).parent.parent)))


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


def filter_relevant_episodes(episodes, ticker, company_name, months=12):
    """Filter episodes for relevance and recency."""
    cutoff = datetime.now().timestamp() - months * 30 * 86400
    relevant = []

    keywords = [ticker.lower(), company_name.lower()]

    for ep in episodes:
        # Check date
        release_date = ep.get("releaseDate", "")
        try:
            dt = datetime.fromisoformat(release_date.replace("Z", "+00:00"))
            if dt.timestamp() < cutoff:
                continue
        except:
            pass

        # Check relevance - title or description should mention company
        title = (ep.get("trackName", "") or "").lower()
        desc = (ep.get("description", "") or "").lower()
        text = title + " " + desc

        is_relevant = any(kw in text for kw in keywords)
        if not is_relevant:
            continue

        relevant.append({
            "title": ep.get("trackName", "Unknown"),
            "show": ep.get("collectionName", "Unknown"),
            "date": release_date[:10] if release_date else "Unknown",
            "duration_min": round(ep.get("trackTimeMillis", 0) / 60000) if ep.get("trackTimeMillis") else 0,
            "description": (ep.get("description", "") or "")[:500],
            "audio_url": ep.get("episodeUrl", ""),
            "episode_url": ep.get("trackViewUrl", ""),
            "feed_url": ep.get("feedUrl", ""),
            "artwork": ep.get("artworkUrl160", ""),
        })

    # Sort by date descending
    relevant.sort(key=lambda x: x.get("date", ""), reverse=True)
    return relevant


def save_podcast_metadata(ticker, episodes):
    """Save podcast episode metadata as individual markdown files."""
    sources_dir = DB_DIR / ticker / "sources" / "podcasts"
    sources_dir.mkdir(parents=True, exist_ok=True)

    saved = []
    for ep in episodes:
        title = ep["title"]
        safe_title = re.sub(r'[^\w\s-]', '', title)[:50].strip().replace(' ', '-')
        date_str = ep.get("date", "unknown")[:10]
        filename = f"{date_str}_{safe_title}.md"

        content = f"""---
ticker: {ticker}
type: podcast
title: "{title}"
show: "{ep['show']}"
date: {date_str}
duration: {ep['duration_min']}min
url: {ep.get('episode_url', '')}
audio_url: {ep.get('audio_url', '')}
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

        filepath = sources_dir / filename
        filepath.write_text(content, encoding="utf-8")
        saved.append({"file": str(filepath), "title": title})

    return saved


def fetch_podcasts_for_company(ticker, company_name, company_name_cn=None):
    """Search and save podcast episodes for a company."""
    print(f"[播客] Searching for {ticker} ({company_name})...")

    all_episodes = []

    # English searches
    search_queries = [
        f"{company_name} earnings",
        f"{company_name} CEO interview",
        f"{company_name} stock analysis",
        f"{ticker} stock",
    ]

    for query in search_queries:
        print(f"  搜索: {query}")
        results = search_itunes_episodes(query, limit=20)
        if results:
            filtered = filter_relevant_episodes(results, ticker, company_name)
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
                filtered = filter_relevant_episodes(results, ticker, company_name)
                # Also check Chinese name
                for ep in results:
                    text = (ep.get("trackName", "") + " " + ep.get("description", "")).lower()
                    if company_name_cn.lower() in text:
                        ep_data = {
                            "title": ep.get("trackName", "Unknown"),
                            "show": ep.get("collectionName", "Unknown"),
                            "date": (ep.get("releaseDate", "") or "")[:10],
                            "duration_min": round(ep.get("trackTimeMillis", 0) / 60000) if ep.get("trackTimeMillis") else 0,
                            "description": (ep.get("description", "") or "")[:500],
                            "audio_url": ep.get("episodeUrl", ""),
                            "episode_url": ep.get("trackViewUrl", ""),
                            "feed_url": ep.get("feedUrl", ""),
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
        saved = save_podcast_metadata(ticker, unique)
        print(f"  ✓ 保存了 {len(saved)} 个episode元数据")

    # Save full list as JSON for later processing
    json_path = DB_DIR / ticker / "_podcast_episodes.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(unique, f, ensure_ascii=False, indent=2)

    return unique


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_podcasts.py TICKER [COMPANY_NAME] [COMPANY_NAME_CN]")
        sys.exit(1)

    ticker = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else ticker
    name_cn = sys.argv[3] if len(sys.argv) > 3 else None

    fetch_podcasts_for_company(ticker, name, name_cn)
