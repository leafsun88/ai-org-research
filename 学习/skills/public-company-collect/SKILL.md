---
name: public-company-collect
description: Collect public-company filings, statements, market data, capital-market signals, earnings calls, books, and semi-public research scaffolding for A-share, US, and Hong Kong listed companies.
---

# Public Company Collect

Use this skill when the user asks to collect上市公司资料, filings, annual reports, earnings calls, prospectus, market data, valuation, holders, investor views, or semi-public material for a public company.

## Workflow

1. Resolve the company through `config/company_targets.json`.
   - Required fields: `ticker`, `slug`, `company_name`, `is_public`, `output_paths`.
   - Preferred `public_company` fields: `market`, `exchange`, `cik`, `ir_url`, `peer_tickers`.
2. Run source/skill discovery before scraping any data or text.
   - Search local skills first: `学习/skills/**/SKILL.md` and `~/.codex/skills/**/SKILL.md`.
   - Check external skill directories such as SkillsMP, OpenAI `openai/skills`, `theskills.directory`, and `skills.sh` for reusable extraction patterns.
   - Check official/public guide pages for the requested market and data category before writing a new scraper.
   - Write `metadata/source_strategy.json` and `.md` with chosen sources, known caveats, and rejected/blocked source options.
3. Create the vault:
   - `companies/{slug}/vault/public_company/raw_filings/`
   - `processed/`
   - `data/`
   - `semi_public/`
   - `models/{YYYY-MM-DD}/`
   - `metadata/`
4. Run:

```bash
python3 scripts/discovery/collect_public_company.py SNDK --max-filings 3 --quality-loop --json
```

5. For US companies, prefer SEC official sources:
   - filings: `submissions/CIK##########.json`
   - statements: `companyfacts/CIK##########.json`
   - raw reports: 10-K, 10-Q, ARS/annual report to security holders, S-1/F-1/424B, DEF 14A, 8-K, Forms 3/4/5.
6. For Hong Kong companies, use the HKEX adapter and yfinance `.HK`; if extraction fails, write an explicit gap.
7. For A-shares, use CNInfo / AKShare first; Tushare is optional and must not block a free-first pass.
8. Save full annual and quarterly reports as raw source artifacts. For annual reports, always attempt a native PDF in addition to SEC HTML/JSON: IR `Download PDF`, SEC `ARS`/shareholder-report PDF, or other official annual-report PDF. If no native PDF exists, write an explicit gap and only then create a rendered PDF fallback labeled `native_pdf_unavailable_rendered_from_html`. Extract MD&A / management discussion separately into `processed/mda/`.
9. Earnings-call handling:
   - IR pages are canonical for events, webcasts, presentations, and press releases.
   - If IR does not publish transcript text, mark that and store third-party transcripts as fallback only.
10. Semi-public handling:
   - Reuse the existing `collect` channel map: podcasts, youtube, substack, official, jobs_org, founder_voice, web_longform, social_community.
   - Save only real URLs, original artifacts, transcripts, or explicit failure reasons.
   - Do not label AI summaries as original source text.
11. Books and investor views:
   - Write `processed/books/company_books.json` and `.md`.
   - Preserve `raw_candidates` even when no high-confidence book is accepted.
   - Write `semi_public/investor_views/investor_views_index.json` and `.md`.
   - Distinguish filings, public fund letters, interviews, Substack/blog posts, social discussion, and short-seller reports.
12. The collector calls `financial-modeling` at the end unless `--skip-model` is passed.

## Source/Skill Discovery Gate

The first act of any scraping task is to ask: "Has someone already documented or packaged this extraction?"

Use this order:

1. Local skills and legacy project skills.
2. Public skill markets/directories, especially SkillsMP (`https://skillsmp.com/zh`) and OpenAI `openai/skills`.
3. Official API/docs/source-guide pages for the market.
4. Open-source scripts, public skills, or well-maintained extraction libraries.
5. General web search or ad hoc scraping only after the above is recorded.

For every source category, record:

- chosen source URL or local skill path;
- why it is trusted enough for this field;
- whether it is official, public fallback, third-party, paid, or blocked;
- extraction caveats such as rate limits, YTD-vs-quarter facts, PDF table reliability, or missing transcript access.

If an API is unstable, try alternate free interfaces before blocking:

1. Retry the same official/public endpoint with conservative timeouts.
2. Try a different transport or endpoint variant, such as `curl --http1.1` for APIs that fail under Python TLS.
3. Try a second free source for the same field, with source type clearly labeled.
4. Use cached raw payloads only when the cache source and timestamp are recorded.
5. Ask the user for a paid API key only after several free/official/third-party options fail or the remaining gap requires paid coverage.

Do not proceed to raw scraping without `metadata/source_strategy.json` unless the user explicitly asks for a quick one-off lookup.

## Quality Gate

Never treat collection as complete just because files exist. After the run, write and read `metadata/data_quality_audit.json`.

## Manual Content Review Gate

Automated file counts are not enough. Before saying a collection is complete, open the actual artifacts and use judgment. A JSON wrapper, metadata file, query map, probe stub, or tiny status note is not evidence that the underlying source was collected.

Write both:

- `metadata/manual_content_audit_{YYYY-MM-DD}.json`
- `metadata/manual_content_audit_{YYYY-MM-DD}.md`

For every important category, record `path`, `opened_by`, `content_type`, `substantive_content`, `identity_hits`, `red_flags`, `repair_action`, and `status`.

Required human-read checks:

- Raw annual/quarterly/prospectus filings: open the document, read the cover/title area, section headings, at least one table, and one narrative paragraph. Confirm company name/ticker/period/form match the target. For annual reports, a 10-K HTML file alone is not enough when a native PDF exists; confirm that `raw_filings/annual_reports/` contains at least one substantive `.pdf` and that its extracted text matches the company.
- MD&A extracts: read the first substantial paragraph and at least one operating-results paragraph. Confirm it is management discussion, not a generic filing shell.
- Earnings-call presentations: run `pdfinfo`/`pdftotext` or visually open pages; read the title page and several slide headings. Confirm company, fiscal quarter, end markets, and management terms match. If a PDF contains unrelated concepts such as a different industry, quarantine it and refetch from IR/static-file links.
- Earnings-call transcripts: read the opening, management remarks, and Q&A speaker names. A page saying "AI Summary" is not enough unless full transcript text follows.
- Statement JSON/CSV: inspect real rows, not only schema. Look for null-heavy periods, wrong YTD-vs-quarter facts, missing source trace, and values that contradict the filing tables. Each key metric must have either row-level source fields or a usable `source_map`.
- Market data/valuation: inspect first and last price rows, latest quote timestamp, market cap source, share count source, and whether a fallback page/API confirms the quote. If a quote API is unstable, try another free source before accepting stale values.
- Capital signals: read representative Form 4/13G/holder rows and confirm issuer CIK/name. Holder totals without source URL or filing trail are only leads.
- Books/investor views/semi-public: distinguish original source material from search scaffolding. Query maps and raw candidates are not collected source content; they pass only as explicit `scaffold_only` warnings or blockers.

If a file is wrong-company, mostly boilerplate, too small to contain the promised source, only metadata, or has no source trail, mark it `needs_repair`. Do not hide this behind a passing automated audit.

When manual review finds a problem, try repair channels in this order:

1. Re-open official source pages with a longer timeout.
2. Retry through a different transport, especially `curl --http1.1`, when Python TLS/requests is unstable.
3. Use official APIs/raw archives: SEC submissions/companyfacts/archive HTML/XBRL for US, HKEXnews for HK, CNInfo/SSE/SZSE disclosure pages for A-shares.
4. Use trusted free fallbacks for the same field: IR static-file links, StockAnalysis transcript/statistics pages, Nasdaq holder API with curl fallback, Holdings Channel/13F aggregation, Yahoo chart JSON, Stooq/other quote sources, AKShare/Eastmoney for A-shares.
5. If several free/official/third-party routes fail or the source is paywalled, ask the user for a paid API key instead of fabricating completeness.

The SNDK pilot had a concrete example: PDF filenames claimed to be Sandisk earnings presentations, but reading the extracted PDF text showed unrelated education-company content. That kind of mismatch must fail the manual content review and trigger refetch from verified IR URLs.

Collection must be `needs_review` when any of these are true:

- quarterly statements do not include revenue plus operating income or net income;
- annual or quarterly statement JSON does not use the canonical `periods` array schema;
- annual report PDF is missing while the issuer/SEC provides a native annual-report PDF such as IR `Download PDF` or SEC `ARS`;
- annual report PDF exists but content-identity review fails or the PDF is only a metadata/download shell;
- annual statements are missing assets, liabilities, debt, cash, equity, shares, revenue, income, cash flow, or capex;
- annual processed statements preserve fewer income-statement years than are available in SEC companyfacts / the raw annual report;
- annual or quarterly statement files have low field density, such as rows that exist but most required financial fields are blank;
- price history has fewer than 60 daily rows, valuation snapshot lacks key quote/share-count/EV fields, or institutional holders have fewer than 10 usable rows;
- current market cap is computed from weighted-average diluted shares instead of a quote/share-count source;
- peer comps have prices but no PE/PS/EV/EBITDA multiples;
- earnings-call transcript text is missing and only presentations/webcasts are present;
- investor views have neither fetched original sources nor a query/index file for follow-up source collection;
- books search has no retained books, raw candidates, or query log.
- `manual_content_audit` is missing, or it marks any core artifact as wrong-company, metadata-only, scaffold-only without warning, or `needs_repair`;
- MD&A, earnings presentations, or transcripts fail content-identity checks after reading representative text;
- statement JSON has values but no usable row source or `source_map` trail for key metrics.

For first-pass semi-public collection, a complete folder/query scaffold is allowed to pass with a warning. Original semi-public URLs/transcripts are still preferred and should be fetched when collect/webfetch credentials are available.

SEC `companyfacts` is a fact source, not a complete statement parser or original report archive. For US companies, do not collapse all facts by `fy/fp`: a 10-K often contains multiple historical annual periods with the same filing `fy`. Preserve annual periods by actual statement end year and preserve quarterly periods by true quarter duration, not YTD facts. If `companyfacts` leaves quarterly income statement, historical annual periods, or balance-sheet fields sparse, mark the gap and either parse statement tables from the raw 10-K/10-Q HTML/PDF or defer that as an explicit follow-up. Do not silently model from partial facts. `data/statements/*.json` and `.csv` are normalized data products; they do not replace the raw annual-report PDF/HTML in `raw_filings/annual_reports/`.

## Quality Loop

Use the bounded quality loop by default:

```bash
python3 scripts/discovery/collect_public_company.py SNDK --quality-loop --max-quality-iterations 3 --json
```

Loop behavior:

1. Build or refresh collection artifacts.
2. Build the financial model.
3. Run `metadata/data_quality_audit.json`.
4. If audit status is `pass`, stop.
5. If gaps are repairable, run the mapped repair action and then rerun model + audit:
   - source strategy missing/stale -> rerun source/skill discovery;
   - raw annual report, annual PDF, annual PDF identity, raw quarterly report, or raw prospectus gaps -> rerun SEC/HKEX/CNInfo filing collection and prefer official PDF/HTML source artifacts;
   - annual/quarterly statement schema, gap, or density failures -> rerun statement extraction/parser;
   - statement source-trace or manual row review failures -> parse raw filing tables or use alternate market API/source before modeling;
   - MD&A gap -> rerun MD&A extraction;
   - MD&A content-identity failure -> re-open the filing and extract the correct item by section boundaries;
   - earnings transcript gap -> rerun IR page scan and approved third-party transcript fallback fetch, with source URL preserved;
   - earnings presentation/transcript content-identity failure -> quarantine wrong artifacts, rerun IR/static-file discovery, then retry with `curl --http1.1` or another approved source;
   - market cap, price-history, valuation-density, or peer-multiple gaps -> rerun market-data/valuation fetchers;
   - institutional holder gaps or holder-density failures -> try Nasdaq API, curl/http1 Nasdaq fallback, then Holdings Channel 13F aggregate before asking for paid data;
   - books gap -> rerun books search and retain raw candidates/query log.
6. Repeat until all checks pass or the loop reaches a hard blocker.

Hard blockers include unavailable semi-public original sources, missing paid/credentialed holder data, investor-view sources that require webfetch/agent collection, or earnings transcripts unavailable from both IR and approved third-party fallback sources. When blocked, write `metadata/quality_loop_status.json` and `.md` with remaining gaps and blocker notes. Never report "complete" when the quality loop is `blocked`.

## Verification

Run:

```bash
python3 -m unittest scripts.discovery.test_public_company_collection
python3 -m py_compile scripts/discovery/collect_public_company.py scripts/discovery/public_company/*.py
```

Then inspect:

- `metadata/collection_status.json`
- `metadata/api_probe_status.json`
- `metadata/data_quality_audit.json`
- `metadata/probes/*.json`
- `models/{date}/model_validation.json`

Do not claim completion if the workbook is missing, required sheets are absent, `model_validation.json` has fatal errors, or `collection_status.json` is `needs_review` without explaining the gaps.
