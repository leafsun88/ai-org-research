---
company: Zomato
ticker: ZOMATO.NS
date: "2026-04-07"
type: collection-report
pipeline_version: "full-collect"
---

# Zomato (ZOMATO.NS) — Full Collection Report

**Date**: 2026-04-07
**Pipeline**: /collect full execution (Steps 1-5)
**Total Files**: 29 (in discovery/)
**Total Size**: ~148KB

---

## Step 1: collect.py Script Results

### Successful Modules
| Module | Result | Details |
|--------|--------|---------|
| podcasts | 8 episodes | 3 Chinese, 5 English — metadata only, no transcripts |
| xiaoyuzhou | 0 episodes | API unavailable |
| youtube | 0 videos | yt-dlp not installed |

### Failed Modules (Expected for Non-US Stock)
| Module | Error | Reason |
|--------|-------|--------|
| financials | TLS connect error | yfinance SSL issue for ZOMATO.NS |
| xbrl | No XBRL data | Not SEC-filed (Indian stock) |
| full_dump | index out of bounds | No yfinance data available |
| fmp_enhanced | Module not found | Missing dependency |
| sec_filings | Type error | No CIK for ZOMATO.NS |

**Note**: Zomato is listed on NSE/BSE India, not US exchanges. SEC/XBRL/yfinance modules are not applicable.

## Step 1.5: Perplexity Deep Research

| Dimension | URLs Found | Fetched | Notes |
|-----------|-----------|---------|-------|
| Twitter | 4 | 1 (extracted_from_citations.md) | 3 duplicates skipped |
| Reddit | 2 | 0 | Connection errors (Indian news sites) |
| Substack | 10 | 0 | All paywalled |
| Podcast Transcripts | 8 | 0 | YouTube/Spotify unfetchable |
| News Investigations | 7 | 1 (extracted_from_citations.md) | 3 connection errors, 3 duplicates |

**Total**: 31 URLs discovered, 8 pages fetched, 13,431 chars extracted

## Step 2: Social Media Search (WebSearch)

| Platform | File | Key Findings |
|----------|------|-------------|
| Twitter/X | social/twitter_x.md | Stock at INR 236.50, Blinkit $13B valuation, HDFC Buy INR 340 target |
| Reddit | social/reddit_discussions.md | P/E 988x concern, Blinkit 46% market share, acquisition ROI debate |
| Substack | social/substack_analysis.md | Damodaran analysis, betatoalpha Blinkit thesis, 10+ authors covering |

## Step 2.5: Founder/CEO Research

| Person | Key Findings |
|--------|-------------|
| Deepinder Goyal | Stepped down Feb 1 2026, pursuing Temple ($54M brain tech) + Continue Research ($25M longevity) |
| Albinder Dhindsa | New CEO, IIT Delhi + Columbia MBA, execution-first style, 3,000 dark stores by FY27 |
| Insider Trading | No allegations found, Goyal holds 3.83% stake |

## Step 3: Deep Search (5 Dimensions)

| Dimension | Key Findings |
|-----------|-------------|
| Latest News 2026 | Platform fee hike, OpenAI partnership, ESOP grants, Q3 revenue +190% YoY |
| Analyst Views | Unanimous Buy: HDFC 340, JM Financial 400, Motilal 260-300 |
| Competitive | Zomato 55-58% food delivery, Blinkit 40-46% quick commerce |
| Controversies | Hygiene raids, Delhi pollution delays, consumer trust erosion |
| New CEO | Execution-focused pivot, data-driven, logistics optimization priority |

## Step 4: YouTube Transcripts

- yt-dlp not installed — 0 transcripts extracted automatically
- 3 key video URLs identified via Perplexity for manual extraction
- Key videos: Raj Shamani podcast with Deepinder Goyal, stock analysis channels

## Data Quality Assessment

### Strong Coverage
- CEO/leadership transition (high-quality, recent data)
- Competitive landscape (Zomato vs Swiggy vs Zepto)
- Quick commerce strategy and dark store expansion
- Analyst consensus and price targets

### Gaps to Fill
- **Financials**: Need Indian financial data source (BSE/NSE filings, not SEC)
- **YouTube Transcripts**: Need yt-dlp installation or manual extraction
- **Employee Sentiment**: No Glassdoor/employee review data
- **Insider Transactions**: Need BSE/NSE insider trading data (not SEC)
- **Earnings Call Transcripts**: Need BSE annual reports / concall transcripts

### Recommended Next Steps
1. Install yt-dlp for YouTube transcript extraction
2. Source BSE/NSE financial data (replacing SEC/XBRL for Indian stocks)
3. Run `/alike ZOMATO.NS` for L2 scoring
4. Deep dive on organizational transition (Goyal to Dhindsa) for org-inflection analysis

## File Inventory

### discovery/ (29 files)
```
_collection_report.md
_podcast_episodes.json
financials.md (from previous lite collect)
profile.md (from previous lite collect)
sources/
  deep_search_2026-04-07.md
  founder_2026-04-07.md
  guru_2026-04-07.md
  org_scan_2026-04-07.md
  signals_2026-04-07.md
  social_search_2026-04-07.md
  perplexity/
    twitter/_url_index.json
    twitter/extracted_from_citations.md
    reddit/_url_index.json
    substack_analysis/_url_index.json
    podcasts_transcripts/_url_index.json
    news_investigations/_url_index.json
    news_investigations/extracted_from_citations.md
  podcasts/ (8 episode metadata files)
  social/
    twitter_x.md
    reddit_discussions.md
    substack_analysis.md
  youtube/
    youtube_search_2026-04-07.md
```
