---
type: collect_validation
ticker: SNPS
status: FAIL
generated: 2026-04-08
---

# SNPS (Synopsys) — 采集校验
- 状态: **FAIL**
- 总耗时: 1084.6秒
- 本轮新增文件: 22
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
- [PASS] `new_files_this_run`: files touched this run: 22
- [PASS] `summary_generated`: _summary.json generated
- [PASS] `org_foundation_present`: org workspace scaffolded
- [PASS] `founder_voice_ready`: founder_voice ready
- [WARN] `org_scan_ready`: org_scan_report=ready, org_structure=pending
- 建议: 运行 /org-scan 补齐组织静态与关键高管变动。
- [WARN] `org_dataset_minimum`: minimum org dataset for D1-D7
- 建议: 在 founder/org-scan 完成前，不建议进入高质量 D1-D7 评分。
- [WARN] `org_dataset_high_quality`: high-quality org dataset
- 建议: 当前若仍是 auto_basic 版本，建议继续运行 `/founder` 和 `/org-scan` 做深挖。
- [PASS] `governance_summary_ready`: governance_summary ready
- [PASS] `proxy_filing_present`: proxy filings: 1

## 本轮新增文件（前20）
- _collection_report.md
- organization/_org_brief.md
- organization/_org_scan_report.md
- organization/_org_scan_request.md
- organization/c_suite/aart_j_de_geus_phd.md
- organization/c_suite/alessandra_costa.md
- organization/c_suite/ann_minooka.md
- organization/c_suite/janet_lee.md
- organization/c_suite/sassine_ghazi.md
- organization/c_suite/shelagh_glaser.md
- organization/c_suite/sudhindra_kankanwadi.md
- organization/c_suite/tushar_jain.md
- organization/governance_summary.md
- organization/overview/org_structure.md
- organization/proxy/2026-02-19_DEF 14A.md
- organization/sources/alessandra_costa/alessandra_costa_svp_operations_at_synopsys.md
- organization/sources/janet_lee/httpslongbridgecomennews271991215.md
- organization/sources/sassine_ghazi/who_is_sassine_ghazi_discover_their_role_as_president_and_ch.md
- organization/sources/sassine_ghazi/who_is_the_ceo_of_synopsys_sassine_ghazis_bio_clay.md
- organization/sources/shelagh_glaser/who_is_the_cfo_of_synopsys_shelagh_glasers_bio_clay.md