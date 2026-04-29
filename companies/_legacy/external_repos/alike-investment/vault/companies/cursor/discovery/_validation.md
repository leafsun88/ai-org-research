---
type: collect_validation
ticker: CURSOR
status: FAIL
generated: 2026-04-08
---

# CURSOR (Cursor) — 采集校验
- 状态: **FAIL**
- 总耗时: 741.2秒
- 本轮新增文件: 8
- SEC应有预期: yes
- 中国公司相关: no

## 检查结果
- [PASS] `profile_exists`: profile.md exists
- [FAIL] `financials_exists`: financials.md missing
- 建议: 检查 financials 模块是否成功写入 financials.md。
- [FAIL] `xbrl_output`: financials_detailed.md missing
- 建议: 若为美股，检查 SEC CIK 映射与 XBRL 拉取。
- [FAIL] `sec_filings_count`: earnings filings: 0
- 建议: 若为美股，检查 SEC filings 是否成功下载。
- [PASS] `youtube_count`: youtube transcripts: 14
- [PASS] `podcast_count`: podcast files: 15
- [PASS] `xiaoyuzhou_applicability`: 非中国相关公司，小宇宙为 0 不视为问题。
- [PASS] `report_freshness`: _collection_report.md fresh
- [PASS] `new_files_this_run`: files touched this run: 8
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
- _collection_report.md
- organization/_org_brief.md
- organization/_org_scan_report.md
- organization/_org_scan_request.md
- organization/governance_summary.md
- organization/overview/org_structure.md
- sources/founder/httpsstratecherycom2025an_interview_with_cursor_co_founder_a.md
- sources/founder_voice.md