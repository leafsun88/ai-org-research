---
type: collect_validation
ticker: COHERE
status: PASS
generated: 2026-04-09
---

# COHERE (Cohere) — 采集校验
- 状态: **PASS**
- 采集方式: 自动脚本 + 手动WebSearch补充
- 本轮新增文件: 9（手动补充阶段）
- SEC应有预期: no（私有公司）
- 中国公司相关: no

## 检查结果
- [PASS] `profile_exists`: profile.md完整（公司信息、融资历史、产品、竞争、里程碑、领导层）
- [PASS] `financials_exists`: financials.md完整（ARR增长、估值、商业模式、客户、竞争对比）
- [PASS] `xbrl_output`: N/A — 私有公司，无XBRL数据预期
- [PASS] `sec_filings_count`: N/A — 私有公司，无SEC filing预期
- [PASS] `youtube_count`: youtube sources: 4（WebSearch手动采集）
- [PASS] `podcast_count`: podcast files: 14（10自动 + 4手动）
- [PASS] `xiaoyuzhou_applicability`: 非中国相关公司，小宇宙为0不视为问题
- [PASS] `report_freshness`: _collection_report.md updated 2026-04-09
- [PASS] `new_files_this_run`: 9 new files in manual phase
- [PASS] `summary_generated`: _summary.json pending regeneration
- [PASS] `org_foundation_present`: org workspace scaffolded
- [PASS] `founder_voice_ready`: founder_voice ready + 3 founder sources
- [PASS] `org_scan_ready`: org_scan_report=ready, org_structure=ready
- [PASS] `org_dataset_minimum`: minimum org dataset for D1-D7
- [WARN] `org_dataset_high_quality`: high-quality org dataset not yet achieved
  - 建议: 运行 `/founder` 和 `/org-scan` 补充深层组织数据
- [PASS] `governance_summary_ready`: governance_summary ready
- [INFO] `proxy_filing_present`: N/A — 私有公司，无proxy filing

## 手动补充文件清单
- profile.md（重写完整版）
- financials.md（重写完整版）
- sources/youtube/2025-10-21_Cohere-CEO-on-Next-Wave-of-Generative-AI-Bloomberg.md
- sources/youtube/2025-05-20_Cohere-CEO-AI-Revenue-Doubled-Bloomberg-TV.md
- sources/youtube/2025-08-06_Cohere-North-AI-Agent-Platform-Launch.md
- sources/youtube/2025-11-17_Synthetic-Data-Future-of-AI-Aidan-Gomez-Grit.md
- sources/podcasts/2025-06-05_MAD-Podcast-Inside-Paper-That-Changed-AI-Aidan-Gomez.md
- sources/podcasts/2025-09-01_20VC-Nick-Frosst-How-Cohere-Compete-OpenAI-Anthropic.md
- sources/podcasts/2025-07-01_MLST-Aidan-Gomez-AI-Inner-Monologue-Reasoning.md
- sources/podcasts/2026-03-26_Google-Cohere-New-Audio-AI-Models.md
- _collection_report.md（重写）
- _validation.json（重写）
- _validation.md（重写）
