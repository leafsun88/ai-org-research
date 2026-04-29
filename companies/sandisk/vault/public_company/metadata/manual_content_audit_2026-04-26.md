# Sandisk Manual Content Audit

- Date: 2026-04-26
- Reviewer: Codex
- Scope: public_company vault core artifacts
- Status: pass_with_warnings

## Findings

| Category | Status | Human-read check | Notes |
|---|---|---|---|
| Annual report | repaired_pass | Opened 2025 10-K HTML and SEC ARS PDF; checked title/CIK, Item 7 MD&A, statement table language, and PDF cover text. | Substantive Sandisk filing. Initial pass missed the native annual-report PDF because SEC 10-K HTML existed; repaired by downloading SEC ARS PDF. |
| Quarterly reports | pass | Opened 10-Q HTML samples and checked Sandisk/CIK, condensed statements, periods. | Substantive filings. |
| Prospectus | pass | Opened 424B files; checked Sandisk title, risk factors, separation/distribution discussion. | Substantive prospectus content. |
| MD&A extract | pass | Read first substantial MD&A paragraphs and operating-results section. | Real MD&A, not metadata. |
| Earnings presentations | repaired_pass | Ran `pdftotext` on all four PDFs and read title/first pages plus keyword hits. | Prior q4cdn PDFs were wrong-company education content; replaced with verified Sandisk IR static-file PDFs. |
| Earnings transcripts | pass_warning | Read openings, management remarks, and Q&A speaker names for StockAnalysis transcript fallbacks. | Full transcript text exists, but source is third-party because IR transcript text was not found. |
| Statements JSON/CSV | pass_warning | Inspected annual/quarterly rows and `source_map`. | Key income/cash-flow rows present; older balance-sheet fields have nulls where filings/companyfacts do not provide full history. Keep explicit source-map trail. |
| Market data / valuation | pass_warning | Checked first/last price rows, StockAnalysis statistics page data, Yahoo instability. | Yahoo chart endpoint returned HTTP 429 during spot check; StockAnalysis fallback confirms current quote/market cap fields. |
| Capital signals | pass | Read sample Form 4, 13G, Nasdaq holder rows. | Issuer name/CUSIP/source URLs present. |
| Books | pass_warning | Read book JSON candidates and query log. | No accepted company/founder book; retained raw candidates/query log. |
| Investor views | warning | Read index/query map. | Only holder counts and query leads; no original investor letters/interviews fetched yet. |
| Semi-public folders | warning | Read `_collection_status.json` files. | Scaffold/query maps only; not source content. Needs collect/webfetch pass when requested. |

## Repairs Made

- Replaced incorrect earnings presentation PDFs:
  - `Q1-FY2026-Earnings-Presentation.pdf`
  - `Q2-FY2026-Earnings-Presentation.pdf`
  - `Q3-FY2025-Earnings-Presentation.pdf`
  - `Q4-FY2025-Earnings-Presentation.pdf`
- Updated `config/company_targets.json` SNDK presentation seed URLs from wrong q4cdn links to verified `investor.sandisk.com/static-files/...` links.
- Updated `earnings_call_metadata.json` and `earnings_calls_index.md` to point to the verified IR static-file URLs.
- Added content-identity checks to the collector/audit so wrong-company PDFs fail instead of passing by file existence.
- Added `2025-10-07_ARS_0001628280-25-044483_sndk014126-arsa.pdf` to `raw_filings/annual_reports/` and changed the collector/audit so SEC `ARS` filings count as annual reports and annual-report PDF absence fails the audit.

## Remaining Warnings

- Semi-public channels are mostly scaffolds, not fetched original sources.
- Investor views still need original fund letters/interviews/13F narrative sources beyond holder tables.
- Statements should continue to preserve explicit gaps for fields unavailable in source filings/companyfacts, rather than silently filling.
