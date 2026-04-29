---
credibility: S5
evidence: E3
source: collect-script + manual WebSearch
date: 2026-04-09
---

# RIPPLING (Rippling) — 数据采集报告
**采集时间**: 2026-04-09
**方法**: 自动采集(2026-04-08) + 手动WebSearch补充(2026-04-09)
**输出目录**: vault/companies/rippling/discovery

## 采集状态概览

| 模块 | 状态 | 说明 |
|------|------|------|
| profile | ✅ 成功 | 手动WebSearch生成，含公司概况、融资历史、竞争格局、关键里程碑 |
| financials | ✅ 成功 | 手动WebSearch生成，含ARR、估值历史、商业模式 |
| xbrl | ❌ N/A | 非上市公司，无SEC XBRL数据 |
| sec_filings | ❌ N/A | 非上市公司，无SEC filing |
| youtube | ✅ 成功 | 4个关键视频/访谈摘要 |
| podcasts | ✅ 成功 | 6个关键播客摘要 |
| xiaoyuzhou | ❌ N/A | 非中国公司，不适用 |
| org_basic | ✅ 成功 | 自动采集(骨架) |
| org_scan | ✅ 成功 | 自动采集(骨架) |
| founder | ✅ 成功 | 自动采集(骨架) + 手动补充 |
| governance | ⚠️ 有限 | 非上市，无proxy filing |

## 文件清单

### Core Files
- profile.md — 公司概况（融资、竞争、里程碑）
- financials.md — 财务数据（ARR、估值、商业模式）

### Organization (自动采集骨架)
- organization/_org_brief.md
- organization/_org_scan_report.md
- organization/_org_scan_request.md
- organization/governance_summary.md
- organization/overview/org_structure.md

### Sources — YouTube (4 files)
- sources/youtube/2022_Stratechery-Ben-Thompson-Interview-Parker-Conrad.md
- sources/youtube/2024-08_Parker-Conrad-Founder-Mode-Go-All-The-Way-To-The-Ground.md
- sources/youtube/2025-01_Garry-Tan-Interview-Parker-Conrad-Compound-Startup.md
- sources/youtube/2025-11_Parker-Conrad-Unconventional-Playbook-Revenge-to-Execution.md

### Sources — Podcasts (6 files)
- sources/podcasts/2024_20VC-Parker-Conrad-Compound-Startup-Benefits.md
- sources/podcasts/2024_Logan-Bartlett-Show-Parker-Conrad-Zenefits-Redemption.md
- sources/podcasts/2024_SaaStr-Parker-Conrad-Theory-Of-Compound-Startup.md
- sources/podcasts/2025-01_YC-How-To-Build-The-Future-Parker-Conrad.md
- sources/podcasts/2025-11_Sequoia-Capital-Parker-Conrad-Revenge-Fantasy.md
- sources/podcasts/2025_TechCrunch-Parker-Conrad-Rippling-Hasnt-Won-Yet.md

### Other Sources
- sources/founder_voice.md (骨架)

## 总计
- **核心文件**: 2 (profile + financials)
- **组织文件**: 5
- **YouTube摘要**: 4
- **Podcast摘要**: 6
- **其他来源**: 1
- **总文件数**: 18

## 信源质量说明
- 非上市公司，无SEC filing / XBRL / 10-K等S5级信源
- 核心财务数据来自媒体报道(S2-S3)，估值来自融资公告(S3)
- CEO访谈/播客为S4级信源（直接主观）
- 组织数据需后续通过 /org-scan 和 /founder 深挖补充

## 已知缺口
1. **无SEC filing**: 非上市公司，预期之内
2. **财务透明度低**: ARR/Revenue均为媒体估计，非官方披露
3. **组织穿透不足**: org_scan骨架需要通过 /private-search 和 /org-scan 深挖
4. **CEO认知档案未生成**: 需要 /ceo-cognition-profile 基于现有播客/访谈数据生成
5. **竞品深度对比缺失**: 需要 /deepsearch 做Deel、Gusto、Workday横向比较
