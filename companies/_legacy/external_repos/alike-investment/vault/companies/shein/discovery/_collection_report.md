# SHEIN — 完整数据采集报告
**公司**: SHEIN（希音）
**状态**: Pre-IPO（非上市）
**创始人**: Chris Xu (许仰天 / Sky Xu)
**执行主席**: Donald Tang (唐伟)
**采集时间**: 2026-04-07
**Vault路径**: vault/companies/shein/

---

## 采集执行摘要

### Step 1: collect.py 统一采集脚本
- **YouTube**: 失败 (yt-dlp未安装)，0个视频
- **Podcasts**: 成功，14个episode元数据
- **小宇宙**: 部分成功，API不可用但通过WebSearch发现相关内容
- financials/xbrl/full_dump/sec_filings: 跳过（非上市公司无公开财务数据）

### Step 1.5: Perplexity深度研究
- **运行成功**，5个维度
- URLs发现: 26个
- 页面成功抓取: 5个（其余paywall或超时）
- 总字符数: 7,399
- 输出目录: substack_analysis/, reddit/, twitter/, news_investigations/, podcasts_transcripts/

### Step 2: 全平台社交媒体搜索
- **Twitter/X**: 成功 — De minimis关税影响为主要讨论话题，DAU下降数据
- **Reddit**: 成功 — IPO估值轨迹（$100B→$10B），上市策略辩论
- **Substack**: 成功 — 商业模式深度分析，供应链创新，ESG争议

### Step 2.5: 创始人/CEO专项搜索
- **Chris Xu**: 成功 — 2026年2月首次公开演讲（重大信号），管理风格详细画像
- **Donald Tang**: 成功 — 完整职业经历（Bear Stearns Asia→SHEIN），角色定位分析
- **Molly Miao (苗苗)**: 成功 — COO角色，联合创始人，日常运营负责人

### Step 3: WebSearch补充搜索 (5个查询)
1. IPO最新进展: 双轨策略(London+Hong Kong)，CSRC审批障碍
2. 估值变化: $100B(2022) → $45B(2024) → $10B(2025.8)
3. 竞争格局: SHEIN 18% vs Zara 17% vs H&M 5%全球快时尚市场
4. ESG/强迫劳动: 英国议会质询，BBC调查，新疆棉花风险披露分歧
5. 供应链本地化: 巴西$1.5亿投资+2,000工厂计划，墨西哥扩展

### Step 4: YouTube Transcript
- 直接提取失败（无yt-dlp），通过WebSearch识别关键视频
- 推荐优先提取: 20VC Donald Tang访谈, Channel 4 "Inside The Shein Machine"

---

## 文件清单 (36个文件, ~196KB)

### discovery/sources/
| 文件 | 类型 | 信源等级 | 大小 |
|------|------|---------|------|
| deep_search_2026-04-06.md | 8维度深搜（前次） | S3/E3 | 大 |
| deep_search_2026-04-07.md | 8维度深搜（更新） | S3/E3 | 大 |
| founder_2026-04-07.md | 创始人/CEO专搜 | S2-S4/E2-E3 | 中 |
| guru_2026-04-07.md | 投资大师持仓 | S2-S3/E2 | 中 |
| org_scan_2026-04-07.md | 组织架构穿透 | S3-S4/E2-E3 | 中 |
| signals_2026-04-07.md | 信号扫描 | S2-S3/E1-E2 | 中 |
| social_search_2026-04-07.md | 社交搜索汇总 | S1-S3/E1-E2 | 中 |

### discovery/sources/social/
| 文件 | 平台 | 信源等级 |
|------|------|---------|
| twitter_x.md | Twitter/X | S2/E1-E2 |
| reddit_discussions.md | Reddit/投资社区 | S1/E1 |
| substack_analysis.md | Substack | S2/E2 |

### discovery/sources/podcasts/ (14个episode)
- 时间跨度: 2021-10 ~ 2026-03
- 中文播客: 4个（希音破隐、硅谷宝典、群雄逐鹿、真假希音心）
- 英文播客: 10个（涵盖tariff影响、IPO、商业模式）

### discovery/sources/perplexity/
- substack_analysis/ — Substack全文提取（5,735字符）
- news_investigations/ — 新闻调查全文（1,664字符）
- twitter/, reddit/, podcasts_transcripts/ — URL索引（内容多为paywall）

### discovery/sources/youtube/
- youtube_search_2026-04-07.md — 视频发现清单（无直接转录）

### leadership/
- ceo-cognition-profile_2026-04-06.md — CEO认知档案

### org/
- winner-pattern-org_2026-04-06.md — 组织模式评估

---

## 核心发现摘要

### 公司定位
- 全球最大快时尚平台，18%全球市场份额
- 从D2C品牌转型为Marketplace平台（6,000+工厂，13,000+商户）
- 2024年营收$38B，2025年预计$58-60B，净利润目标$2.6B

### 组织关键信号
1. **创始人破隐**（2026.2）: 18年来首次公开演讲，为IPO+政府关系铺路
2. **双轨IPO**（2025.7）: London + Hong Kong同时推进，CSRC是关键阻碍
3. **估值暴跌**: $100B(2022) → $10B(2025.8)，核心原因: 利润下滑+关税冲击+IPO延期
4. **De Minimis终结**: 美国2025年5月/8月分阶段取消，SHEIN DAU下降25%
5. **供应链本地化**: 巴西、墨西哥扩展制造，美国15+仓库，缓解关税冲击

### 信息缺口
- CEO认知深度不足（许仰天极少公开发言，仅1次公开演讲）
- 内部组织架构不透明（C-suite多数身份未公开）
- 财务数据依赖第三方估算（非上市无官方披露）
- 员工视角缺失（无Glassdoor/脉脉数据）

---

## 建议下一步
1. **提取20VC Donald Tang播客转录** — 最重要的高管原声（需安装yt-dlp）
2. **Channel 4纪录片提取** — ESG证据链
3. **执行 /alike SHEIN** — 进入L2 Alike Score评分
4. **补充员工视角** — 搜索脉脉/Glassdoor上的SHEIN员工评价
