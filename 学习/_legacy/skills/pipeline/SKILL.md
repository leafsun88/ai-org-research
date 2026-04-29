---
name: pipeline
description: |
  投研Pipeline编排器（v2）。四层架构：采集→评分→拐点→投资决策。
  已被/alike skill替代为主入口，pipeline作为底层编排逻辑保留。

  触发场景：
  - 被/alike自动调用
  - 用户说"pipeline XX"、"全流程研究XX"

  不触发：
  - 用户说"研究下XX"（→ /alike，更简洁的入口）
  - 用户只想做单一维度
context: fork
model: opus
effort: high
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
  - Agent
  - TodoWrite
  - WebSearch
  - WebFetch
  - Skill
---

# Pipeline v2：四层投研编排器

## 核心架构

```
L1: 数据采集（Duolingo级别详尽度）
  ↓ 自动
L2: Alike Score（D1-D7统一评分 + Fit Score）
  ↓ Top30自动触发
L3: Inflection分析（组织拐点 + 业务拐点）
  ↓ 有催化剂 + 用户确认
L4: Investment Memo（估值、认知差、买入逻辑）
```

## 投资哲学（不可变）

- 好组织 + 好Timing = 好投资
- 组织先于战略，战略先于业务，业务先于财务
- 组织变化 → 战略变化 → 业务结果 → 股价反映，时间差 = 投资窗口
- "学我者生，似我者死" — 衡量生成力，不是相似度

## Vault路径

```
vault/companies/{slug}/
  ├── discovery/          ← L1产出（raw采集数据）
  ├── leadership/         ← CEO认知档案
  ├── org/                ← 组织深度分析（winner-pattern-org）
  ├── scoring/            ← L2-L4产出
  │   ├── alike-memo.md        ← D1-D7 + Fit Score
  │   ├── org-inflection.md    ← 组织拐点（Top30）
  │   ├── biz-inflection.md    ← 业务拐点（Top30）
  │   └── investment-memo.md   ← 投资决策（最终候选）
  ├── fundamental/        ← 财务/业务分析
  ├── exec-voice/         ← 高管原声
  ├── employee/           ← 员工视角
  ├── red-team/           ← 反方论证
  ├── intel/              ← 竞争情报
  ├── transcripts/        ← 电话会/访谈转录
  └── notes/              ← 研究笔记/杂项
```

## Old Friends校准

```
vault/old-friends/
  ├── _calibration.json   ← D1-D7校准矩阵
  ├── applovin/profile.md
  ├── netflix/profile.md
  └── pdd/profile.md
```

所有评分参照 `_calibration.json`，不因Old Friend不同产生不同分数。

---

## L1: 数据采集

### 目标
达到Duolingo级别的信息详尽度（55+ discovery文件）

### 执行
调用 `/collect TICKER [CompanyName]`，内部并行调度：
- deepsearch（8维度深度搜索）
- founder（创始人动态）
- org-scan（组织穿透扫描）
- signals-scan（每日信号）
- social-search（社交媒体）
- guru（投资大师持仓）

### 补充采集（非上市）
- private-search（非上市公司专用）

### 产出
- `vault/companies/{slug}/discovery/sources/` — 各类raw数据
- `vault/companies/{slug}/discovery/financials/` — 财务数据

### 完成标准
- discovery/目录下至少有6类数据源
- 核心信源（CEO访谈、财报、组织架构）必须有S3+级别数据

---

## L2: Alike Score

### 目标
基于D1-D7统一框架评估组织生成力

### 执行
调用 `/alike-memo TICKER`

### 前置
- L1采集数据存在
- `vault/old-friends/_calibration.json` 存在

### 执行逻辑
1. Step 0: 业务本质画像
2. D1-D7逐维度评分（参照校准锚点）
3. Fit Score（组织-业务适配度）
4. 生成力判断 + Most Resonant Old Friend标签

### 产出
- `vault/companies/{slug}/scoring/alike-memo.md`
- 更新 `vault/_index.json`（alike_score字段）

### 分流
- Alike Score进入当前Top30 → 自动进入L3
- 未进Top30 → 输出摘要结束，提示/vault-save

---

## L3: Inflection分析

### 目标
识别组织拐点和业务拐点，判断Timing

### 触发条件
- Alike Score进入vault当前Top30
- 或用户手动 `/org-inflection TICKER`

### 执行
并行启动2个分析：

**Agent A: 组织拐点**
调用 org-inflection-memo 逻辑：
- 近期是否有CEO变更、重组、文化转型？
- 组织变化是否会导致D1-D7分数在6-12个月内显著变化？
- 产出 → `scoring/org-inflection.md`

**Agent B: 业务拐点**
调用 biz-inflection-memo 逻辑（ABCD四层）：
- A=Asset Quality（资产质量变化）
- B=Engine Switch（增长引擎切换）
- C=Valuation Safety（估值安全边际）
- D=Catalyst（催化剂识别）
- 产出 → `scoring/biz-inflection.md`

### 分流
- 有明确催化剂（org或biz层面）→ 提示用户确认后进入L4
- 无明确催化剂 → 标记为WATCH，输出摘要结束

---

## L4: Investment Memo

### 目标
最终投资决策文档

### 触发条件
- L3发现催化剂 + 用户确认
- 或用户手动 `/investment-memo TICKER`

### 执行
读取该公司vault全部研究数据，生成投资备忘录：

1. **组织穿透章节**（30%+篇幅）— 来自alike-memo + org/
2. **业务分析**（20%）— 来自fundamental/ + discovery/
3. **拐点与催化剂**（20%）— 来自scoring/inflection
4. **估值与认知差**（15%）— 市场定价 vs 组织价值的差距
5. **风险与反方论证**（15%）— 来自red-team/

### 产出
- `vault/companies/{slug}/scoring/investment-memo.md`
- Signal Engine决策矩阵标签：AUTO-APPLY / PROPOSAL / WATCH / DISCARD

### 5项交叉验证
1. 组织评分 vs 财务表现：是否一致？
2. CEO认知 vs 实际执行：说到做到？
3. 员工口碑 vs 官方叙事：内外一致？
4. 历史Key Bet vs 当前Key Bet：进化了还是退化了？
5. 市场定价 vs 组织价值：被低估还是高估？

---

## 智能跳过规则

Pipeline启动时检查vault中该公司各层的最新文件日期：
- **已有且<7天**：跳过，提示"已有最新（{date}）"
- **已有但7-30天**：默认跳过，标记"可选更新"
- **已有但>30天**：建议更新
- **未覆盖**：必须执行
- **--refresh参数**：忽略所有，全量重跑

---

## 进度展示

```
Alike Pipeline: CrowdStrike (CRWD)

L1 采集: ✅ 完成（12个数据源）
L2 评分: ✅ Alike Score 81 | Fit 4/5 | Resonant: Netflix
L3 拐点: 🔄 org-inflection进行中...
         ⏳ biz-inflection排队中
L4 决策: ⏳ 等待L3完成
```
