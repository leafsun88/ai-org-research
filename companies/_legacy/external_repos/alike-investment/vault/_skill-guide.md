# Alike Investment — Skill速查指南

> 每次开始研究前先读这个文件，快速定位该用哪个skill

## 四层Pipeline
```
L1: 数据采集 → vault/companies/{slug}/discovery/
L2: Alike Score (D1-D7 + Fit) → vault/companies/{slug}/scoring/alike-memo.md
L3: Inflection分析 → scoring/org-inflection.md + biz-inflection.md
L4: Investment Memo → scoring/investment-memo.md
```

## Skill速查表

| Skill | 层级 | 用途 | 输入 | 输出路径 |
|-------|------|------|------|----------|
| `/collect` | L1 | 一键全量采集（8模块并行） | TICKER [Name] | `discovery/` |
| `/deepsearch` | L1 | 8维度深度搜索 | TICKER Name | `discovery/sources/deep_search_*.md` |
| `/founder` | L1 | CEO公开言论+insider trading | TICKER "CEO" | `discovery/sources/founder_voice.md` |
| `/guru` | L1 | 投资大师持仓 | TICKER Name | `discovery/sources/guru_opinions.md` |
| `/org-scan` | L1 | 组织架构穿透（C-suite→VP） | TICKER "Name" | `discovery/organization/` |
| `/social-search` | L1 | 社交媒体+分析平台搜索 | TICKER "Name" ["CEO"] | `discovery/sources/` |
| `/private-search` | L1 | 私有公司人物为核心搜索 | TICKER "Name" ["CEO"] | `discovery/organization/` |
| `/signals-scan` | L1 | 每日信号快扫（5min） | TICKER | `discovery/signals/{date}.md` |
| `/transcript-critic` | L1 | 音视频转录+分析 | .vtt/URL | `discovery/transcripts/` |
| `/alike-memo` | **L2** | D1-D7统一评分+Fit+Alike Score | TICKER | `scoring/alike-memo.md` |
| `/alike` | **L2** | 智能路由（自动判断层级） | TICKER | 调用下游skill |
| `/winner-pattern-org` | L2辅助 | 组织Winner Pattern深度分析 | Company | 7D评分+A类机制 |
| `/vault-save` | 支撑 | 持久化研究到vault | (读context) | vault + _index.json |
| `/vault-search` | 支撑 | 搜索已有研究 | 公司/关键词 | 文件路径+摘要 |
| `/vault-status` | 支撑 | Vault健康仪表盘 | 无 | 统计+覆盖热图 |
| `/vault-brief` | 支撑 | 公司一页概览 | 公司名 | 简报+覆盖矩阵 |

## Alike Score计算公式
```
Alike Score = (D1×0.20 + D2×0.15 + D3×0.15 + D4×0.10 + D5×0.10 + D6×0.15 + D7×0.15) × 20
```
Fit Score独立，不参与加权。

## D1-D7校准锚点（5/5长什么样）

| 维度 | 权重 | 5/5标杆 | 核心特征 |
|------|------|---------|----------|
| D1 CEO认知 | 20% | Jensen/Tobi/黄峥 | 第一性原理+20年长期主义+自我颠覆 |
| D2 Key Leader | 15% | Netflix双CEO/PDD四柱 | 创始人退后公司不受影响 |
| D3 考核机制 | 15% | Netflix Keeper Test/PDD赛马 | 机制倒逼选拔，无政治 |
| D4 信息架构 | 10% | NVIDIA T5T/Shopify GSD | CEO触达ground truth |
| D5 熵减能力 | 10% | AppLovin人减半营收+43% | 人效持续提升，主动精简 |
| D6 人才密度 | 15% | AppLovin人均利1000万$ | Pay top + Keeper Test |
| D7 Key Bet | 15% | NVIDIA CUDA 20年/PDD TEMU | All-in + 长期验证 |
| Fit | 独立 | 业务本质→组织形态完美适配 | 组织放大业务，非模仿他人 |

## 标准研究流程（每家公司）

### Step 1: L1数据采集
```bash
python3 scripts/collect_lite.py TICKER "CompanyName"
python3 scripts/fetch_youtube_vault.py TICKER "CompanyName" 15
```

### Step 2: D1-D7组织穿透（/winner-pattern-org）
- 读取discovery数据 + _calibration.json + org_patterns.md
- 执行: Step 0业务本质 → D1-D7评分 → Fit → 生成力判断
- 输出: `org/{date}.md` + `organization/core_team.md`

### Step 3: Alike Memo生成（/alike-memo）
- 读取org分析 + 校准矩阵
- 4步: 业务本质画像 → D1-D7校准评分 → Fit Score → 生成力判断
- 计算Alike Score (0-100)
- 输出: `scoring/alike-memo.md`

### Step 4: BIZ_INFLECTION + Key Questions
- 基于alike-memo + 财务数据
- ABCD四层(Asset/Engine Swap/Valuation/Catalyst)
- 提取2-3个最关键KQ

### Step 5: Dashboard注入（index-ye.html）
- CANDIDATE_SCORES (D1-D7分数)
- BIZ_INFLECTION (ABCD conviction)
- COMPANY_STATUS (Key Questions)

## Inflection时间差校准
| 组织变化类型 | 到业务验证的lag |
|-------------|----------------|
| CEO更换 | 12-24个月 |
| 组织重组 | 12-18个月 |
| 人才转移 | 12-18个月 |
| 文化变革 | 18-36个月 |

## 关键文件路径
- 校准矩阵: `vault/old-friends/_calibration.json`
- 评判标准: `skills/winner-pattern-org/references/org_patterns.md`
- Old Friend档案: `vault/old-friends/{name}/profile.md`
- 公司数据: `vault/companies/{slug}/`
- Dashboard: `product-demo/index-ye.html`（本地，不push）
