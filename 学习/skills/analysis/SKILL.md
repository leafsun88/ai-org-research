---
name: analysis
description: Use when turning company essence files into detailed analysis markdown under companies/{slug}/analysis, especially long complex reports, fact packs, evidence maps, and organization/investment analysis.
argument-hint: TARGET_KEY
---

# Analysis Skill

`analysis` 负责把 `companies/{slug}/vault/*/essence/` 里的材料转成 `companies/{slug}/analysis/` 里的研究文档。它不负责抓取；抓取用 `学习/skills/collect/SKILL.md`。
如果高相关 transcript 还没有 source-level essence，先用 `学习/skills/essence/SKILL.md` 补齐。

自动脚本只稳定生成两类轻量 analysis：

- `source_inventory`
- `evidence_map`

fact pack、复杂报告、一页分析是研究写作流程，由 agent 读 essence 后写入 markdown。除非用户明确要求，不再默认写 500 字短文。

## 0. Pre-Analysis Protocol

正式分析前先读：

- `Agent.md`
- `progress.md`
- `core-principles-and-lessons.md`
- `project-structure.md`
- `学习/skills/collect/SKILL.md`
- `学习/skills/essence/SKILL.md`
- `学习/org-as-alpha/`
- `学习/old-friends/`
- `学习/style_references/anthropic_org_investment_style_notes_2026-04-21.md`
- `学习/style_references/anthropic_org_investment_style_reference_2026-04-21.md`
- `companies/{slug}/analysis/{Company}_org_block_report_*_recovered.md`（如果存在；用于校准本公司报告的人话风格）
- `学习/_legacy/skills/alike/SKILL.md`
- `学习/_legacy/skills/alike-memo/SKILL.md`
- `学习/_legacy/skills/winner-pattern-org/SKILL.md`

默认主问题仍然是 AI org 三问：

- Founder 对 AI 组织有什么独到见解？
- Founder 在 AI 组织落地上做了哪些具体动作？
- AI 组织的变革对业务有何影响？

所有组织/AI org 报告都必须围绕这三问展开。三问要放在正式报告最前面，作为文章总纲，而不是放到文末当总结。先把业务本质、Founder world model、组织动作、业务结果的传导链想清楚，再用三问开篇压住全文。

组织相关内容至少占正式报告 70%。商业模式、收入、估值、竞争、产品功能都可以写，但必须服务组织主线，并放在组织机制之后。不要让商业模式综述、增长数字或竞争格局抢走报告主体。

## 1. Paths

先定位 target：

```bash
python3 scripts/discovery/collect_target.py TARGET_KEY --dry-run
```

核心输入：

```text
companies/{slug}/vault/podcasts/essence/
companies/{slug}/vault/youtube/essence/
companies/{slug}/vault/substack/essence/
companies/{slug}/vault/financials/essence/
```

运行状态只在需要排查时看：

```text
companies/{slug}/_staging/sources/**/metadata/
companies/{slug}/_staging/sources/**/transcripts/
```

正式写分析只读 essence。raw transcript / article / report 只在 essence 明显缺证据、quote pack 可疑、或用户要求核验时打开，不作为报告默认输入。

## 2. Script Map

| 产物 | 入口 | 输出 |
|---|---|---|
| source inventory | `scripts/discovery/collect_target.py` | `companies/{slug}/analysis/*source_inventory*.md` |
| evidence map skeleton | `scripts/discovery/collect_target.py` | `companies/{slug}/analysis/*evidence_map*.md` |
| transcript essence queue | `scripts/discovery/build_transcript_essence_queue.py` | `companies/_meta/transcripts/_transcript_essence_queue_*.json/md` |
| fact pack | agent 写作流程 | `companies/{slug}/analysis/{Company}_fact_pack_{date}.md` |
| complex report | agent 写作流程 | `companies/{slug}/analysis/{Company}_AI组织复杂报告_{date}.md` |
| one-page report | agent 写作流程 | `companies/{slug}/analysis/{Company}_一页分析_{date}.md` |
| detailed complex report | agent 写作流程 | `companies/{slug}/analysis/{Company}_complex_report_{date}.md` |

## 3. Analysis Flow

### Step 1. Inventory

如果 source inventory / evidence map 不存在或明显过期：

```bash
python3 scripts/discovery/collect_target.py TARGET_KEY --channels all --skip-transcript
```

`all` 只跑四块：podcast / financials / Substack / YouTube。

### Step 2. Source Quality Gate

写正文前先看 status：

```text
companies/{slug}/_staging/sources/podcasts/transcripts/_podcast_transcription_status.json
companies/{slug}/_staging/sources/podcasts/transcripts/_podcast_transcription_failures.json
companies/{slug}/_staging/sources/youtube/metadata/_youtube_collection_status.json
companies/{slug}/_staging/sources/youtube/metadata/_youtube_rejected_candidates.json
companies/{slug}/_staging/sources/substack/metadata/_collection_status.json
companies/{slug}/_staging/sources/substack/metadata/_collection_failures.json
```

真实失败很多时，先回到 collect 补抓，不要急着写大报告。

### Step 3. Essence Coverage Gate / Full Essence Pass

```bash
find companies/{slug}/vault -path '*essence*' -type f | sort
```

如果高相关 transcript 没有 essence，先按 `学习/skills/essence/SKILL.md` 补 essence。分析不能绕过 essence 层。

分析前生成 essence coverage 清单：

```bash
find companies/{slug}/vault -path '*/essence/*.md' -type f | sort
```

如果 evidence 主要来自 transcript 原文而不是 essence，停止写作，先回到 essence。

正式复杂报告前必须通读该公司所有相关 essence。这里的“通读”最低标准是：逐份读 frontmatter、标题、每个 insight block 的判断段和 quote pack；高权重 source 需要读完整 essence；弱 source 也要看完标题、判断段和 quote 后做降权，而不是跳过。不能只读几份核心 podcast 后开始写，也不能只靠关键词搜索拼材料。

通读后先做 source weighting：

```text
A 层：能承重的主证据，通常是 founder/operator 原声、客户/竞品/投资人深度材料、带完整 quote pack 的高相关 essence。
B 层：边界校准，通常是教程、用户案例、重复访谈、现场观察、弱 quote 的 YouTube essence。
C 层：缺口或低置信材料，不能支撑主判断，只能放进待核验或下一轮采集。
```

正式报告只能让 A 层证据承重；B 层可以补边界和反方；C 层只能暴露缺口。source weighting 可以写进 analysis 附录或 audit 文件，不要直接塞进正式报告正文。

### Step 4. Build Fact Pack

fact pack 是公司全景材料，不是观点文。默认结构：

```markdown
---
company: {Company}
type: fact_pack
date: {YYYY-MM-DD}
status: current
---

# {Company} Fact Pack

## 公司简介
## 历史发展
## 产品与商业模式
## 客户与 GTM
## 财务 / 收入 / 融资
## 行业结构与竞争格局
## 团队与组织
## 战略方向
## 关键数据表
## 已确认事实与来源
## 待核验问题
```

规则：

- 所有数字都带来源。
- 私有公司用 reported / estimated / third-party estimate 标口径。
- ARR、revenue、GMV、valuation 不混写。
- 对明显不可靠来源降权。

### Step 5. Evidence Map

把 essence 证据按主题归类：

```text
Founder 认知
组织动作
业务影响
商业模式
产品战略
GTM / enterprise
财务与融资
竞争格局
风险与反方
个人思考
```

Evidence map 不是最终报告，重点是“证据放哪里、哪些证据能支撑哪个判断”。

### Step 5.5. Insight Audit

Evidence map 之后、Alike Lens 之前，必须做一次 insight audit。目标不是再分类一次材料，而是把所有 essence 里最 sharp 的点先捞出来。很多报告“清楚但没有洞见”，常见原因就是先套了 Founder / 招聘 / 增长 / 企业化 / 风险 这类职能目录，最后每段都正确，但整篇没有回答“这家公司为什么可能不一样”。

Insight audit 的交付物不是主题表，而是一组候选机制。顺序必须是：

```text
essence 里的 sharp points -> candidate mechanisms -> thesis spine -> article architecture
```

不要反过来先定文章章节，再找材料填空。好报告的结构应该从材料里长出来，尤其要让反常识点、冲突点、具体流程、异常数字和反方证据先占住位置。后面再做压缩，而不是为了顺滑提前删掉。

先自下而上扫所有 essence：

- 读每个 essence 的标题、判断段和 quote pack。
- 摘出有反常识、具体动作、数字、真实流程、冲突、反方风险、业务传导的点。
- 不要先把材料塞进固定目录。固定目录只用作 completeness checklist，不用作最终文章骨架。
- Founder 原声优先，但第三方深度文章、客户、投资人、竞品、员工、离职人员、律师、安全专家的高质量判断也要保留。
- 不要只保留支持主线的材料。会推翻、限制或削弱主线的反方也要进入 audit，例如 source bias、客户侧缺口、指标污染、enterprise handoff、安全责任、留存质量。

Sharp point 用五个问题筛：

| 维度 | 问题 |
|---|---|
| Surprise | 这点是否和直觉不同，或者读者大概率不知道？ |
| Causal power | 它能不能解释组织为什么有效、为什么失效，或业务为什么拐弯？ |
| Falsifiability | 后续能不能被数据、客户行为、招聘变化、产品结果或竞品反例验证？ |
| Investment relevance | 它会不会改变对 TAM、收入质量、竞争格局、估值上限或风险的判断？ |
| Concreteness | 有没有具体人、流程、工具、组织动作、数字或原话支撑？ |

临时输出一个 insight audit 表，可以写在草稿或 analysis 附录里：

```markdown
| sharp point | supporting essence / source | why it matters | report placement | keep/drop |
|---|---|---|---|---|
| 软件生产权外溢：想法先变成 working prototype，再进入工程判断 | xxx_essence.md | 改变客户公司的产品流程，也解释 Lovable 自己为什么要求员工都能 build | A 类机制 | keep |
```

报告必须保留最 sharp 的点。不要为了让结构顺，把怪异但有解释力的细节删掉。对 Lovable 这类公司，waitlist / user research、prompt box / time-to-aha、Lovable Launch、token cascade、load-bearing infrastructure、benchmark 被 hack、ownership dilution 这类点，比“增长团队”“企业化”“招聘文化”这样的目录更有穿透力。

如果某个 sharp point 只出现在旧分析、style reference 或记忆里，还没有 source-level essence，不要直接塞进报告。先回到 `学习/skills/essence/SKILL.md` 把对应 source 补成正式 essence；如果暂时补不了，就在报告里标 `待补 essence`，不要伪装成已验证材料。

把 sharp points 聚成机制时，要做一层“上层框架加深”。AI org 三问是最终压缩口径，不是文章骨架。更好的框架要回答：

- 价值链哪一段被改写了？输入、生产过程、分发、信任、计费、维护，哪一环发生了迁移？
- 旧世界的默认组织假设是什么？比如工程队列、销售漏斗、专家审批、长 roadmap、职能分工。
- 这家公司用什么组织机制替代旧假设？比如谁获得了新权限，谁更靠近 ground truth，什么反馈回路变短。
- 这个机制如何传导到业务结果？比如 adoption、retention、gross margin、enterprise budget、生态供给、竞争入口。
- 同一机制在什么条件下会反噬？比如速度失控、安全事故、ownership 稀释、分发过载、指标被 hack。

一个候选机制如果只能解释“公司做了什么”，还不够深；它必须解释“为什么这件事会改变业务判断”。写作时宁可少放几个机制，也不要把章节写成完整但平的职能说明书。

做一次 omission audit：

- 用 insight audit 表反查报告大纲。
- 如果高 surprise / 高 causal power 的点没有进入主线，要写明原因。
- 如果报告大纲只剩“Founder 认知、招聘、工作方式、增长、企业化、风险”，通常说明骨架太平，需要重搭。
- 对 source bias 做备注：如果材料主要来自 Founder / 公司高管，要标出缺少客户、员工、竞品、投资人或离职人员交叉验证。
- 对“旧稿里有、正式 essence 里没有”的高价值点做 `待补 essence` 清单。不要用旧稿记忆补事实，但要把它暴露成下一轮采集任务。

### Step 5.6. Thesis / Architecture Pressure Test

落笔前，把 insight audit 压成一条 thesis spine 和 2-4 个 A 类核心机制。每个 A 类机制必须通过五个压力测试：

- 它来自多个 sharp points，而不是来自一个职能章节名。
- 它能解释业务本质或价值链变化，而不只是描述组织动作。
- 它能容纳正反证据，不是 founder 叙事的复述。
- 它能推出组织动作、产品动作和业务影响之间的因果链。
- 如果删除这个机制，文章的核心判断会塌掉。

对每个 A 类机制写四行草稿：

```markdown
### 机制名
- underlying shift：价值链或组织假设哪里变了？
- org expression：公司用什么组织动作承接这个变化？
- business consequence：它影响 adoption / retention / revenue quality / competition 的哪一段？
- falsifier：什么客户行为、财务数据、产品事故、竞品动作或招聘变化会推翻它？
```

只有过了这一步，再决定文章章节。章节顺序要服务因果，而不是服务资料归档。常见顺序可以是：

```text
业务本质变化 -> 核心机制 -> 组织动作 -> 业务结果 -> 反方与待验证
```

也可以是：

```text
从用户工作流变化写起 -> 写公司内部如何镜像这种变化 -> 写规模化后如何保持可控 -> 写收入质量和竞争反方
```

反过来，以下结构默认需要重搭，除非用户明确要 fact pack：

- Founder 认知 / 招聘 / 工作方式 / 增长 / 企业化 / 风险。
- 产品 / GTM / 团队 / 融资 / 风险。
- 逐条 essence 摘要。

这些结构可以当 completeness checklist，不能当复杂报告的主骨架。

### Step 6. Alike Lens

复杂报告前先跑 Alike / Winner Pattern 组织投资镜头。这里不默认机械打分，目的是让报告有判断骨架。

参考旧 skill 的三个核心思想：

- `alike`: 自动路由不是重点，重点是 L1 采集、L2 组织生成力、L3 拐点、L4 投资 memo 的层级意识。
- `alike-memo`: 先回答业务本质和理想组织，再看 D1-D7；信息不足就 `⛔`，不硬打。
- `winner-pattern-org`: 组织是业务的函数；先识别 2-3 个 A 类核心机制，再写 B 类支撑机制。

必须先回答：

```markdown
## 业务本质
这家公司在造什么？输入是什么，输出是什么，价值创造的关键环节在哪里？

## 理想组织形态
这种业务天然需要什么样的组织？小队速度、强销售、研究突破、平台生态、现场部署、递归自进化，哪一个更关键？

## 实际组织形态
Founder、key leaders、招聘、绩效、信息流、工具链、决策 cadence、资源投向实际长成了什么样？

## 组织-业务适配
实际组织有没有加速业务本质？哪些机制是核心因果，哪些只是有趣但不关键？
```

然后把 insight audit 里的 sharp points 上升成 2-4 个 A 类核心机制，再写 B 类支撑机制。A 类机制必须能解释业务本质，B 类机制只解释 A 类为什么能运转。

可以这样思考：

- A 类机制：如果没有它，公司故事会明显变弱，甚至不成立。
- B 类机制：招聘、文化、工具、流程、销售、社区等支撑动作。
- 反方机制：同一套动作在哪些条件下会变成风险。

不要把职能分类误当成 A 类机制。比如“招聘很特殊”“增长很强”“企业化在推进”通常只是 B 类机制；更深的 A 类机制应该回答它们共同服务什么业务变化。以 Lovable 为例，可能的 A 类机制是：

- 软件生产权外溢：从 PRD / meeting 进入 working prototype。
- Builder density loop：生成供给增加后，社区、Launch、分享和早期用户反馈变成第二增长引擎。
- 组织镜像产品：客户要成为 builder，员工也必须把 build 当作基本动作。
- 可控地快：速度是优势，focus、ownership、security、eval 和 enterprise handoff 用来防止速度失控。

这些例子只是示范，不是模板。每家公司都要从自己的 essence 里长出机制。

D1-D7 只作为思考维度，除非用户要求，不写机械分数：

| 维度 | 分析问题 |
|---|---|
| D1 Founder / CEO cognition | Founder 是否从业务本质倒推组织？ |
| D2 Key leader depth | CEO 之外，关键产品、工程、GTM、研究、运营负责人能否独立承重？ |
| D3 Incentive / selection | 招聘、绩效、晋升、淘汰机制在奖励什么行为？ |
| D4 Information architecture | 用户、客户、模型、销售、一线执行的 ground truth 怎么进入决策？ |
| D5 Entropy reduction | 组织如何对抗膨胀、会议、审批、层级和慢？ |
| D6 Talent density | 最好的人是谁，为什么愿意来，人才密度有没有随规模上升？ |
| D7 Key bet | 公司资源是否压在最重要的一两个赌注上？ |

再做两个判断：

```markdown
## Fit Score（文字判断即可）
组织形态和业务本质的适配度：高 / 中 / 低。说明原因。

## Most Resonant Old Friend
最像哪个 old friend 的生成力模式？重点写共振机制，不写表面相似。
```

最后压回 AI org 三问。

如果信息不足，写 `⛔ 信息不足`。不要用 PR、官网价值观或单条 founder quote 硬推 D3 / D6 / key leader 结论。

### Step 7. Complex Report

复杂报告默认从 essence coverage、fact pack 和 evidence map 开始，不从空白页开始。

正式落笔前，先写一条 5-10 个 bullet 的 thesis spine。这个 spine 来自 insight audit，不来自职能目录。它要回答：

- 这家公司真正改变了哪条价值链？
- Founder 的独到判断在哪里，和旧世界的组织假设有什么差异？
- 哪几个 A 类机制在驱动业务结果？
- 哪些 B 类动作支撑这些机制？
- 哪些反方能证伪这套判断？

如果写出来的 spine 只是“Founder 认知、招聘、工作方式、增长、企业化、风险”，先不要写正文，回到 insight audit 重搭骨架。完整不等于有 insight；报告越顺滑、越像普通综述，越要警惕 sharp points 被磨掉。

默认写法要参考：

```text
学习/style_references/anthropic_org_investment_style_reference_2026-04-21.md
学习/style_references/essence_quote_pack_example_lovable_2026-04-21.md
companies/{slug}/analysis/{Company}_org_block_report_*_recovered.md（如果存在）
```

复杂报告不要写成普通综述，也不要把 fact pack 改写成文章。默认用“storyline + blocks”的结构：先用 2-4 段讲清楚主线，再用一个个高密度 block 串起来。每个 block 必须包含：

1. 一个有判断的标题。
2. 一段中文判断段，解释这个机制为什么重要、和业务/组织有什么因果关系。
3. 一段或多段原文 quote pack。播客、访谈、视频必须优先保留 speaker 原话；第三方深度文章可保留作者原文判断。不要把 quote pack 改成第三人称摘要。

读者默认没有完整背景。落笔时不要把大量信息压成一句黑箱判断。每个 block 的中文判断段通常需要 2-5 句，把以下四件事讲清楚：

- 这件事具体是什么，涉及哪个人、团队、产品或流程。
- 过去的工作方式是什么，现在发生了什么变化。
- 这个变化靠什么机制运转，比如招聘、信息流、工具、反馈、决策节奏、绩效或销售组织。
- 它为什么会影响组织速度、产品质量、客户采用、收入质量或竞争位置。

如果自己读起来也有点不理解，或者感觉句子只是把几个概念挤在一起，停止写作，顺着 essence frontmatter 的 `source_path` 回到原始 transcript / article / report。找到对应 speaker、source 和日期，阅读引用前后上下文，再重写判断段。仍然不清楚时，写 `待核验` 或删掉这个 block，不要用浓缩句遮过去。

Block 标号按章节字母重置，不要全篇都用 `B01 / B02`：

```text
第一章：A01、A02、A03...
第二章：B01、B02、B03...
第三章：C01、C02、C03...
第四章：D01、D02、D03...
```

如果报告超过四章，继续按 `E / F / G` 往后排。编号只是导航，标题本身仍要有判断，不能只写“组织动作”“商业模式”。

如果用户要求“组织分析”或“AI org”，复杂报告至少 70% 篇幅写组织：

- Founder 对业务本质和组织的看法。
- 招聘、筛选、人才密度、晋升、senior / junior 配比。
- 信息流、反馈路径、决策 cadence、meeting / planning / demo 机制。
- 内部如何使用 AI、每个人如何与 AI 协作、管理工具如何变化。
- 组织如何对抗熵增、headcount 稀释、enterprise sales 拖慢速度。
- 组织动作如何传导到产品速度、客户 adoption、收入质量。

商业模式、行业、融资、估值、风险可以写，但默认服务组织主线，不要抢走篇幅。

组织报告的正文顺序默认是：

```text
AI 组织三问 -> 核心判断 -> 组织机制主线 -> 组织动作/人才/信息流/节奏 -> 业务影响与反方 -> 待核验问题
```

除非用户明确要求 fact pack，否则不要把“公司与业务 / 产品与商业模式 / 财务融资 / 竞争格局”放在前面。这些内容要后置，并解释它们如何验证或推翻组织判断。

下面这个结构只是 completeness checklist，适合检查有没有漏事实，不适合直接当复杂报告骨架。真正的章节应该优先按 Step 5.6 的 A 类机制组织；只有 fact pack 或用户明确要求综述时，才按下面的通用目录写：

```markdown
---
company: {Company}
type: complex_report
date: {YYYY-MM-DD}
status: draft/current
---

# {Company} 复杂报告

## 核心判断
## 公司与业务
## 行业与竞争
## 产品与商业模式
## Founder / 管理层判断
## 组织动作
## 业务影响
## 财务 / 融资 / 估值
## 风险
## 个人思考
```

写法：

- 句子像研究员，不像 AI 汇报。
- Topic sentence 要有判断。
- 少用“不是 X，而是 Y”模板。
- 说人话。不要为了显得浓缩而牺牲可读性；宁可多写两句，把机制拆开讲透。
- 先给读者必要 context。默认读者不了解这家公司，也没读过前文材料。每个重要判断都要交代：过去怎么做、公司改了什么、这个变化靠什么组织动作运转、为什么会影响业务。
- 注意因果承接。不要把多个抽象名词堆在一句里；用“因为 / 所以 / 这会导致 / 这解释了 / 后续要看”把逻辑接起来。
- 英文要克制使用。中文能准确表达时优先中文；只保留必要专有名词、产品名、岗位名、指标名和原文术语。不要把普通词写成英文来显得专业，例如能写“工作流”就不要写 `workflow`，能写“反馈回路”就不要写 `feedback loop`，能写“发布”就不要写 `launch`。
- 专有名词首次出现必须解释。默认读者完全不了解这家公司和行业黑话。首次出现 `ARR`、`PMF`、`GTM engineer`、`Goodhart`、`NDR`、`gross margin`、`prompt box`、`builder`、`founder mode`、`AI-native`、`workflow` 等词时，要用一句中文解释它具体指什么、为什么重要；之后再使用缩写或英文。
- 不要让标题堆英文。标题优先使用中文判断句；英文只在必须保留原产品名、岗位名、指标名或无法准确翻译时出现。
- 所有关键数字和直接引用都要能回到 essence；如果 essence 没有，先补 essence，不要直接从 transcript 抄到报告。
- Block 内引用要贴近判断段，不要统一堆到文末；读者应能一眼看到“判断”和“证据”如何咬合。
- 一段话里如果连续出现 3 个以上抽象词，如“组织边界、工作流、范式、能力、机制”，通常说明需要拆句。改成“谁做了什么、怎么做、带来什么后果”。
- 每章都要回答一个更高层问题：这家公司为什么可能不一样？这个机制为什么重要？后续用什么事实能证明或推翻它？

正式报告正文不要展示研究过程。不要写“我读了多少份 essence”“本轮重新过了材料”“上一版写浅了”“这次改成”等过程性语言；不要使用第一人称“我/我们”叙述研究动作。source weighting、full essence audit、修改记录可以落在单独 audit 文件或 progress 里，不能出现在面向读者的研究报告正文。

正式报告可以写证据限制，但要写成投资判断的一部分，而不是研究日志。例如：

```markdown
公开材料主要来自 founder 和 growth operator，因此客户侧、员工侧、安全团队和企业采购方仍是后续验证重点。
```

不要写：

```markdown
我这次重新过了 87 份 essence。Podcast essence 是主证据层……
```

如果本公司存在 recovered 文风样例，写作前必须先总结其风格并按它矫正正文。Lovable recovered 样例的核心风格是：先把问题讲简单，再逐步解释组织含义；每段只推进一个判断；多用具体人、具体流程和具体业务后果；少暴露方法论；少用压缩概念；让读者不需要上下文也能跟上。写完后按这个样例做一轮 tone pass。

常见失败模式：

- 用职能目录代替投资判断。
- 忠实总结每条 essence，却没有二阶判断。
- 只保留 Founder 叙事，没有标注 source bias。
- 为了文章顺，把反常识细节、奇怪数字、具体工具和真实流程删掉。
- 觉得“读得顺”就完成了。读得顺只是底线，报告还要能改变读者对公司的看法。
- 把 analysis workflow、source weighting、修改记录写进正式报告正文，导致报告像工作日志而不是研究报告。
- 引用太短，只剩一句证据标签，丢掉 speaker 的语气、上下文和判断力度。复杂报告的关键 block 应保留更厚的 quote pack，优先覆盖定义问题、机制运行、数字、反方和业务传导。

### Step 8. Optional Compression

只有用户明确要求时，才从 complex report 压缩一页版或 500 字版，不重新发明观点。

500 字版按三问：

1. Founder 对 AI 组织有什么独到见解？
2. Founder 落地了哪些具体动作？
3. AI 组织变革对业务有什么影响？

每家公司 500 字内时，不写铺垫，不写行业空话，只保留最能解释因果链的机制和证据。

## 4. Stop Conditions

遇到以下情况先停：

- 数字无来源。
- essence 不足以支撑核心判断。
- source status 显示大量真实失败。
- 用户要求的文风或结构和现有稿明显不一致。
- 需要引用原文但只能找到二手摘要。

## 5. Completion Checklist

- `analysis/` 下有目标 md。
- 关键数字有来源。
- 重要判断能回到 essence；raw transcript 只用于核验或补 essence。
- 有 `待核验` 列表，而不是把不确定信息写成事实。
- 最终稿没有明显 AI 腔、空泛管理学词和无证据结论。
