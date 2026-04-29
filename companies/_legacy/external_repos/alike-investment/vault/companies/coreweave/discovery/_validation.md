---
type: collect_validation
ticker: CRWV
status: FAIL
generated: 2026-04-08
---

# CRWV (CoreWeave) — 采集校验
- 状态: **FAIL**
- 总耗时: 631.3秒
- 本轮新增文件: 37
- SEC应有预期: yes
- 中国公司相关: no

## 检查结果
- [FAIL] `profile_exists`: profile.md missing
- 建议: 检查 financials 模块是否成功写入 profile.md。
- [FAIL] `financials_exists`: financials.md missing
- 建议: 检查 financials 模块是否成功写入 financials.md。
- [FAIL] `xbrl_output`: financials_detailed.md missing
- 建议: 若为美股，检查 SEC CIK 映射与 XBRL 拉取。
- [FAIL] `sec_filings_count`: earnings filings: 0
- 建议: 若为美股，检查 SEC filings 是否成功下载。
- [WARN] `youtube_count`: youtube transcripts: 0
- 建议: 检查 yt-dlp、YouTube 搜索词和字幕可用性。
- [WARN] `podcast_count`: podcast files: 0
- 建议: 检查 Apple Podcasts 搜索是否返回结果。
- [PASS] `xiaoyuzhou_applicability`: 非中国相关公司，小宇宙为 0 不视为问题。
- [PASS] `report_freshness`: _collection_report.md fresh
- [PASS] `new_files_this_run`: files touched this run: 37
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
- organization/c_suite/brannin_mcbee.md
- organization/c_suite/brian_m_venturo.md
- organization/c_suite/deborah_crawford.md
- organization/c_suite/jeffrey_r_baker.md
- organization/c_suite/michael_n_intrator.md
- organization/c_suite/mr_brannin_mcbee.md
- organization/c_suite/mr_brian_m_venturo.md
- organization/c_suite/mr_jeffrey_r_baker.md
- organization/c_suite/mr_michael_n_intrator.md
- organization/c_suite/mr_nitin_agrawal.md
- organization/c_suite/mr_peter_salanki.md
- organization/c_suite/mr_sachin_jain.md
- organization/c_suite/ms_kristen_j_mcveety.md
- organization/c_suite/ms_sandhya_venugopal.md
- organization/c_suite/nitin_agrawal.md
- organization/c_suite/peter_salanki.md