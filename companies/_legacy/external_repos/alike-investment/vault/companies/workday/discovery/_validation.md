---
type: collect_validation
ticker: WDAY
status: FAIL
generated: 2026-04-09
---

# WDAY (Workday) — 采集校验
- 状态: **FAIL**
<<<<<<< HEAD
- 总耗时: 524.6秒
- 本轮新增文件: 50
=======
- 总耗时: 500.6秒
- 本轮新增文件: 49
>>>>>>> origin/servicenow-collect
- SEC应有预期: yes
- 中国公司相关: no

## 检查结果
- [PASS] `profile_exists`: profile.md exists
- [PASS] `financials_exists`: financials.md exists
- [FAIL] `xbrl_output`: financials_detailed.md missing
- 建议: 若为美股，检查 SEC CIK 映射与 XBRL 拉取。
- [PASS] `sec_filings_count`: earnings filings: 9
<<<<<<< HEAD
- [WARN] `youtube_count`: youtube transcripts: 0
- 建议: 检查 yt-dlp、YouTube 搜索词和字幕可用性。
- [PASS] `podcast_count`: podcast files: 9
- [PASS] `xiaoyuzhou_applicability`: 非中国相关公司，小宇宙为 0 不视为问题。
- [PASS] `report_freshness`: _collection_report.md fresh
- [PASS] `new_files_this_run`: files touched this run: 50
=======
- [PASS] `youtube_count`: youtube transcripts: 2
- [PASS] `podcast_count`: podcast files: 9
- [PASS] `xiaoyuzhou_applicability`: 非中国相关公司，小宇宙为 0 不视为问题。
- [PASS] `report_freshness`: _collection_report.md fresh
- [PASS] `new_files_this_run`: files touched this run: 49
>>>>>>> origin/servicenow-collect
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
<<<<<<< HEAD
- organization/_org_brief.md
- organization/_org_scan_report.md
- organization/_org_scan_request.md
=======
- organization/_org_scan_report.md
>>>>>>> origin/servicenow-collect
- organization/c_suite/aneel_bhusri.md
- organization/c_suite/david_albert_duffield.md
- organization/c_suite/justin_allen_furby.md
- organization/c_suite/mark_s_garfield.md
- organization/c_suite/mr_aneel_bhusri.md
- organization/c_suite/mr_david_albert_duffield.md
- organization/c_suite/mr_justin_allen_furby.md
- organization/c_suite/mr_mark_s_garfield.md
- organization/c_suite/mr_richard_harry_sauer_jd.md
- organization/c_suite/mr_robert_enslin.md
- organization/c_suite/mr_zane_c_rowe.md
- organization/c_suite/ms_ashley_d_goldsmith.md
- organization/c_suite/ms_emma_chalwin.md
<<<<<<< HEAD
- organization/c_suite/ms_rani_johnson.md
=======
- organization/c_suite/ms_rani_johnson.md
- organization/c_suite/rani_johnson.md
- organization/c_suite/richard_harry_sauer_jd.md
>>>>>>> origin/servicenow-collect
