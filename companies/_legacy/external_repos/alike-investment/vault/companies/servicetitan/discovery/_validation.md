---
type: collect_validation
ticker: TTAN
status: FAIL
generated: 2026-04-09
---

# TTAN (ServiceTitan) — 采集校验
- 状态: **FAIL**
- 总耗时: 549.3秒
- 本轮新增文件: 61
- SEC应有预期: yes
- 中国公司相关: no

## 检查结果
- [PASS] `profile_exists`: profile.md exists
- [PASS] `financials_exists`: financials.md exists
- [FAIL] `xbrl_output`: financials_detailed.md missing
- 建议: 若为美股，检查 SEC CIK 映射与 XBRL 拉取。
- [PASS] `sec_filings_count`: earnings filings: 7
- [WARN] `youtube_count`: youtube transcripts: 0
- 建议: 检查 yt-dlp、YouTube 搜索词和字幕可用性。
- [PASS] `podcast_count`: podcast files: 22
- [PASS] `xiaoyuzhou_applicability`: 非中国相关公司，小宇宙为 0 不视为问题。
- [PASS] `report_freshness`: _collection_report.md fresh
- [PASS] `new_files_this_run`: files touched this run: 61
- [PASS] `summary_generated`: _summary.json generated
- [PASS] `org_foundation_present`: org workspace scaffolded
- [PASS] `founder_voice_ready`: founder_voice ready
- [PASS] `org_scan_ready`: org_scan_report=ready, org_structure=ready
- [PASS] `org_dataset_minimum`: minimum org dataset for D1-D7
- [WARN] `org_dataset_high_quality`: high-quality org dataset
- 建议: 当前若仍是 auto_basic 版本，建议继续运行 `/founder` 和 `/org-scan` 做深挖。
- [PASS] `governance_summary_ready`: governance_summary ready
- [PASS] `proxy_filing_present`: proxy filings: 1

## 本轮新增文件（前20）
- _collection_report.md
- _podcast_episodes.json
- financials.md
- organization/_org_scan_report.md
- organization/c_suite/abhishek_mathur.md
- organization/c_suite/ara_mahdessian.md
- organization/c_suite/chris_petros.md
- organization/c_suite/dave_sherry.md
- organization/c_suite/jason_rechel.md
- organization/c_suite/michele_oconnor.md
- organization/c_suite/mr_abhishek_mathur.md
- organization/c_suite/mr_ara_mahdessian.md
- organization/c_suite/mr_chris_trombetta.md
- organization/c_suite/mr_dave_sherry.md
- organization/c_suite/mr_jason_rechel.md
- organization/c_suite/mr_rikus_pretorius.md
- organization/c_suite/mr_vahe_kuzoyan.md
- organization/c_suite/ms_michele_oconnor.md
- organization/c_suite/ms_olive_huang.md
- organization/c_suite/olive_huang.md