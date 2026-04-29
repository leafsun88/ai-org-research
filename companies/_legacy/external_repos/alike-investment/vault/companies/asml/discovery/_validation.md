---
type: collect_validation
ticker: ASML
status: WARN
generated: 2026-04-08
---

# ASML (ASML) — 采集校验
- 状态: **WARN**
- 总耗时: 0.0秒
- 本轮新增文件: 1
- SEC应有预期: no
- 中国公司相关: no

## 检查结果
- [PASS] `profile_exists`: profile.md exists
- [PASS] `financials_exists`: financials.md exists
- [PASS] `xbrl_output`: financials_detailed.md exists
- [WARN] `sec_filings_count`: earnings filings: 0
- 建议: 若为美股，检查 SEC filings 是否成功下载。
- [PASS] `youtube_count`: youtube transcripts: 1
- [PASS] `podcast_count`: podcast files: 28
- [PASS] `xiaoyuzhou_applicability`: 非中国相关公司，小宇宙为 0 不视为问题。
- [WARN] `report_freshness`: _collection_report.md stale
- 建议: 若报告未更新，优先查看 _validation.json / _summary.json 和实际产物。
- [PASS] `new_files_this_run`: files touched this run: 1
- [PASS] `summary_generated`: _summary.json generated
- [PASS] `org_foundation_present`: org workspace scaffolded
- [PASS] `founder_voice_ready`: founder_voice ready
- [PASS] `org_scan_ready`: org_scan_report=ready, org_structure=ready
- [PASS] `org_dataset_minimum`: minimum org dataset for D1-D7
- [WARN] `org_dataset_high_quality`: high-quality org dataset
- 建议: 当前若仍是 auto_basic 版本，建议继续运行 `/founder` 和 `/org-scan` 做深挖。
- [PASS] `governance_summary_ready`: governance_summary ready
- [WARN] `proxy_filing_present`: proxy filings: 0
- 建议: 若美股 proxy 仍为空，检查 DEF 14A 抓取是否成功。

## 本轮新增文件（前20）
- _summary.json