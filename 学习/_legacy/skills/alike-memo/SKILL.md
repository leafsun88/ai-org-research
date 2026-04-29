---
name: alike-memo
description: |
  Alike Score核心评分技能。基于D1-D7统一框架评估组织生成力，Old Friends作为校准锚点而非模板。

  核心理念："学我者生，似我者死"——衡量的不是"像不像Netflix"，而是"有没有Netflix那种发明自己范式的能力"。

  触发场景：
  - /alike流程自动调用（L2层）
  - 用户说"给XX打alike分"、"评估XX的组织生成力"
  - 用户说"alike-memo XX"

  不触发：
  - 只想看组织深度分析（→ winner-pattern-org）
  - 只想看投资判断（→ investment-memo）
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
  - WebSearch
  - WebFetch
---

# Alike Memo：D1-D7组织生成力评分

## 核心定位

Alike Score回答一个问题：**这家公司有多强的组织生成力（organizational generative capacity）？**

不是"像不像某个Old Friend"，而是"有没有能力发明属于自己的组织范式"。
Old Friends是校准锚点——我们知道Netflix的D3=5/5长什么样（Keeper Test），所以能判断其他公司的D3是几分。

## 输入

```
/alike-memo TICKER
```

## 数据来源（按优先级）

1. **校准矩阵**：`vault/old-friends/_calibration.json`（D1-D7各维度的5/5标杆）
2. **采集数据**：`vault/companies/{slug}/discovery/`（全部raw数据）
3. **已有分析**：`vault/companies/{slug}/leadership/`、`org/`（如有CEO档案、组织分析）
4. **Old Friend档案**：`vault/old-friends/{name}/profile.md`（校准参照）
5. **winner-pattern-org知识库**：`skills/winner-pattern-org/references/org_patterns.md`（案例库）

## 评分框架：D1-D7 + Fit Score

### 统一权重（所有公司、所有实验一致）

| 维度 | 权重 | 衡量什么 |
|------|------|---------|
| D1 CEO认知质量 | 20% | 第一性原理思考 + 长期主义 + 认知迭代速度 |
| D2 Key Leader深度 | 15% | 关键岗位人才质量 + CEO以外的组织厚度 |
| D3 考核激励机制 | 15% | 是否有A类机制驱动正确行为（如Keeper Test, 四不政策） |
| D4 信息架构 | 10% | 决策信息如何流动 + 组织透明度 |
| D5 组织熵减能力 | 10% | 对抗组织膨胀/官僚化的能力 |
| D6 Talent Density | 15% | 人才密度 + 招聘标准 + 人效指标 |
| D7 Key Bet质量 | 15% | 关键战略赌注的质量 + 执行力 |
| **Fit Score** | **独立** | 组织形态与业务本质的适配度（不参与加权） |

### 评分标尺（1-5分，参照校准锚点）

```
5/5 = 该维度的教科书级表现（Old Friend中的顶尖水平）
4/5 = 明显高于行业平均，有独特机制
3/5 = 行业平均水平，无特别突出也无明显短板
2/5 = 低于行业平均，有可识别的弱点
1/5 = 严重缺陷，对公司构成威胁
⛔ = 信息不足，拒绝打分
```

**关键规则：信息不足时必须⛔拒绝打分，绝不硬打。**

## 执行流程

### Step 0: 业务本质画像

在打分之前，先回答：**这家公司在造什么？它的业务本质决定了什么样的组织形态是理想的？**

```markdown
## 业务本质
{一段话：业务核心是什么、价值创造逻辑是什么}

## 理想组织形态
{基于业务本质推导：这样的业务需要什么样的组织？}
{例：高频交易需要极扁平+高自动化；内容平台需要创意自由+数据纪律并存}
```

这决定了Fit Score的评判标准——不同业务的理想组织形态不同。

### Step 1: D1-D7逐维度评分

对每个维度：

```markdown
### D{N} {维度名} — {X}/5

**校准参照**：{Old Friend}的{person/mechanism} = 5/5
**关键证据**：
- [S?] {具体证据，标注信源等级}
- [S?] {具体证据}

**评分理由**：{为什么给这个分，与校准锚点的对比}

**信息充分度**：{充分/部分/不足}
```

### Step 2: Fit Score

```markdown
## Fit Score: {X}/5

Step 0定义的"理想组织形态" vs 实际D1-D7表现的匹配度。

**匹配点**：{哪些维度的表现恰好是这个业务需要的}
**错配点**：{哪些维度的表现与业务需求不匹配}
**判断**：{组织设计是否服务于业务本质，还是在模仿其他公司}
```

### Step 3: 生成力判断

这是Alike Memo区别于普通org分析的核心：

```markdown
## 组织生成力判断

**这家公司有没有"发明自己范式"的能力？**

证据：
1. {是否有A类原创机制（不是从别人那里学来的）}
2. {CEO是否展示过认知迭代能力（改变自己的想法）}
3. {面对危机时是否产生了组织创新（而非退回标准做法）}

**Most Resonant Old Friend**: {哪个Old Friend在生成力模式上最共振}
**共振原因**: {一句话——不是"做了相似的事"，而是"有相似的生成力"}
```

### Step 4: 输出Alike Memo

```markdown
---
company: {name}
ticker: {TICKER}
alike_score: {加权总分，转换为100分制}
fit_score: {X}/5
d_scores: {d1: X, d2: X, d3: X, d4: X, d5: X, d6: X, d7: X}
most_resonant_old_friend: {name}
calibration_version: "2.0"
date: {YYYY-MM-DD}
info_gaps: [{缺信息的维度}]
---

# {Company} — Alike Memo

## Alike Score: {score}/100 | Fit: {X}/5

## 一句话结论
{这家公司的组织生成力处于什么水平，最大的亮点和最大的短板}

## 业务本质 → 理想组织
{Step 0}

## D1-D7 评分矩阵
| 维度 | 得分 | 校准锚点 | 关键证据 | 信息充分度 |
|------|------|---------|---------|-----------|
| D1 CEO认知 | X/5 | {anchor} | {evidence} | ✅/⚠️/⛔ |
| D2 Key Leader | X/5 | ... | ... | ... |
| D3 考核激励 | X/5 | ... | ... | ... |
| D4 信息架构 | X/5 | ... | ... | ... |
| D5 组织熵减 | X/5 | ... | ... | ... |
| D6 Talent Density | X/5 | ... | ... | ... |
| D7 Key Bet | X/5 | ... | ... | ... |

## Fit Score: {X}/5
{Step 2}

## 组织生成力
{Step 3}

## 信息缺口
{哪些D维度缺乏S3+信源，下一步采集建议}
```

## 存储

- 输出路径：`vault/companies/{slug}/scoring/alike-memo.md`
- 同步更新：`vault/_index.json`（alike_score字段）

## 质量标准

1. **必须先做Step 0** — 没有业务本质画像不能打分
2. **校准锚点必须引用** — 每个D维度都要说明"5/5长什么样"
3. **信息不足=⛔** — 绝不猜测打分
4. **生成力 > 相似度** — 评的是"能力"不是"外观"
5. **Fit Score独立** — 不被D1-D7平均分影响
6. **一个公司一个分** — 不因Old Friend不同而产生不同分数
