"""
Perplexity URL Discovery + WebFetch Full-Text Pipeline
=======================================================
两阶段架构:
  Phase 1: Perplexity搜索URL（只找链接，不要内容，杜绝幻觉）
  Phase 2: 逐个URL用requests抓取原始全文

设计原则:
- Perplexity只当搜索引擎，返回URL列表
- 全文由真实HTTP请求获取，不是AI编造
- 每个source保存为独立.md文件
"""

import os
import sys
import json
import re
import time
import requests
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser

DB_DIR = Path(os.environ.get('ALIKE_DB_DIR', str(Path(__file__).parent.parent)))
API_KEY = os.environ.get('PERPLEXITY_API_KEY') or os.environ.get('PPLX_API_KEY') or ''
API_URL = 'https://api.perplexity.ai/chat/completions'
HEADERS_WEB = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}


# ══════════════════════════════════════════════
# HTML → Text extractor
# ══════════════════════════════════════════════

class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []
        self.skip_tags = {'script', 'style', 'head', 'meta', 'link', 'nav', 'footer', 'header'}
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag.lower() in self.skip_tags:
            self._skip_depth += 1
        if tag.lower() in ('p', 'br', 'div', 'tr', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote'):
            self.result.append('\n')

    def handle_endtag(self, tag):
        if tag.lower() in self.skip_tags:
            self._skip_depth = max(0, self._skip_depth - 1)
        if tag.lower() in ('p', 'div', 'tr', 'table', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'article'):
            self.result.append('\n')

    def handle_data(self, data):
        if self._skip_depth == 0:
            self.result.append(data)

    def get_text(self):
        text = ''.join(self.result)
        text = re.sub(r'[ \t]+', ' ', text)
        text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
        return text.strip()


def html_to_text(html: str) -> str:
    parser = HTMLTextExtractor()
    try:
        parser.feed(html)
    except Exception:
        pass
    return parser.get_text()


# ══════════════════════════════════════════════
# Prompt Templates (通用化，变量注入)
# ══════════════════════════════════════════════

def get_url_search_prompts(ticker: str, company: str, ceo: str, industry: str = '', competitors: str = '') -> dict:
    """生成URL搜索prompt，每个prompt只要求返回URL列表JSON"""

    base_rules = """STRICT RULES:
- Return ONLY real URLs that actually exist on the internet. Do NOT fabricate or guess URLs.
- If you are not certain a URL is real, do NOT include it.
- Return valid JSON array only. No markdown, no explanation, no ```json``` wrapper, no other text before or after the JSON.
- Every URL must be a complete, valid URL starting with https:// or http://
- Do NOT include any paywall-only content (Bloomberg, WSJ subscriber-only, The Information, Stratechery member-only)."""

    return {
        # ── Twitter/X ──
        "twitter": f"""You are a search engine. Find URLs of significant Twitter/X posts about {company} (${ticker}) stock.

Return ONLY a JSON array. Each element must be exactly this format:
{{"url":"https://x.com/username/status/1234567890","handle":"@username","date":"YYYY-MM-DD","brief":"10 words max"}}

Search categories (find posts for EACH category):

1. OFFICIAL: Posts by {company}'s official account and CEO {ceo}'s personal account
2. BULL: Bullish analysis tweets about ${ticker} with high engagement (500+ likes)
3. BEAR: Bearish/short seller tweets about ${ticker}, short reports, fraud allegations
4. ANALYSTS: Sell-side analyst upgrades/downgrades, price target changes for ${ticker}
5. EARNINGS: Tweets reacting to {company} quarterly earnings (every quarter from 2022-2026)
6. NEWS: Major news — acquisitions, SEC filings, product launches, S&P 500 inclusion
7. FINTWIT INFLUENCERS: Popular finance accounts mentioning ${ticker}
8. VIRAL: Any tweet about ${ticker} exceeding 5000 likes or 500K views
9. CONTROVERSIAL: Tweets about Muddy Waters short, SEC probe, data privacy concerns
10. E-COMMERCE PIVOT: Tweets about {company}'s e-commerce advertising expansion

Time range: 2021 to present (April 2026). Search EACH year separately to ensure completeness.

{base_rules}
Minimum 100 URLs. If you cannot find 100 real ones, return as many REAL ones as you can. Quality over quantity — only real URLs.""",

        # ── Reddit ──
        "reddit": f"""You are a search engine. Find URLs of Reddit posts and comments about {company} (${ticker}) stock.

Return ONLY a JSON array. Each element must be exactly this format:
{{"url":"https://www.reddit.com/r/subreddit/comments/id/title/","subreddit":"r/stocks","title":"exact post title","date":"YYYY-MM-DD","brief":"10 words max"}}

Search these subreddits: r/stocks, r/investing, r/wallstreetbets, r/ValueInvesting, r/StockMarket, r/options, r/SecurityAnalysis, r/FluentInFinance, r/technology

Search categories:
1. DD POSTS: Any post with "DD" or "Due Diligence" or "Deep Dive" about {company} or ${ticker}
2. EARNINGS THREADS: Post-earnings discussion threads for {company} (all quarters 2022-2026)
3. BULL/BEAR DEBATES: "Is ${ticker} overvalued" or "bull case" or "bear case"
4. SHORT SELLER: Discussions about Muddy Waters or any short report on {company}
5. YOLO/POSITION: WSB position posts involving ${ticker}
6. NEWS REACTIONS: Threads reacting to major {company} news (S&P inclusion, SEC probe, etc.)
7. COMPARISON: "${ticker} vs" comparison posts with {competitors if competitors else 'competitors'}
8. GENERAL: Any post mentioning {company} or ${ticker} with 50+ upvotes

Time range: 2021 to present (April 2026).

{base_rules}
Minimum 100 URLs. Return as many REAL Reddit URLs as you can find.""",

        # ── Substack + 独立长文分析 ──
        "substack_analysis": f"""You are a search engine. Find URLs of ALL long-form analysis articles about {company} (${ticker}) stock on Substack, Seeking Alpha (free), Medium, and independent blogs.

Return ONLY a JSON array. Each element must be exactly this format:
{{"url":"https://example.substack.com/p/article-slug","title":"exact article title","author":"author name","platform":"substack","date":"YYYY-MM-DD","brief":"10 words max"}}

Search strategies:
- site:substack.com "{company}" OR "${ticker}"
- site:seekingalpha.com "{company}" (free articles only)
- site:medium.com "{company}" stock analysis
- "{company}" "${ticker}" "investment thesis"
- "{company}" "${ticker}" "deep dive"
- "{company}" "${ticker}" "valuation" analysis
- "{company}" "${ticker}" "bull case" OR "bear case"
- "{company}" earnings review analysis blog
- "{company}" short report response analysis

{base_rules}
Minimum 30 URLs. Be exhaustive — find every Substack and independent analysis you can.""",

        # ── 播客 + Transcript ──
        "podcasts_transcripts": f"""You are a search engine. Find URLs of ALL podcast episodes that discuss {company} (${ticker}) in detail. Include BOTH episodes where executives are guests AND episodes where analysts/investors discuss {company} as a main topic.

Return ONLY a JSON array. Each element must be exactly this format:
{{"url":"https://...","title":"episode title","podcast":"show name","date":"YYYY-MM-DD","guest":"guest name or null","has_transcript":true,"transcript_url":"https://... or null","brief":"10 words max"}}

Search for:
1. GUEST APPEARANCES: {ceo} or any {company} executive as guest on ANY podcast
2. EARNINGS ANALYSIS: Podcast episodes analyzing {company} earnings
3. STOCK ANALYSIS: Episodes with {company} as the main topic or prominent discussion
4. INDUSTRY: {industry if industry else 'tech/advertising'} podcasts that discuss {company}
5. POPULAR FINANCE PODCASTS: All-In, 20VC, Invest Like the Best, Acquired, My First Million, Animal Spirits, The Prof G Pod, Motley Fool, Mad Money
6. CHINESE PODCASTS: 中文播客讨论{company} (小宇宙, 喜马拉雅, etc.)

CRITICAL — also search for TRANSCRIPTS:
- "{company}" podcast transcript
- "{ceo}" interview transcript full text
- site:podscribe.com "{company}"
- site:snipd.com "{company}"
- site:podcastnotes.org "{company}"
- "{company}" OR "${ticker}" earnings call transcript site:fool.com
- "{company}" conference call transcript
- site:rev.com/blog "{company}"

{base_rules}
Minimum 50 entries. Include transcript URLs when they exist separately from episode URLs.""",

        # ── 新闻深度报道 ──
        "news_investigations": f"""You are a search engine. Find URLs of ALL significant free news articles and investigative reports about {company} (${ticker}).

Return ONLY a JSON array. Each element must be exactly this format:
{{"url":"https://...","title":"article title","source":"publication name","date":"YYYY-MM-DD","type":"news|investigation|profile|opinion","brief":"10 words max"}}

Search for:
1. INVESTIGATIVE: In-depth investigative pieces about {company}
2. CEO PROFILES: Feature stories about {ceo} — background, management style, vision
3. PRODUCT DEEP DIVES: Detailed technical analyses of {company}'s technology
4. EARNINGS COVERAGE: Major earnings coverage (beat/miss reactions)
5. CONTROVERSY: Short seller reports, SEC investigation articles, fraud allegations
6. STRATEGY: Strategic moves — acquisitions, pivots, e-commerce expansion, S&P 500 inclusion
7. INDUSTRY REPORTS: Industry reports prominently featuring {company}

Search these FREE sources:
- CNBC, Reuters, Yahoo Finance, MarketWatch, Barron's (free articles)
- TechCrunch, The Verge, Wired, Ars Technica
- Business Insider (free), Forbes, Fortune
- Industry: AdExchanger, Mobile Dev Memo, ExchangeWire, Digiday, eMarketer
- HackerNoon, VentureBeat
- Company IR page: investors.applovin.com

DO NOT include paywalled articles (Bloomberg subscriber, WSJ subscriber, FT subscriber, The Information).

{base_rules}
Minimum 50 URLs. Cover 2021-2026 comprehensively.""",
    }


# ══════════════════════════════════════════════
# Phase 1: Query Perplexity for URLs
# ══════════════════════════════════════════════

def query_perplexity_urls(prompt: str) -> list[dict]:
    """Query Perplexity and parse JSON array of URLs from response."""
    resp = requests.post(API_URL, headers={
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }, json={
        'model': 'sonar-pro',
        'messages': [
            {'role': 'system', 'content': 'You are a search engine that returns ONLY valid JSON arrays of URLs. Never include explanations, markdown formatting, or any text outside the JSON array. Return [] if you find nothing.'},
            {'role': 'user', 'content': prompt}
        ],
        'max_tokens': 16000,
        'temperature': 0.0,
        'return_citations': True,
    }, timeout=180)

    if resp.status_code != 200:
        print(f"  API Error {resp.status_code}: {resp.text[:200]}")
        return []

    data = resp.json()
    content = data['choices'][0]['message']['content']
    citations = data.get('citations', [])

    # Try to parse JSON from response
    urls = []

    # Method 1: Direct JSON parse
    try:
        parsed = json.loads(content)
        if isinstance(parsed, list):
            urls = parsed
    except json.JSONDecodeError:
        pass

    # Method 2: Find JSON array in text
    if not urls:
        match = re.search(r'\[[\s\S]*\]', content)
        if match:
            try:
                urls = json.loads(match.group())
            except json.JSONDecodeError:
                pass

    # Method 3: Extract URLs from citations + content with regex
    if not urls:
        all_urls = set()
        for c in citations:
            if isinstance(c, str) and c.startswith('http'):
                all_urls.add(c)
        url_pattern = re.findall(r'https?://[^\s\)"\'<>]+', content)
        all_urls.update(url_pattern)
        urls = [{'url': u, 'brief': 'extracted from citations'} for u in all_urls]

    # Add citation URLs as bonus
    citation_urls = set()
    for c in citations:
        if isinstance(c, str) and c.startswith('http'):
            citation_urls.add(c)

    existing_urls = {item.get('url', '') for item in urls if isinstance(item, dict)}
    for cu in citation_urls:
        if cu not in existing_urls:
            urls.append({'url': cu, 'brief': 'from perplexity citation'})

    # Filter: only keep items with valid URLs
    valid = []
    for item in urls:
        if isinstance(item, dict) and item.get('url', '').startswith('http'):
            valid.append(item)
        elif isinstance(item, str) and item.startswith('http'):
            valid.append({'url': item, 'brief': ''})

    return valid


# ══════════════════════════════════════════════
# Phase 2: Fetch full text from URLs
# ══════════════════════════════════════════════

def fetch_full_text(url: str, timeout: int = 30) -> dict:
    """Fetch full text content from a URL."""
    try:
        r = requests.get(url, headers=HEADERS_WEB, timeout=timeout, allow_redirects=True)
        if r.status_code != 200:
            return {'success': False, 'error': f'HTTP {r.status_code}', 'url': url}

        content_type = r.headers.get('Content-Type', '')
        if 'html' in content_type or 'text' in content_type:
            text = html_to_text(r.text)
            # Remove very short results (likely blocked/paywall)
            if len(text) < 200:
                return {'success': False, 'error': 'Content too short (likely paywall)', 'url': url, 'text': text}
            return {'success': True, 'text': text, 'url': url, 'chars': len(text)}
        elif 'json' in content_type:
            return {'success': True, 'text': json.dumps(r.json(), indent=2), 'url': url, 'chars': len(r.text)}
        else:
            return {'success': False, 'error': f'Unsupported content type: {content_type}', 'url': url}

    except requests.Timeout:
        return {'success': False, 'error': 'Timeout', 'url': url}
    except Exception as e:
        return {'success': False, 'error': str(e), 'url': url}


# ══════════════════════════════════════════════
# Main Pipeline
# ══════════════════════════════════════════════

def run_search_pipeline(ticker: str, company: str, ceo: str,
                        industry: str = '', competitors: str = '',
                        topics: list = None, skip_fetch: bool = False):
    """
    Full pipeline: Perplexity URL search → WebFetch full text → save .md files

    Args:
        ticker: Stock ticker
        company: Company name
        ceo: CEO name
        industry: Industry description (for prompt customization)
        competitors: Comma-separated competitor names
        topics: List of specific topics, or None for all
        skip_fetch: If True, only search URLs without fetching full text
    """
    print(f"\n{'='*70}")
    print(f"  Perplexity URL Discovery + Full-Text Pipeline")
    print(f"  {company} ({ticker}) | CEO: {ceo}")
    print(f"{'='*70}\n")

    all_prompts = get_url_search_prompts(ticker, company, ceo, industry, competitors)

    if topics:
        prompts = {k: v for k, v in all_prompts.items() if k in topics}
    else:
        prompts = all_prompts

    total_urls = 0
    total_fetched = 0
    total_chars = 0

    for i, (topic, prompt) in enumerate(prompts.items(), 1):
        print(f"\n[{i}/{len(prompts)}] ═══ {topic.upper()} ═══")

        # Phase 1: Get URLs from Perplexity
        print(f"  Phase 1: Searching URLs via Perplexity...")
        urls = query_perplexity_urls(prompt)
        print(f"  Found {len(urls)} URLs")
        total_urls += len(urls)

        if not urls:
            print(f"  ⚠ No URLs found for {topic}, skipping")
            continue

        # Create output directory
        output_dir = DB_DIR / ticker / 'sources' / topic
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save URL index
        index_path = output_dir / '_url_index.json'
        with open(index_path, 'w') as f:
            json.dump(urls, f, indent=2, ensure_ascii=False)
        print(f"  Saved URL index → {index_path.name}")

        if skip_fetch:
            print(f"  Skipping full-text fetch (--skip-fetch)")
            continue

        # Phase 2: Fetch full text for each URL
        print(f"  Phase 2: Fetching full text for {len(urls)} URLs...")
        fetched = 0
        failed = 0

        for j, item in enumerate(urls):
            url = item.get('url', '') if isinstance(item, dict) else str(item)
            if not url.startswith('http'):
                continue

            # Skip known paywall domains
            paywall_domains = ['bloomberg.com', 'wsj.com', 'ft.com', 'theinformation.com',
                               'stratechery.com', 'theathletic.com', 'nytimes.com']
            if any(d in url for d in paywall_domains):
                print(f"    [{j+1}/{len(urls)}] ⏭ Paywall: {url[:80]}")
                continue

            # Generate filename
            title = item.get('title', item.get('brief', ''))
            if not title:
                title = url.split('/')[-1][:50]
            safe_name = re.sub(r'[^a-zA-Z0-9\s-]', '', title)[:60].strip().replace(' ', '_').lower()
            if not safe_name:
                safe_name = f'item_{j+1}'

            # Check if already fetched
            existing = list(output_dir.glob(f'*{safe_name}*'))
            if existing:
                print(f"    [{j+1}/{len(urls)}] ⏭ Already exists: {safe_name}")
                fetched += 1
                continue

            # Fetch
            result = fetch_full_text(url)

            if result['success']:
                # Save as markdown
                date = item.get('date', datetime.now().strftime('%Y-%m-%d'))
                author = item.get('author', item.get('handle', ''))
                platform = item.get('platform', item.get('subreddit', topic))

                md = f"""---
ticker: {ticker}
type: {topic}
title: "{title}"
author: "{author}"
date: {date}
url: {url}
chars: {result['chars']}
fetched: {datetime.now().strftime('%Y-%m-%d %H:%M')}
---

# {title}

**Source**: {url}
**Author**: {author}
**Date**: {date}

---

{result['text']}
"""
                filepath = output_dir / f'{safe_name}.md'
                filepath.write_text(md, encoding='utf-8')
                print(f"    [{j+1}/{len(urls)}] ✅ {result['chars']:,} chars → {filepath.name}")
                fetched += 1
                total_chars += result['chars']
            else:
                print(f"    [{j+1}/{len(urls)}] ❌ {result['error'][:60]} — {url[:60]}")
                failed += 1

            # Rate limit
            time.sleep(0.5)

        total_fetched += fetched
        print(f"  Summary: {fetched} fetched, {failed} failed out of {len(urls)} URLs")

    # ── Final Summary ──
    print(f"\n{'='*70}")
    print(f"  PIPELINE COMPLETE")
    print(f"  URLs found:    {total_urls}")
    print(f"  Pages fetched: {total_fetched}")
    print(f"  Total chars:   {total_chars:,}")
    print(f"  Output dir:    discovery_database/{ticker}/sources/")
    print(f"{'='*70}\n")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python fetch_perplexity.py TICKER CompanyName CEOName [topic1,topic2,...] [--skip-fetch]")
        print("\nExample:")
        print("  python fetch_perplexity.py APP AppLovin 'Adam Foroughi'")
        print("  python fetch_perplexity.py APP AppLovin 'Adam Foroughi' twitter,reddit")
        print("  python fetch_perplexity.py APP AppLovin 'Adam Foroughi' --skip-fetch")
        print("\nAvailable topics:")
        for t in get_url_search_prompts('X', 'X', 'X').keys():
            print(f"  - {t}")
        sys.exit(1)

    ticker = sys.argv[1]
    company = sys.argv[2] if len(sys.argv) > 2 else ticker
    ceo = sys.argv[3] if len(sys.argv) > 3 else 'the CEO'

    topics = None
    skip_fetch = False
    for arg in sys.argv[4:]:
        if arg == '--skip-fetch':
            skip_fetch = True
        elif ',' in arg or arg in get_url_search_prompts('X', 'X', 'X'):
            topics = arg.split(',')

    run_search_pipeline(ticker, company, ceo, topics=topics, skip_fetch=skip_fetch)
