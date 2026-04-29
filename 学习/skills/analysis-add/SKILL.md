---
name: analysis-add
description: Use when working in the AI Org research project and an existing company report must absorb new source-note evidence without rebuilding the report or changing its established framework.
---

# Analysis Add Skill

`analysis-add` 用于“给已经写好的报告增补新材料”。它继承 `analysis2` 的核心方法：材料是根本，主线只是摆放材料的方法。但它的任务不是重新写一篇报告，而是在保留既有文章框架的前提下，把新 essence / source note 里的高价值证据块放到正确位置，再做一次顺稿。

核心原则：

```text
现有报告是承重结构，不能轻易推倒重来。
新 source note 是新的积木，必须放到最合适的位置。
增补不是附录，不是材料清单，也不是重新摘要。
高价值新证据不能无声丢失；低价值重复材料不能制造噪音。
最终正文只写公司、产品、组织、业务和风险，不写写作过程。
```

## 0. 适用场景

用 `analysis-add`：

- 用户已经认可一份报告的大框架，希望加入新 source notes。
- 新材料来自 `vault/*/essence/*_source_note.md`。
- 用户明确要求“不破坏原有文章框架”“把新 essence 加进去”“补充 YouTube / Substack / jobs 信息”。
- 旧报告整体可用，但存在细节遗漏、证据不足、quote 不够好、某些段落需要被新材料加厚。

不要用 `analysis-add`：

- 现有报告主线本身错了，需要重新写。用 `analysis2`。
- 高相关 raw transcript 还没有 source note。先用 `essence`。
- 用户要求 theme map、thesis spine、evidence map 或诊断文件。用 `analysis`。
- 新材料只适合做来源审计，不适合进入正文。

## 1. 必读

开始前读必要文件，不批量塞无关材料。

必读：

- `Agent.md`
- `progress.md`
- `core-principles-and-lessons.md`
- `project-structure.md`
- `学习/skills/analysis2/SKILL.md`
- `学习/skills/essence/SKILL.md`
- 用户指定的既有报告
- 本轮要加入的新增 source notes

按需读：

- `学习/style_references/anthropic_org_investment_style_notes_2026-04-21.md`
- 对应 raw transcript，仅用于核验可疑 quote 或补足 source note 漏洞。
- 同一来源的旧 note / duplicate note，仅用于去重判断。

## 2. 输入层

正式新增证据默认只读新版逐源笔记：

```text
companies/{slug}/vault/podcasts/essence/*_source_note.md
companies/{slug}/vault/youtube/essence/*_source_note.md
companies/{slug}/vault/substack/essence/*_source_note.md
companies/{slug}/vault/financials/essence/*_source_note.md
companies/{slug}/vault/_optional/*/essence/*_source_note.md
```

如果同一来源有旧短 `_essence.md` 和新版 `_source_note.md`，只让 `_source_note.md` 承重。旧短 essence 只能用于审计，不进入正文。

## 3. 工作流

### Step 1. 固定现有报告骨架

先完整读既有报告，建立一张临时骨架图，不默认落盘：

- 报告核心判断是什么。
- 现有章节顺序是什么。
- 每节承担哪条主线。
- 哪些地方已经有强证据，哪些地方只有概括。
- 哪些关键词和细节已经出现。

除非新证据强到改变结论，不要改报告的大标题、主线顺序和基本结构。增补的默认动作是在现有结构里加厚、合并、替换更好证据，而不是新增一整套框架。

### Step 2. 逐篇读新增 source notes

对每份新增 source note 从头读到尾，不只搜关键词。每个 evidence block 标为五类之一：

| 状态 | 含义 |
|---|---|
| 直接插入 | 新证据能独立支撑一个现有章节里的判断。 |
| 合并加厚 | 旧报告已有同类判断，但新材料提供更具体动作、数字、工具、岗位、quote 或反方。 |
| 替换证据 | 旧报告判断方向对，但新 quote 更一手、更长、更能承重。 |
| 边界/待核验 | 新材料不适合做正向结论，但能补风险、来源偏差或反方。 |
| 不纳入 | 重复、低相关、证据弱、偏离报告问题。 |

这个清单可以只存在于工作上下文里。不要默认写成新的 analysis 文件，除非用户要求审计轨迹。

### Step 3. 给每块新证据找位置

每个“直接插入 / 合并加厚 / 替换证据”的 block 必须有一个目标位置：

```text
目标章节 -> 目标小节 -> 插入在某段前后 -> 动作类型
```

优先放进现有章节，不要把新增材料全部堆到文末。只有当新增材料连续形成一个原报告没有覆盖的新 storyline，且至少有两三个强 evidence blocks 支撑，才新增小节；新增大节必须非常克制。

不要写“新增 YouTube 材料”“本轮补充材料”“从新 essence 看”这类章节。正式读者只需要看到公司事实和判断，不需要看到写作过程。

### Step 4. 像拼积木一样改正文

增补时优先保留 source note 的证据块：

- source note 的判断段可以轻微顺稿，但不要压缩成抽象摘要。
- source note 的中文译引可以直接使用；如果太短、太转述、太像上一段复述，回 source note 或 transcript 修。
- 已有段落和新证据重复时，合并为一个更具体的段落，保留更强的事实和 quote。
- 新证据只是在旧判断旁边补一个例子时，不要开新小节；把它自然写进原段落或原小节。
- 如果新证据推翻旧判断，不要悄悄改结论；在正文或待核验问题里写清楚冲突和需要验证的地方。

增补不是越多越好。低价值重复材料会削弱报告。真正要加入的是能提高解释力的动作、数字、工具、岗位、流程、用户反馈、竞争判断和风险。

## 4. 写作规则

继承 `analysis2` 的文风，并额外强调“增补不能露出工程痕迹”。

必须做到：

- 正文直接讲企业怎么做、产品怎么变、组织怎么运行、风险在哪里。
- 每节开头如被明显加厚，要补一段总起，让读者知道本节现在为什么这样展开。
- 每段只推进一个判断，信息密度不要过高；宁可把自然段写完整一点。
- 读者默认看不到后文，所以专有名词首次出现要解释。
- 中文优先，但不硬翻行业专有词。Lovable、Linear、FigJam、roadmap、demo、workflow、PMF、GTM、AI-native、vibe coding、Minimum Lovable Product 等自然保留。
- 一句话里英文过多时，把普通词改回中文；翻成中文会别扭或损失语气的专有词保留英文。
- 引用使用 source note 的较长中文译引，尽量保留第一人称和现场语气。

避免：

- “某某说 / 某某认为 / 某某觉得 / 某某指出”作为正文推进方式。引用署名放在 quote 后面即可。
- “新材料显示 / source note 里提到 / 这一版补充 / 上一版遗漏 / 本轮重新阅读 / 报告质量”这类写作过程痕迹。
- 把新增材料写成附录、清单或素材堆。
- 为了顺滑删掉具体工具、招聘仪式、岗位变化、数字、失败模式和反方。
- 把 analyst paraphrase 放进引号里。引号里只能是来源本人表达的意思。

好的写法：

```markdown
Lovable 用 Linear 跟踪人才申请，这个细节说明早期团队并没有急着把每个职能都拆成一套专门系统。少数通用工具承担了产品、工程和招聘的协调任务，减少了切换成本，也让小团队在信息很密的状态下保持速度。
```

不要写：

```markdown
新 YouTube essence 补充说，Anton 提到他们用 Linear 做人才申请跟踪，这说明上一版漏掉了工具层细节。
```

## 5. 引用规则

引用是证据，不是装饰。

- 使用 source note 里的中文译引；不要把一条长引用拆成几个短 bullet。
- quote 要支撑当前段落里的事实或机制，不能只是重复上一段判断。
- 多人对话可以保留必要上下文，但引号里要尽量呈现“我 / 我们 / 你”的一手表达。
- 不要把主持人旁白、分析者总结或“某某回应说”写进引号里。
- 署名格式沿用既有报告：

```markdown
> “……” —— Anton Osika, Lenny's Podcast, 2025-03-09
```

如果新增 source note 的 quote 不合格，先修 source note 或回 raw transcript 核验，再进入报告。

## 6. 输出策略

默认优先保留原报告文件，另存一个新版本：

```text
companies/{slug}/analysis/{ExistingReportStem}_updated_{YYYY-MM-DD}.md
```

如果用户明确说“就改这份文档”“添加进之前写的总结文档里”，可以直接编辑指定报告；但必须保留原框架，并在交付时说明改动集中在哪些章节。

不要默认生成 theme map、thesis spine、evidence map、addendum plan 等脚手架文件。除非用户明确要求看过程，只交付增补后的报告。

## 7. 完成检查

交付前必须做：

- 检查所有新增高价值 evidence blocks 是否进入报告，或有明确不纳入理由。
- 搜索新增 source notes 的高价值关键词，确认没有被抽象吞掉。按公司材料自定义关键词；Lovable 常查：`Linear`、`FigJam`、`工作模拟`、`每周计划`、`demo`、`office`、`lunch`、`security`、`enterprise`、`growth`、`retention`。
- 搜索正式报告，清掉过程痕迹：`上一版`、`本轮`、`新材料`、`source note`、`essence`、`报告质量`、`重新阅读`。
- 搜索正文中的“说 / 认为 / 觉得 / 指出 / 提到”，判断是否是访谈转述腔；必要时改成直接公司动作。
- 检查新增 quote 是否是真实一手译引，不是第三人称摘要。
- 检查新增英文是否必要；保留专有词，普通词改中文。
- 看 diff，确认没有大幅删除既有高价值内容，没有无意改坏标题层级和章节顺序。

完成汇报只说结果：新增了哪些 source notes、主要补进哪些章节、哪些材料因重复或低相关没有进入、是否还存在待核验问题。
