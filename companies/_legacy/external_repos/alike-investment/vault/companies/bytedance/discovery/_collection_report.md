---
title: "ByteDance Discovery Collection Report"
date: 2026-04-07
company: ByteDance
---

# ByteDance (字节跳动) — 数据采集报告

**采集时间**: 2026-04-07
**总耗时**: ~15分钟
**公司类型**: 非上市公司

## 采集模块状态

| 模块 | 状态 | 文件数 | 说明 |
|------|------|--------|------|
| financials (yfinance) | 跳过 | 0 | 非上市公司，无公开财务数据 |
| xbrl (SEC EDGAR) | 跳过 | 0 | 非上市公司，无SEC filing |
| full_dump | 跳过 | 0 | 非上市公司 |
| sec_filings | 跳过 | 0 | 非上市公司 |
| youtube | 成功 | 20 | 19/20有字幕，298,132字符 |
| podcasts | 失败 | 0 | Python requests模块缺失 |
| xiaoyuzhou | 失败 | 0 | Python requests模块缺失 |
| perplexity | 部分成功 | 5 | 27个URL发现，1个全文提取成功（多数遇paywall） |
| social (Twitter) | 成功 | 1 | WebSearch综合整理 |
| social (Reddit) | 成功 | 1 | WebSearch综合整理 |
| social (Substack) | 成功 | 1 | WebSearch + WebFetch全文提取 |
| founder/CEO | 成功 | 1 | 张一鸣 + 梁汝波深度研究 |
| deep_search (5维度) | 成功 | 1 | 最新新闻、估值、竞争、TikTok ban、AI战略 |
| org_scan | 成功 | 1 | 核心高管团队 + AI组织架构 |
| signals | 成功 | 1 | 8个关键投资信号 |
| guru | 成功 | 1 | 机构投资者 + 分析师观点 |
| profile | 成功 | 1 | 公司概况 + 财务 + 竞争格局 |

## 文件统计

- **总文件数**: 42个
- **总数据量**: ~524KB
- **YouTube字幕**: 19个视频，298,132字符
- **社交媒体**: 3个综合文件
- **深度研究**: 5个专题文件
- **Perplexity**: 5个文件（含URL索引）

## YouTube视频清单（20个）

| # | 文件 | 大小 |
|---|------|------|
| 1 | Iran-Tanks-IPOs--2026-VC-Outlook-with-PitchBook--C | 73KB |
| 2 | ByteDance-TikTok-and-Chinas-Growing-Influence-in-G | 57KB |
| 3 | TikTok-CEO-Shou-Chew-on-Its-Future--and-What-Makes | 38KB |
| 4 | Chinas-Seedance-AI-Collapsing-Hollywoods-Economics | 33KB |
| 5 | ByteDance-to-Get-About-50-of-TikTok-US-Profit-Unde | 16KB |
| 6 | Podcast-ByteDances-SeaDance-20-The-AI-Video-Revolu | 15KB |
| 7 | Deep-Dive-With-DanielThe-TikTok-Ban-SCOTUS-China-a | 12KB |
| 8 | UNRELENTING-Tom-Cotton-Unflinchingly-Grills-TikTok | 9KB |
| 9 | ByteDance-Making-1-Billion-in-Games---Business-of | 6KB |
| 10 | Bloomberg-News-Now-Dip-Buying-Raises-Stocks-ByteDa | 6KB |
| 11 | Former-TikTok-CEO-Kevin-Mayer-on-ByteDance-decisio | 5KB |
| 12 | TikTok-CEO-Shou-Zi-Chew-I-dont-condone-effort-by-f | 4KB |
| 13 | Most-Americans-dont-appreciate-how-big-Bytedances | 4KB |
| 14 | ByteDance-and-Oracle-Ink-TikTok-US-Joint-Venture | 4KB |
| 15 | Oracle-TikTok-deal-is-a-huge-win-for-ByteDance-Lig | 3KB |
| 16 | TikTok-US-Deal-Skyrockets-ByteDance-Valuation-to-4 | 2KB |
| 17 | TikTok-owner-Bytedances-revenue-surges-in-2020-Mic | 1KB |
| 18 | TikTok-CEO-Grilled-in-Congress-Key-Moments | 1KB |
| 19 | ByteDance-TikTok-suitors-discuss-options-to-advanc | 1KB |
| 20 | ByteDance-CEO-returns-to-apartment (无字幕) | 0KB |

## 核心发现摘要

### 财务
- 2025年预计收入$1860亿（+20% YoY），利润$500亿
- 已超越Meta成为全球最大社交媒体公司（按收入）
- 估值从$330B升至$550B（6个月+66%）

### 组织
- 张一鸣退居二线但深度参与AI/AGI战略
- 梁汝波推动"务实浪漫" + "不官僚不内卷"文化改革
- AI组织独立建制：Seed + Flow + Stone直接向CEO汇报
- 40%+ AI研究人员为近两年新招

### AI战略
- 豆包（Doubao）155M WAU，中国AI第一
- $230亿2026年AI CapEx
- Doubao 2.0定位Agent Era
- AI手机 + AI电商 + Seedance视频生成

### 关键风险
- TikTok US交易算法许可模式法律灰色地带
- 芯片出口管制限制
- 非上市缺乏透明度
- AI CapEx ROI不确定

## 建议下一步

1. **L2 Alike Score评分** — 数据量充足，可启动D1-D7评分
2. **补充播客数据** — 修复requests模块后重新运行podcasts/xiaoyuzhou
3. **组织穿透** — 对Seed/Flow/Stone团队做深度VP级别搜索
4. **中文源补充** — 搜索更多关于字节跳动组织文化的中文深度分析
