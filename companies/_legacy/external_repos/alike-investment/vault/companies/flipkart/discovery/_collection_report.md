---
company: Flipkart
ticker: "FLIPKART (Private, Walmart subsidiary)"
collected: 2026-04-07
pipeline_version: "collect v2"
---

# Flipkart — 全量数据采集报告

**采集时间**: 2026-04-07
**公司类型**: 非上市（Walmart子公司，准备2026-2027 IPO）
**CEO**: Kalyan Krishnamurthy (Group CEO)
**创始人**: Sachin Bansal & Binny Bansal（均已完全退出）

## 采集步骤执行情况

### Step 1: collect.py 脚本 ✅
- **YouTube**: 失败（yt-dlp未安装），0个视频
- **Podcasts**: 成功，25个episode元数据
- **小宇宙**: API不可用，0个episode
- **财务模块**: 跳过（非上市公司无yfinance/SEC数据）
- 输出已从 `FLIPKART/` 移至 `vault/companies/flipkart/discovery/`

### Step 1.5: Perplexity深度研究 ✅
- **Twitter**: 4个URL发现，2个成功提取
- **Reddit**: 0个URL发现
- **Substack Analysis**: 9个URL发现，0个成功提取（全部paywall）
- **Podcasts/Transcripts**: 5个URL发现，1个成功提取（16,415字符）
- **News/Investigations**: 4个URL发现，4个成功提取
- 输出已从 `FLIPKART/sources/` 移至 vault

### Step 2: 社交媒体搜索 ✅
- **Twitter/X**: 10个高质量推文，覆盖IPO进展+快速商务+估值
- **Reddit**: 未找到高质量DD帖子（非上市公司在Reddit讨论较少）
- **Substack**: 10篇分析文章索引，覆盖竞争格局+估值+策略
- 输出: `sources/social/twitter_x.md`, `reddit_discussions.md`, `substack_analysis.md`

### Step 2.5: 创始人/CEO专项搜索 ✅
- Kalyan Krishnamurthy: IPO策略、增长目标、AI投资
- Sachin Bansal: 已创办Navi Group，完全退出Flipkart
- Binny Bansal: 已创办Opptra，完全退出Flipkart
- 输出: `sources/founder_2026-04-07.md`（完整版，覆盖3人）

### Step 3: WebSearch补充搜索 ✅（5个查询全部完成）
1. IPO最新进展: NCLT批准、总部迁回、银行选择
2. 估值变化: $20B(2018) → $37B(2024) → $60-70B(IPO目标)
3. 竞争格局: Flipkart 48% GMV vs Amazon 30-35% vs Meesho 9%
4. 快速商务: Flipkart Minutes ~800暗仓，目标1,200
5. 高管变动: CFO离职、4位VP/SVP离职、400-500裁员
- 输出: `sources/deep_search_2026-04-07.md`（完整版）

### Step 4: YouTube搜索 ✅（部分）
- WebSearch找到关键视频和报道链接
- Perplexity成功提取1个播客转录（16K字符）
- yt-dlp未安装，无法自动字幕提取
- 输出: `sources/youtube/search_results_2026-04-07.md`

### Step 5: 采集总结 ✅

## 文件统计

| 类别 | 文件数 | 备注 |
|------|--------|------|
| 播客元数据 | 25 | Apple Podcasts（2018-2026） |
| 社交媒体 | 3 | Twitter/X, Reddit, Substack |
| 创始人/CEO | 1 | 3人完整档案 |
| 深度搜索 | 1 | 5维度综合报告 |
| YouTube | 1 | 搜索结果+视频索引 |
| Perplexity | 5 | twitter, substack, podcasts, news, url_indexes |
| 既有文件 | 6 | 前期采集的org/leadership/signals等 |
| 配置文件 | 2 | _collection_report + _podcast_episodes.json |
| **总计** | **47** | **252KB** |

## 数据质量评估

| 维度 | 覆盖度 | 信源质量 | 备注 |
|------|--------|----------|------|
| IPO进展 | 高 | S2-S3 | TechCrunch, Bloomberg, Business Standard |
| 估值/财务 | 中 | S2-S3 | FY25数据可用，详细财报缺失（非上市） |
| 竞争格局 | 高 | S2-S3 | GMV/订单量双维度数据 |
| 快速商务 | 高 | S2-S3 | 暗仓数、订单量、城市覆盖详实 |
| CEO/领导层 | 中 | S2-S3 | Kalyan公开发言较少，缺深度访谈文本 |
| 创始人 | 中 | S2 | 两位创始人均已退出，历史信息充足 |
| 组织内部 | 低 | S1-S2 | 非上市公司，内部信息有限 |
| 员工视角 | 低 | S1 | 缺少Glassdoor/Blind数据 |

## 关键数据缺口

1. **详细财报**: 非上市公司无SEC/XBRL数据，需等IPO招股书
2. **CEO深度访谈文本**: Kalyan Krishnamurthy公开长篇访谈较少
3. **组织内部**: 缺少DEF 14A等组织架构文件
4. **员工情绪**: 需要Glassdoor/Blind采集
5. **YouTube字幕**: 需安装yt-dlp后重新采集
6. **中文源**: 小宇宙API不可用，缺少中文分析视角

## 建议下一步

1. **等待IPO招股书**: 将提供详细财务数据和组织信息
2. **补充Glassdoor采集**: 了解内部文化和员工满意度
3. **安装yt-dlp**: 重新采集YouTube视频字幕
4. **监控IPO进展**: 2026年4月预计开始银行pitch流程
5. **进入L2评分**: 基于现有数据可以尝试Alike Score初步评估
