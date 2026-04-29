"""
小宇宙 (Xiaoyuzhou) Podcast Search
- 小宇宙没有公开API，通过搜索引擎间接获取
- 也可直接搜索其网页版 xiaoyuzhoufm.com
- 保存到 {TICKER}/sources/podcasts/
"""

import sys
import re
import json
import requests
import time
from pathlib import Path
from datetime import datetime

DB_DIR = Path(__file__).parent.parent


def search_xiaoyuzhou_web(query: str, limit=20) -> list[dict]:
    """
    Search 小宇宙 via their web interface.
    小宇宙 web version: https://www.xiaoyuzhoufm.com/search?q=xxx&type=episode
    """
    results = []
    url = "https://www.xiaoyuzhoufm.com/search"
    params = {"q": query, "type": "episode"}

    try:
        # The web search returns HTML, we need to parse it
        # But since there's no public API, we'll use a different approach:
        # Search Google/Bing for site:xiaoyuzhoufm.com
        print(f"  [小宇宙] 搜索: {query}")

        # Approach 1: Try the mobile API (known from reverse engineering)
        api_url = "https://api.xiaoyuzhoufm.com/v1/search"
        api_headers = {
            'User-Agent': 'Xiaoyuzhou/2.57.1 (iPhone; iOS 17.0)',
            'Content-Type': 'application/json',
            'x-jike-device-id': 'web-search',
        }
        payload = {
            "keyword": query,
            "type": "EPISODE",
            "loadMoreKey": None,
        }

        r = requests.post(api_url, json=payload, headers=api_headers, timeout=15)
        if r.status_code == 200:
            data = r.json()
            episodes = data.get('data', [])
            for ep in episodes[:limit]:
                ep_data = ep.get('episode', ep)
                results.append({
                    "title": ep_data.get('title', ''),
                    "show": ep_data.get('podcast', {}).get('title', '') if isinstance(ep_data.get('podcast'), dict) else '',
                    "date": (ep_data.get('pubDate', '') or '')[:10],
                    "duration_min": round(ep_data.get('duration', 0) / 60) if ep_data.get('duration') else 0,
                    "description": (ep_data.get('description', '') or ep_data.get('shownotes', ''))[:500],
                    "eid": ep_data.get('eid', ''),
                    "audio_url": ep_data.get('enclosure', {}).get('url', '') if isinstance(ep_data.get('enclosure'), dict) else ep_data.get('mediaKey', ''),
                    "episode_url": f"https://www.xiaoyuzhoufm.com/episode/{ep_data.get('eid', '')}",
                    "source_platform": "xiaoyuzhou",
                    "language": "zh",
                })
            if results:
                print(f"    ✓ 找到 {len(results)} 个episode (via API)")
                return results
    except Exception as e:
        print(f"    API搜索失败: {e}")

    # Approach 2: Fallback - use Google to search xiaoyuzhoufm.com
    # This will be handled by the research.py using WebSearch tool
    print(f"    小宇宙API不可用, 将在research阶段通过WebSearch搜索")
    return results


def save_xiaoyuzhou_episodes(ticker: str, episodes: list[dict]) -> list[dict]:
    """Save 小宇宙 episode metadata as markdown files."""
    sources_dir = DB_DIR / ticker / "sources" / "podcasts"
    sources_dir.mkdir(parents=True, exist_ok=True)

    saved = []
    for ep in episodes:
        title = ep.get("title", "unknown")
        safe_title = re.sub(r'[^\w\s-]', '', title)[:50].strip().replace(' ', '-')
        if not safe_title:
            safe_title = ep.get('eid', 'unknown')[:20]
        date_str = ep.get("date", "unknown")[:10]
        filename = f"{date_str}_xy_{safe_title}.md"

        content = f"""---
ticker: {ticker}
type: podcast
title: "{title}"
show: "{ep.get('show', '')}"
date: {date_str}
duration: {ep.get('duration_min', 0)}min
url: {ep.get('episode_url', '')}
audio_url: {ep.get('audio_url', '')}
source_platform: xiaoyuzhou
transcript_method: pending
language: zh
relevance: medium
---

# {title}

## 节目信息
- **节目**: {ep.get('show', 'N/A')}
- **日期**: {date_str}
- **时长**: {ep.get('duration_min', '?')}分钟
- **平台**: 小宇宙
- **链接**: {ep.get('episode_url', 'N/A')}

## 描述
{ep.get('description', 'N/A')}

## 转录全文
*待转录 - 音频URL: {ep.get('audio_url', 'N/A')}*
"""

        filepath = sources_dir / filename
        filepath.write_text(content, encoding='utf-8')
        saved.append({"file": str(filepath), "title": title})

    return saved


def fetch_xiaoyuzhou_for_company(ticker: str, company_name: str, company_name_cn: str = None):
    """Search and save 小宇宙 podcast episodes for a company."""
    print(f"[小宇宙] Searching for {ticker} ({company_name})...")

    all_episodes = []
    seen_titles = set()

    # Search queries
    queries = []
    if company_name_cn:
        queries.extend([company_name_cn, f"{company_name_cn} 分析"])
    queries.extend([company_name, f"{company_name} stock"])

    for query in queries:
        episodes = search_xiaoyuzhou_web(query, limit=15)
        for ep in episodes:
            t = ep.get('title', '').lower()
            if t not in seen_titles:
                seen_titles.add(t)
                all_episodes.append(ep)
        time.sleep(1)

    print(f"  共找到 {len(all_episodes)} 个小宇宙episode")

    if all_episodes:
        saved = save_xiaoyuzhou_episodes(ticker, all_episodes)
        print(f"  ✓ 保存了 {len(saved)} 个episode元数据")

    return all_episodes


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_xiaoyuzhou.py TICKER COMPANY_NAME [COMPANY_NAME_CN]")
        sys.exit(1)

    ticker = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else ticker
    name_cn = sys.argv[3] if len(sys.argv) > 3 else None
    fetch_xiaoyuzhou_for_company(ticker, name, name_cn)
