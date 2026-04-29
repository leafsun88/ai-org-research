# AI Org 研究 — Skill 速查指南

> 当前主路径收敛为：`collect -> essence -> analysis`。旧 D1-D7 / 分散抓取 skill 已归档到 `学习/_legacy/skills/`，不再默认调用。

## 主路径

```text
L0: config/company_targets.json
L1: /collect  -> companies/{slug}/_staging/ -> companies/{slug}/vault/
L2: /essence  -> companies/{slug}/vault/{source}/essence/
L3: /analysis -> companies/{slug}/analysis/
```

## Active Skills

| Skill | 什么时候用 | 主输入 | 主输出 |
|---|---|---|---|
| `/collect` | 开始或修复公司采集；默认只抓 podcast / financials / Substack / YouTube | TARGET_KEY | `companies/{slug}/vault/` |
| `/essence` | 把 transcript / article / report 逐条压成可分析的 insight blocks | TARGET_KEY 或 source_path | `companies/{slug}/vault/{source}/essence/` |
| `/analysis` | 把 vault / essence 变成 source inventory、evidence map、fact pack、复杂报告、一页分析、500 字版 | TARGET_KEY | `companies/{slug}/analysis/` |

## Legacy Skills

位置：

```text
学习/_legacy/skills/
```

旧 skill 不删除，但默认不调用：

- `alike` / `alike-memo` / `winner-pattern-org`：旧 D1-D7 评分。当前已把核心视角并入 `/analysis`。
- `pipeline`：旧流水线入口，和当前主路径重叠。
- `founder` / `org-scan` / `private-search` / `social-search` / `deepsearch` / `guru` / `signals-scan`：旧分散抓取或专题入口。
- `transcript-critic`：单个音视频处理。
- `vault-*`：旧 vault 支撑工具。

## 标准研究流程

### Step 1. Target

```bash
python3 scripts/discovery/collect_target.py TARGET_KEY --dry-run
```

如果 target 不存在，先更新：

```text
config/company_targets.json
```

### Step 2. Collect

```bash
python3 scripts/discovery/collect_target.py TARGET_KEY --channels all
```

`all` 只表示：

```text
podcasts / financials / substack / youtube
```

最大化抓取才用：

```bash
python3 scripts/discovery/collect_target.py TARGET_KEY --channels all_sources
```

### Step 3. Essence

每条高相关 source 抓完后，使用 `学习/skills/essence/SKILL.md` 生成对应 essence：

```text
companies/{slug}/vault/podcasts/essence/
companies/{slug}/vault/youtube/essence/
companies/{slug}/vault/substack/essence/
companies/{slug}/vault/financials/essence/
```

### Step 4. Analysis

脚本只稳定生成前两类：

```text
companies/{slug}/analysis/{Company}_source_inventory_{date}.md
companies/{slug}/analysis/{Company}_evidence_map_{date}.md
```

agent 写作流程生成：

```text
companies/{slug}/analysis/{Company}_fact_pack_{date}.md
companies/{slug}/analysis/{Company}_AI组织复杂报告_{date}.md
companies/{slug}/analysis/{Company}_一页分析_{date}.md
companies/{slug}/analysis/{Company}_500字提交版_{date}.md
```

## 当前关键文件

- 项目规范：`Agent.md`
- 当前状态：`progress.md`
- 稳定经验：`core-principles-and-lessons.md`
- 路径说明：`project-structure.md`
- 流程图：`companies/_meta/workflows/collect_analysis_flow_2026-04-21.html`
