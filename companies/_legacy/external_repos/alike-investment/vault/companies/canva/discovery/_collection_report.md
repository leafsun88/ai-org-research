---
credibility: S3
evidence: E2
collected: 2026-04-07
---

# Canva -- Discovery Collection Report
**Collected**: 2026-04-07
**Status**: Private company (non-listed)
**Slug**: canva

## Collection Summary

| Module | Status | Details |
|--------|--------|---------|
| financials | Skipped | Private company, no yfinance data |
| xbrl | Skipped | Not SEC-filing |
| full_dump | Skipped | Private company |
| fmp_enhanced | Skipped | Private company |
| sec_filings | Skipped | Private company |
| youtube | SUCCESS | 16/19 videos with transcripts, 401K chars |
| podcasts | FAILED | Missing requests module |
| xiaoyuzhou | FAILED | Missing requests module |
| perplexity | FAILED | Most URLs returned 403 (Canva.com blocks scraping) |
| social-search (Twitter/CEO) | SUCCESS | Melanie Perkins + Cliff Obrecht activity mapped |
| social-search (Substack) | SUCCESS | 6 substantive articles fetched & summarized |
| social-search (Reddit) | LIMITED | No direct Reddit results found |
| social-search (Glassdoor) | SUCCESS | 826 reviews analyzed |
| founder search | SUCCESS | Perkins + Obrecht + Adams profiles |
| deep search (5 dims) | SUCCESS | News, valuation, competitive, AI, acquisitions |
| org scan | SUCCESS | C-suite mapped, key hires identified |
| signals scan | SUCCESS | 12 signals categorized (HIGH/MED/LOW) |

## File Inventory

### sources/youtube/ (18 files, ~476KB)
Key transcripts:
- Canva Deep Dive (Sandy Kory, HorizonVC)
- She turned 100+ rejections into $42B company (Melanie Perkins)
- CFO Explains Canva's $42B Valuation but ZERO Profit
- A Canva Deep Dive (partner analysis)
- Canva IPO: Public Market Insights
- Canva: She founded a unicorn by 30

### sources/social/ (3 files)
- twitter_ceo_2026-04-07.md -- CEO/COO public activity
- substack_analysis_2026-04-07.md -- 6 Substack articles
- glassdoor_employee_2026-04-07.md -- employee sentiment

### sources/ (4 files)
- founder_2026-04-07.md -- Perkins + Obrecht + Adams profiles
- deep_search_2026-04-07.md -- 5-dimension deep search
- org_scan_2026-04-07.md -- executive team scan
- signals_2026-04-07.md -- signal categorization

## Total: 28 files, ~560KB

## Key Data Points Collected

### Financial
- $4B ARR (2025), 35-40% YoY growth
- $42B valuation (Aug 2025 secondary)
- 7 years consecutive profitability
- Revenue per employee: $500K
- ~4,000 employees

### Users
- 265M monthly active users
- 31M paid seats
- 95% Fortune 500 penetration
- 135K+ paying businesses

### Organization
- 3 co-founders still in C-suite (Perkins/Obrecht/Adams)
- CFO hire Nov 2024 (Kelly Steckelberg, ex-Zoom) = IPO prep
- Chief Algorithms Officer created 2026 (Nirmal Govind, ex-Netflix)
- 300 dedicated AI employees

### Competitive
- 10% of $15B creative software market (Adobe = 70%)
- Canva Pro $120/yr vs Adobe CC $660/yr
- Magic Studio used 24B+ times
- 11 acquisitions total, 4 major in 18 months

## Gaps / Missing Data
1. No financial statements (private company -- no public filings)
2. Podcast data collection failed (requests module issue)
3. No direct Reddit discussions captured
4. Perplexity pipeline failed (403 errors from Canva.com)
5. 3 YouTube videos had no transcripts (2 CEO interviews)
6. Limited insider trading data (not public)
7. No detailed board composition data

## Recommended Next Steps
1. **L2 Alike Score**: Sufficient data for D1-D7 scoring (strong on D1 CEO, D2 Key Leaders, D7 Key Bets)
2. **Podcast transcripts**: Manually add key CEO interviews (20VC Cliff Obrecht, Masters of Scale)
3. **IPO watch**: Monitor H2 2026 IPO timeline
4. **Competitive tracking**: Adobe + Figma quarterly results as benchmarks
