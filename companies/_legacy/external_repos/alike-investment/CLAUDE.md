# Alike Investment — AI-native 投资系统

## 项目结构
- `vault/` — Research Vault 知识库（以公司为核心的文件系统）
- `vault/old-friends/` — Old Friends校准坐标系（D1-D7标杆 + Inflection标准样本 + 时间差校准）
- `product-demo/` — Alike Investment 前端SPA（单文件 index.html，零依赖）
- `skills/` — 投研Skill定义（分析层 + 采集层）
- `scripts/discovery/` — 数据采集Python脚本（yfinance, SEC EDGAR, YouTube等）
- `.team/` — 团队协作（Git-based）

## 启动命令
- 前端：`npx serve product-demo -l 3456`

## 核心入口
- **一键研究**：`/alike TICKER` — 自动判断进度，从正确层级开始
- 一键采集：`/collect TICKER [CompanyName]`

## 四层投研架构（Pipeline v2）

```
L1: 数据采集（Duolingo级别详尽度）→ vault/companies/{slug}/discovery/
  ↓ 自动
L2: Alike Score（D1-D7统一评分 + Fit Score）→ vault/companies/{slug}/scoring/alike-memo.md
  ↓ Top30自动触发
L3: Inflection分析（组织拐点 + 业务拐点）→ scoring/org-inflection.md + biz-inflection.md
  ↓ 有催化剂 + 用户确认
L4: Investment Memo（估值、认知差、买入逻辑）→ scoring/investment-memo.md
```

## 投资哲学（不可变）
- 好组织 + 好Timing = 好投资
- 组织先于战略，战略先于业务，业务先于财务
- 组织变化 → 战略变化 → 业务结果 → 股价反映，时间差 = 投资窗口
- "学我者生，似我者死" — 衡量组织生成力（generative capacity），不是输出相似度
- 核心问题："Who is the next XX?"（XX = Old Friends 基准公司）

## Old Friends 校准系统
- 存储：`vault/old-friends/{name}/profile.md`（三层校准：D1-D7 + Org-Inflection + Biz-Inflection）
- 校准矩阵：`vault/old-friends/_calibration.json`（D1-D7标杆 + inflection_anchors + time_lag_calibration）
- Old Friends提供三层校准：
  - **Layer 1**: D1-D7组织DNA — "5/5长什么样"
  - **Layer 2**: Org-Inflection样本 — "好的组织拐点长什么样，时间差多久"
  - **Layer 3**: Biz-Inflection样本 — "好的业务拐点长什么样，ABCD四层怎么演变"
- Old Friends是校准锚点，不是模板——我们知道"5/5长什么样"，但不要求候选公司"变得像它"
- 好投资 = 好组织（D1-D7高分）+ 好Timing（识别inflection + 抓住时间差窗口）
- 当前Old Friends（7位）：Netflix, PDD, AppLovin, Meta, Shopify, Nvidia, Anthropic
- 原始研究文档：`vault/old-friends/{name}/*.md`（14篇深度研究）

## Alike Score 统一框架
- D1-D7权重固定，不因Old Friend不同而变化
- 一家公司只有一个Alike Score，不分per-benchmark
- 核心skill：`skills/alike-memo/SKILL.md`

| 维度 | 权重 |
|------|------|
| D1 CEO认知质量 | 20% |
| D2 Key Leader深度 | 15% |
| D3 考核激励机制 | 15% |
| D4 信息架构 | 10% |
| D5 组织熵减能力 | 10% |
| D6 Talent Density | 15% |
| D7 Key Bet质量 | 15% |
| Fit Score | 独立（不参与加权） |

## Research Vault 约定
- 路径：`vault/companies/{kebab-case-name}/`
- 公司数据目录：
  - `discovery/` — L1采集raw数据
  - `scoring/` — L2-L4评分+决策文档（alike-memo, inflection, investment-memo）
  - `leadership/` — CEO认知档案
  - `org/` — 组织深度分析
  - `fundamental/` — 财务/业务分析
  - `exec-voice/` — 高管原声
  - `employee/` — 员工视角
  - `red-team/` — 反方论证
  - `intel/` — 竞争情报
  - `transcripts/` — 电话会/访谈转录
  - `notes/` — 研究笔记/杂项
- 全局索引：`vault/_index.json`（每次vault写入后必须同步更新）
- Schema：`vault/_schema/data-infra-schema.json`
- Calibration Memory：`vault/_calibration/signal-patterns.json`
- 文件命名：`{dimension}/{YYYY-MM-DD}.md`
- 研究完成后必须提示 /vault-save

## 数据采集层（Discovery）
- 采集输出路径：`vault/companies/{slug}/discovery/`（raw数据，不与分析混合）
- TICKER→slug映射：`vault/_index.json` 的 `ticker_map`
- 数据结构文档：`vault/_schema/DATA_SCHEMA.md`
- 采集skills：collect, deepsearch, founder, guru, org-scan, private-search, signals-scan, social-search, transcript-critic
- 所有采集数据必须在YAML frontmatter中标注 `credibility: S?` 和 `evidence: E?`

## 信源置信度（S1-S5）
- S5 = S4 = S3（同等权重，均为可信信源）
  - S5：直接客观（SEC filing, 财报原文）
  - S4：直接主观（CEO访谈, 内部信源）
  - S3：间接客观（分析师报告, 行业数据）
- S2：间接主观（媒体报道, 社交媒体）— 权重下降
- S1：三手主观（论坛传闻, 未经证实消息）— 最低权重

## Invest Brain 核心框架
- D1-D7组织评分的权威定义：`skills/winner-pattern-org/SKILL.md`
- D1-D7案例库+子维度标准：`skills/winner-pattern-org/references/org_patterns.md`
- 分析起点永远是 Step 0（业务本质画像），不是直接打分
- 组织-业务适配度(Fit Score)是独立于D1-D7的最重要单一判断
- 信息不足时必须 ⛔ 报错拒绝打分，绝不硬打

## 认知模式（3模式 triangulate）
- Evidence Validation（证据校验）
- Pattern Matching（模式匹配）
- Adversarial Thinking（对抗性思考）

## Signal Engine 决策矩阵
- AUTO-APPLY：≥80% + HIGH/MED significance
- PROPOSAL：50-79%
- KEY QUESTION：需要更多信息
- WATCH：25-49%
- DISCARD：<10%

## 前端架构
- Status = AI结论面板（只读：Score Card + Signals + KQs + Biz + Artifacts）
- Cowork = AI工作台（交互：Chat + Signal展开 + KQ展开）
- Cowork变更必须同步Status数据层（COMPANY_STATUS + DELTA_PROPOSALS）

## 代码规范
- 中文为主，技术术语保留英文
- 纯文件系统存储，零外部依赖
- kebab-case 用于文件名和目录名
- 研究笔记用 Markdown，结构化数据用 JSON

## UI偏好
- 小按钮，不要大按钮
- 精简直觉，信息密度优先
- 深色主题
