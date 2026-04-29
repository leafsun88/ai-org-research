---
type: collect_validation
ticker: DATABRICKS
status: FAIL
generated: 2026-04-08
---

# DATABRICKS (Databricks) — 采集校验
- 状态: **FAIL**
- 总耗时: 662.1秒
- 本轮新增文件: 24
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
- [PASS] `podcast_count`: podcast files: 16
- [PASS] `xiaoyuzhou_applicability`: 非中国相关公司，小宇宙为 0 不视为问题。
- [PASS] `report_freshness`: _collection_report.md fresh
- [PASS] `new_files_this_run`: files touched this run: 24
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
- _podcast_episodes.json
- organization/_org_brief.md
- organization/_org_scan_report.md
- organization/_org_scan_request.md
- organization/governance_summary.md
- organization/overview/org_structure.md
- sources/founder_voice.md
- sources/podcasts/2025-05-31_Snowflake--Databricks-Cross-the-Rubicon-into-a-New.md
- sources/podcasts/2025-06-12_AI-Ads-Hit-the-NBA-Finals--Kalshi-Databricks-Luma.md
- sources/podcasts/2025-08-04_Databricks-IPO-and-the-Next-Three-Years-in-AI.md
- sources/podcasts/2025-08-07_Unlocking-Value-with-Ari-Kaplan-from-Databricks.md
- sources/podcasts/2025-08-21_20VC-Databricks-at-100BN--Chamaths-SPAC-Revival-Pe.md
- sources/podcasts/2025-08-27_Inside-OpenAIs-500B-Valuation--Altimeters-Largest.md
- sources/podcasts/2025-09-08_Does-Anthropic-Owe-Me-3000.md
- sources/podcasts/2025-09-26_OpenAIs-ChatGPT-Pulse-Debuts-Musks-AI-Strategy-and.md
- sources/podcasts/2025-12-04_E240-xAI-230B-valuation-Databricks-134B-valuation.md
- sources/podcasts/2025-12-19_Hardwares-brutal-week-iRobot-Luminar-and-Rad-Power.md
- sources/podcasts/2025-12-19_KI-ist-keine-Zahnpasta--Funding-Woche-Databricks-W.md
- sources/podcasts/2026-01-09_E242-OpenAI-raise-at-830b-Anthropic-raise-at-350b.md