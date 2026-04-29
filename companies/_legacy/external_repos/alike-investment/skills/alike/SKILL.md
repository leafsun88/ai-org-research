---
name: alike
description: |
  一键触发完整Alike研究流程。自动判断公司当前进度，从正确的层级开始执行。

  触发场景：
  - 用户说"alike研究下XX"、"研究下XX"、"看看XX"
  - 用户说"alike XX"、"/alike XX"
  - 用户给出公司名+研究意图

  不触发：
  - 用户只想查已有研究（→ vault-search）
  - 用户明确指定单个skill（如"帮我做XX的org穿透"）
  - 用户只想看排名/清单（→ vault-status）
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

# Alike：一键投研入口

## 核心理念

一句话触发，自动走完全流程。用户不需要记住进度，系统自动判断从哪里开始。

## 输入

```
/alike TICKER [CompanyName]
```

- TICKER：股票代码（如APP, CRWD）或公司名（如ByteDance）
- CompanyName：可选，首次研究时用于创建目录

示例：
- `/alike CRWD`
- `/alike ByteDance 字节跳动`
- `alike研究下Stripe`

## 执行流程

### Step 0: 路由判断

1. 查 `vault/_index.json` 的 `ticker_map`，获取slug
   - 不存在 → 新公司，创建条目，从L1开始
   - 存在 → 检查已有数据深度

2. 检查已有层级：
   ```
   vault/companies/{slug}/
     discovery/  → L1已完成？
     scoring/
       alike-memo.md → L2已完成？
       org-inflection.md + biz-inflection.md → L3已完成？
       investment-memo.md → L4已完成？
   ```

3. 路由决策：
   - 无discovery/ → 从L1开始（全量采集+评分+拐点+投资决策）
   - 有discovery/ 无alike-memo → 从L2开始
   - 有alike-memo 无inflection → 检查是否进入Top30，是→L3，否→完成
   - 全部完成 → 提示"已完成研究，要刷新吗？"

### Step 1 (L1): 大规模数据采集

**目标**：Duolingo级别的信息详尽度

并行启动采集agents：
- `/collect TICKER` — 一键全量采集（内部调度deepsearch + founder + org-scan + signals-scan + social-search + guru）

采集完成后自动进入L2。

### Step 2 (L2): Alike Score — D1-D7组织生成力评分

**调用 `/alike-memo TICKER`**

这是核心评分层：
- 读取 `vault/old-friends/_calibration.json` 获取校准锚点
- 读取 `vault/companies/{slug}/discovery/` 全部采集数据
- 读取 `vault/companies/{slug}/leadership/`、`org/` 已有分析（如有）
- 按D1-D7统一维度+权重评分
- 产出 `vault/companies/{slug}/scoring/alike-memo.md`

### Step 3 (L3): Inflection分析

**触发条件**：Alike Score进入当前vault Top30

并行启动：
- `/org-inflection TICKER` → `scoring/org-inflection.md`
- `/biz-inflection TICKER` → `scoring/biz-inflection.md`

如果不在Top30，跳过L3/L4，输出摘要结束。

### Step 4 (L4): Investment Memo

**触发条件**：L3发现明确催化剂（org-inflection或biz-inflection中有active catalyst）

**需用户确认后执行**：
```
"CrowdStrike Alike Score 81（Top 5），发现组织拐点：July 2024危机后组织韧性验证。
是否生成Investment Memo？"
```

用户确认 → `/investment-memo TICKER` → `scoring/investment-memo.md`

## 输出摘要

无论在哪一层结束，都输出一段摘要：

```markdown
## {Company} Alike研究完成

**Alike Score**: 81/100（D1=4.5, D2=3.5, D3=4, D4=3, D5=3.5, D6=4, D7=4.5）
**Fit Score**: 4/5
**Most Resonant Old Friend**: Netflix（危机验证+组织韧性共振）
**当前排名**: #5 / 74家
**Inflection**: 🟢 org-inflection detected | 🟡 biz-inflection pending
**文件**: vault/companies/crowdstrike/scoring/

提示：/vault-save 保存到Git
```

## 批量模式

```
/alike CRWD KVYO MDB SentinelOne
```

自动为每家公司启动独立agent并行处理。

## 刷新模式

```
/alike CRWD --refresh
```

忽略已有数据，全量重跑L1-L4。
