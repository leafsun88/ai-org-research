---
type: collect_validation
ticker: CDNS
status: FAIL
generated: 2026-04-08
---

# CDNS (Cadence Design Systems) — 采集校验
- 状态: **FAIL**
- 总耗时: 862.7秒
- 本轮新增文件: 35
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
- [PASS] `new_files_this_run`: files touched this run: 35
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
- organization/_org_brief.md
- organization/_org_scan_report.md
- organization/_org_scan_request.md
- organization/c_suite/anirudh_devgan_phd.md
- organization/c_suite/ariel_sella.md
- organization/c_suite/dr_anirudh_devgan_phd.md
- organization/c_suite/john_m_wall.md
- organization/c_suite/marc_taxay_jd.md
- organization/c_suite/mr_ariel_sella.md
- organization/c_suite/mr_john_m_wall.md
- organization/c_suite/mr_marc_taxay_jd.md
- organization/c_suite/mr_paul_scannell.md
- organization/c_suite/mr_richard_gu.md
- organization/c_suite/mr_tarak_ray.md
- organization/c_suite/paul_scannell.md
- organization/c_suite/richard_gu.md
- organization/c_suite/tarak_ray.md
- organization/governance_summary.md
- organization/overview/org_structure.md