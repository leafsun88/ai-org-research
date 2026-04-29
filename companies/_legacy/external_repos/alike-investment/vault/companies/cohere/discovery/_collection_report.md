---
credibility: S5
evidence: E3
source: collect-script + manual-websearch
date: 2026-04-09
---

# Cohere — 数据采集报告
**采集时间**: 2026-04-09 (初始自动采集) + 2026-04-09 (手动WebSearch补充)
**输出目录**: vault/companies/cohere/discovery

## 采集概述
Cohere为私有公司（未上市），无SEC filing、无XBRL数据、无公开财报。采集策略以WebSearch聚合公开信息为主，辅以自动化podcast/YouTube爬取。

### Phase 1: 自动采集（collect script）
- financials: 框架生成（N/A占位）
- profile: 框架生成（N/A占位）
- xbrl: 不适用（私有公司）
- sec_filings: 不适用（私有公司）
- youtube: 搜索完成，0条有效transcript
- podcasts: 10条episode采集
- org_basic/org_scan: 框架生成
- founder: 3条founder source + founder_voice.md

### Phase 2: 手动WebSearch补充（2026-04-09）
- **profile.md**: 重写完整版（公司概况、融资历史、产品、竞争、里程碑、领导层）
- **financials.md**: 重写完整版（估值、ARR增长、商业模式、客户、竞争对比）
- **YouTube sources**: 新增4个视频/媒体报道摘要
  - Bloomberg TV: CEO on Next Wave of Generative AI (2025-10)
  - Bloomberg TV: Revenue Doubled (2025-05)
  - North Platform Launch coverage (2025-08)
  - Grit Podcast: Synthetic Data and Future of AI (2025-11)
- **Podcast sources**: 新增4个高质量podcast摘要
  - MAD Podcast: Inside the Paper That Changed AI (2025-06)
  - 20VC: Nick Frosst on competing with OpenAI/Anthropic (2025-09)
  - MLST: Aidan Gomez on AI Inner Monologue (2024-06)
  - SiliconANGLE: Google & Cohere Audio Models (2026-03)

## 文件统计

### 核心文件
| 文件 | 状态 | 大小 |
|------|------|------|
| profile.md | 完整 | ~5KB |
| financials.md | 完整 | ~4KB |
| organization/_org_scan_report.md | 框架 | ~1KB |
| organization/overview/org_structure.md | 框架 | ~1KB |
| sources/founder_voice.md | 已有 | ~1KB |

### Sources统计
| 类别 | 数量 | 备注 |
|------|------|------|
| YouTube | 4 | 手动WebSearch采集 |
| Podcasts | 14 | 10(自动) + 4(手动) |
| Founder sources | 3 | 自动采集 |
| Earnings | 0 | 不适用（私有公司） |

### 私有公司特殊说明
- 无SEC filing / XBRL / proxy filing — 这是预期行为，不是采集失败
- 财务数据依赖媒体报道（S2-S3），非公司直接披露
- 组织信息依赖LinkedIn/媒体报道，深度有限
- IPO如果实现，将获得完整的公开财务数据

## 数据质量评估
- **profile.md**: 信息全面，涵盖基本信息、融资、产品、竞争、里程碑 ✅
- **financials.md**: 私有公司范围内尽可能完整，包含ARR增长、商业模式、客户 ✅
- **YouTube**: 4个高相关性视频/报道，覆盖CEO公开陈述 ✅
- **Podcasts**: 14个episode，包含CEO和Co-Founder的深度访谈 ✅
- **Organization**: 基础框架已有，需运行/org-scan补充高管详细信息 ⚠️
- **信息缺口**: 具体盈利数据、详细客户合同、内部组织结构 ❌

## 下一步建议
1. 运行 `/org-scan Cohere` 补充高管详细档案（C-Suite, VP级别）
2. 运行 `/founder Cohere` 深挖创始人社交媒体和公开言论
3. 如IPO消息确认，立即更新financials.md和profile.md
4. 考虑transcript-critic处理关键podcast（MAD Podcast, 20VC）

**总计**: ~35个文件, ~40KB
