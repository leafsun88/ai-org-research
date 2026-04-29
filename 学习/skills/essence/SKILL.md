---
name: essence
description: Use when converting company transcripts, podcast notes, YouTube transcripts, Substack articles, reports, jobs pages, or other source material into source-level notes for AI org or investment research.
---

# Essence Skill

`essence` 这个名字保留，是为了兼容现有目录和工作流；它真正产出的东西应当是 `source_note` / `evidence_note` / 逐源厚笔记，不是短摘要。它负责把 `companies/{slug}/vault/{source}/transcripts/`、`financials/reports/` 或 `_optional/` 中的正式 source，转成 `companies/{slug}/vault/{source}/essence/` 里的逐源证据笔记。

核心原则：一份 source 对应一份 source note；一份 source note 里可以有很多 insight blocks。目标不是“聪明地压缩”，而是“认真读完这篇 source 后，把所有高价值证据搬出来，后续写报告不必再重读全文，raw transcript 只用于核验”。

## 0. 为什么还需要这一层

不要取消中间层。直接把所有 transcript 塞进上下文，短期像一个大笔记本，长期会出三个问题：上下文撑爆、出处变松、局部修复困难。正确做法是两层：

```text
companies/{slug}/vault/{source}/essence/{date}_{title}_source_note.md
  # 单篇 source 的厚笔记，可追踪、可重做、可局部修复。

companies/{slug}/analysis/{Company}_research_notebook_{date}.md
  # 多篇 source note 汇总后的公司级笔记本。

companies/{slug}/analysis/{Company}_theme_map_{date}.md
  # 从 notebook 二次整理出的主题地图 / thesis spine。
```

先逐篇 source 扎实读完并落盘，再读公司级 notebook 做主线整理。不要用一个巨型 notebook 代替逐源笔记；它会让后续很难回答“这条判断来自哪篇 transcript、哪篇 source 已经认真读完、哪篇只是扫过”。

## 1. 必读

写 source note 前先读：

- `Agent.md`
- `progress.md`
- `core-principles-and-lessons.md`
- `project-structure.md`
- `学习/style_references/anthropic_org_investment_style_notes_2026-04-21.md`
- `学习/style_references/essence_source_note_example_lovable_lenny_2026-04-22.md`
- 对应 source 的原始 transcript / article / report / jobs page

必要时参考旧样例，但不能被旧样例里的短 quote 带偏：

- `学习/style_references/essence_quote_pack_example_lovable_2026-04-21.md`
- `学习/style_references/essence_format_tests_2026-04-21.md`

如果是批量任务，还要先看：

- `companies/_meta/transcripts/_transcript_essence_queue_*.json`
- `companies/_meta/transcripts/_transcript_essence_queue_*.md`

## 2. 输入与输出

常规输入：

```text
companies/{slug}/vault/podcasts/transcripts/
companies/{slug}/vault/youtube/transcripts/
companies/{slug}/vault/substack/transcripts/
companies/{slug}/vault/financials/reports/
companies/{slug}/vault/_optional/{source}/transcripts/
```

常规输出：

```text
companies/{slug}/vault/podcasts/essence/
companies/{slug}/vault/youtube/essence/
companies/{slug}/vault/substack/essence/
companies/{slug}/vault/financials/essence/
companies/{slug}/vault/_optional/{source}/essence/
```

推荐命名：

```text
{date}_{source-title}_source_note.md
```

旧的 `{date}_{source-title}_essence.md` 可以读，但新产物优先用 `_source_note.md`，frontmatter 里写 `type: source_note`。

队列脚本只负责排工作清单，不会替你理解材料：

```bash
python3 scripts/discovery/build_transcript_essence_queue.py \
  --output-json companies/_meta/transcripts/_transcript_essence_queue_{target}_{date}.json \
  --output-md companies/_meta/transcripts/_transcript_essence_queue_{target}_{date}.md
```

## 3. 工作流

一次只处理一篇 source。单篇 60KB、80KB transcript 通常可以完整读；不要把十几篇 transcript 一次性放进同一个上下文。

正确顺序：

1. 读 source metadata，确认公司、日期、speaker、source type、relevance 线索。
2. 从头到尾读 source，不只搜关键词，不只读开头和结尾。
3. 每遇到重要机制、动作、数字、组织信号、产品策略、客户反馈、商业模式、竞争判断、反方风险，就开一个 insight block。
4. 后文继续补充同一机制时，把证据并入已有 block，不重复开空标题。
5. 写完后做 coverage audit：检查有没有漏掉具体数字、组织动作、工具、岗位、招聘标准、办公室/会议/lunch/feedback 等看似琐碎但能解释组织运行的细节。
6. 落盘并验证格式，再进入下一篇 source。

Batch mode：

- 一个 batch 开始时读一次本 skill、四个核心文件和 style reference。
- 把本轮角度压成一张短 checklist 放在当前上下文里。
- 之后一条 source 一条 source 地读和写。
- 新会话、subagent、context 压缩或中断很久后，重新读本 skill 和 style reference。
- 长批量任务按 5-10 条 source 为一个批次收口，更新 queue/status，再继续。

`collect` 调用 essence 时，不应把全量 transcript 交给同一个上下文。它只需要生成 backlog，或把刚完成的高相关 source 交给 `/ai-org-essence` 按 batch 处理。

Subagent batch mode：

- 用户允许并行时，可以把 source note 写作分给多个 subagent；这适合 podcast / YouTube 批量补 note、长 transcript 分批、或高相关 source 已经排好队的场景。
- 主线程负责修改 skill、核心文件、queue、status、progress 和最终验收；subagent 只负责自己被分配的 transcript 与对应 source note 输出，不改共享状态文件，不改脚本，不改 skill。
- 每个 subagent 开工前必须读取 `Agent.md`、`progress.md`、`core-principles-and-lessons.md`、`project-structure.md`、本 skill、`学习/style_references/anthropic_org_investment_style_notes_2026-04-21.md` 和 `学习/style_references/essence_source_note_example_lovable_lenny_2026-04-22.md`。
- 分配给 subagent 的写入范围必须互不重叠，例如 Worker A 只写 podcast 的 4 条 `_source_note.md`，Worker B 只写 YouTube 的 5 条 `_source_note.md`。所有 worker 都要知道自己不是唯一在改这个 repo，不能 revert、覆盖或清理别人的文件。
- 单个 subagent 的推荐批量是 3-6 条 source；长访谈、法律长节目、Founder 原声访谈可以降到 1-3 条。subagent 内部仍然一条 source 一条 source 读写，不能把多篇 transcript 混成一份 note。
- subagent 的最终回报必须列出：写入文件路径、每份 note 的 `##` block 数、中文译引数、跳过的 low relevance / duplicate source、以及自己跑过的格式检查结果。
- 主线程收到 subagent 结果后，再统一更新 status / progress，并跑跨文件验证。不要让多个 subagent 同时编辑同一个 `_status.md` 或 `_queue.md`。

## 4. Relevance Gate

先判断材料是否值得进入 source note。

保留条件：

- 和公司、Founder、管理层、产品、客户、行业、组织、AI 转型或投资判断有关。
- 能提供新的机制、动作、数字、例子、矛盾、反方或原话。
- 对后续报告有可引用价值。
- Founder / CEO / 负责人原声优先，但不是硬门槛。科技媒体、投资人、律师、客户、行业专家、竞品 founder 的深度分析，只要高度相关且能提供机制、数据、竞争、风险或商业判断，也应进入 source note。
- Jobs / careers / security / GRC / enterprise / pricing / docs 等官方页面，如果能说明组织扩张、岗位变化、治理或商业化，应作为 source 进入 `_optional/` 或对应 vault，再写 source note；不要指望报告阶段凭记忆补。

淘汰条件：

- 只是泛泛新闻串烧，和公司只有标题级关联。
- 教程、营销片、短噪音、重复字幕，无法提供新信息。
- 只有很宽的行业词命中，没有公司、产品或关键人物上下文。
- 第三方材料不因为“不是公司内部原声”而淘汰；只在它缺少深度、缺少公司相关性、或只提供标题级信息时淘汰。

低相关也要可追踪，但不需要写完整 note。优先在 queue / status 里标记：

```text
status: no_essence_low_relevance
reason: ...
source_path: ...
```

如果用户要求审计轨迹，或该 source 已经进入人工 review，再写短 rejected record：

```markdown
---
company: {slug}
source_type: {podcasts|youtube|substack|financials|optional}
type: source_note
status: rejected_low_relevance
source_path: ...
date: YYYY-MM-DD
---

# {Source Title}

这条材料只在标题或背景里提到公司，正文没有新的组织、产品、客户、财务或竞争信息。本轮不进入分析证据池。
```

重复 source 同理：如果内容已由 podcast / YouTube / Substack 的更好版本覆盖，不写完整 note，只在 queue / status 标 `duplicate_of`。需要审计时再写 rejected duplicate record。

## 5. 默认提炼角度

用户没有额外指定时，按这些角度逐段看材料。角度是雷达，不是筛子：

- 组织结构、团队形态、管理层思考。
- 组织形态和业务模式之间的关系。
- 招聘标准、人才密度、绩效、晋升、淘汰机制。
- 工作 cadence、会议、planning、demo、roadmap、office、lunch、direct feedback。
- 内部 AI 转型、AI 管理工具、agent、workflow、developer productivity。
- 工具体系如何变化，人和 AI 如何协作。
- 管理产品是什么，管理产品背后的世界观是什么。
- 产品战略、GTM、客户反馈、业务数据、商业模式、行业结构。
- Jobs / careers 中出现的岗位变化：PM、FDE、Deployment Strategist、GRC、Security、Sales、Enterprise 等。
- CEO / Founder 对行业的哲学判断和长期下注。
- 竞争对手、客户、伙伴、监管、反方风险。

## 6. Source Note 格式

每份 source note 只保留 frontmatter、标题、必要说明和 insight blocks。不要加数据库式尾巴。

Frontmatter：

```yaml
---
company: {slug}
source_type: {podcasts|youtube|substack|financials|optional}
type: source_note
status: done
source_path: companies/{slug}/vault/{source}/transcripts/{file}.md
source_title: "{title}"
source_date: YYYY-MM-DD
created_at: YYYY-MM-DD
speaker: "{Founder / CEO / guest / author}"
source_weight: A
relevance: high
quote_language: zh_translation_from_en_transcript
---
```

Block 格式：

```markdown
## {像投资判断的小标题}

{一段详实判断自然段。先讲机制，再讲具体动作和为什么重要，最后落到组织、业务或投资含义。读者默认没有读过原文，也不了解这家公司，所以不要省掉谁、什么事、为什么重要。}

“{一条较长、连续、有上下文的中文译引。不要拆成三四条短句。}” —— {speaker/source, date}
```

高相关长访谈出现 15-30 个 blocks 是正常的。宁可厚，不要聪明但空。一个 source note 如果只有 3-6 个高层观点，通常说明你在摘要，而不是在做证据笔记。

## 7. Quote 规则

Quote 是素材池，不是装饰。每个 high-relevance block 后必须有一条可复用的 source quote；没有足够证据就删掉这个 block，或降级为 low-confidence note。

公开英文播客 / 视频 transcript：

- 默认把引用翻译成中文，方便中文报告直接使用。
- 每个 block 放一条较长的连续译引，保留前后语境和说话人口吻。
- 中文译引必须像真正的引用，而不是旁白摘要。不要写“Lenny 在访谈里问 / Anton 回应说 / Elena 介绍”这种第三人称转述；引号里应尽量保留说话人的第一人称和现场语气，例如“我们用 Linear 做很多事，甚至用它做 talent application tracking”。
- Quote 不能只是重复上一段判断。判断段负责解释机制和含义，quote 负责提供一手事实、原话语气、具体数字或更细的上下文；如果两者只是在说同一句话，要么重写判断段，要么换一条更有信息量的 quote。
- 不要拆成一句一句的短 bullet quote。
- 不要把 analyst paraphrase 放进引号里；引号里只能是 source 本人的意思。
- 可以轻微修正 ASR 错字、断句和明显错词，但不能改变意思。
- 不需要贴大段原英文；如需逐字核验，回到 `source_path`。

中文 source：

- 直接保留中文原话或轻度清理后的近原话。
- 同样优先一条连续上下文，不要短句清单。

第三方 written analysis / 报告 / jobs page：

- Quote 可以来自作者、页面或岗位描述本身，不必强行寻找 founder 原声。
- 英文内容默认翻译成中文；岗位名、产品名、法律/合规术语可保留英文。
- 引号里必须是 source 的事实、判断、要求或描述，不能把我们的总结伪装成原文。

长度标准：

- 引用要足够长，能让后续读者判断上下文，而不是只证明一个关键词存在。
- 公开 source 不要整段整页搬运；通常一条连续中文译引覆盖一个完整说法即可。
- 内部访谈、用户自有材料、已授权 transcript 才可以保留更长连续原话。

Long Quote Gate：

- 如果一条 quote 短到可以当 slogan、标签或关键词证据，它就是不合格的。每个 high-relevance block 的译引必须能独立说明“谁在说、说的是什么机制、前后语境为什么重要”。
- 公开 transcript 的单条译引通常应至少包含两个连续句子，或一个完整的长句群；经验上 80-250 个中文字符比较合适。短于 60 个中文字符的 quote 默认需要返工，除非它是 source 中独立完整的数字、产品名或法律事实。
- Quote 必须连续，不能把 transcript 里相隔很远的几句拼在同一组引号里；需要跨段证据时，拆成两个 insight block，或在判断段说明综合逻辑。
- Quote 里保留说话人的口吻。Founder / CEO / 主讲人用第一人称时，译引也尽量保留“我们 / 我”；第三方主持人、律师、记者或行业分析者的 quote 也要保留其推理链，不能写成我们的复述。
- 一个 block 只允许“判断段 + 一条长译引”。不要用三四条短 quote 补足长度；这会让后续报告只拿到碎片，还是要回 raw transcript。
- 已写出的旧短 `_essence.md` 或旧短 `_source_note.md` 只能作为 source inventory 参考，不能作为新 note 的风格样本。发现旧 note 的 quote 过短时，优先回原 transcript 返工。

Attribution：

```markdown
“……” —— Anton Osika, Lenny's Podcast, 2025-03-09
“……” —— Lovable careers page, 2026-04-22
```

## 8. 写法风格

风格参考 `学习/style_references/anthropic_org_investment_style_notes_2026-04-21.md` 和 `学习/style_references/essence_source_note_example_lovable_lenny_2026-04-22.md`。

写法目标：

- 小标题就是 topic sentence，直接给判断，不写“组织文化”“产品开发”这种空标签。
- 判断段先讲机制，但必须给足读者理解所需的背景。
- 每段至少有具体名词、动作、数字、岗位、流程、工具或 case。
- 中文判断和英文关键词可以混写；英文在更精确、更像行业原话时要保留，比如 `feedback loop`、`cadence`、`workflow`、`roadmap`、`demo`、`ship`、`context`、`owner`、`taste`、`GTM`、`PMF`、`AI-native`、`founder-mode`、`Minimum Lovable Product`。不要为了“全中文”把专有名词硬翻得别扭。
- 句子可以长，但要有信息密度。
- 说人话。一个判断如果需要很多背景才能懂，就拆成多句，先解释事实，再解释机制，最后落到含义。
- 竞争判断要敢压缩：谁强、谁弱、强在哪里、弱在哪里。
- 风险写成机制，不写“存在不确定性”这种空话。

禁止：

- “这段材料说明了……”
- “AI 赋能”“深度协同”“组织升级”这类空词。
- 用二元对照模板撑句子，尤其不要把“不是 X，而是 Y”当默认句式。
- 一篇 source 只有一条 insight。
- 每个 block 只贴一句象征性引用。
- 用过度浓缩的抽象词代替解释，比如只写“组织边界变化”“工作流重构”“范式迁移”，但没有说明具体是谁如何工作发生了变化。
- 添加 `Evidence anchors`、`Tags`、`Report use`、`Fact Bank`、`Open Questions`、`Candidate Mainlines`、`Coverage Notes`、`关键引用`、`原文定位`、`可用于哪些分析角度` 等工具字段。

## 9. Coverage Audit

写完后必须做遗漏检查。Lovable 的失败案例说明：问题不是“只读 essence”规则错了，而是 source-level note 做得太薄，导致正式报告按规则只读 essence 时丢失组织细节。

重点检查这些容易被摘要漏掉的材料：

- 具体 cadence：weekly planning、FigJam、Linear、demo、roadmap 如何运行。
- 招聘与筛选：work simulation、JD 的强度话术、long hours、comfortable work need not apply。
- 线下协作：office、lunch、direct feedback、非结构化高带宽沟通。
- 工具体系：Linear 是否被拿来做 talent application tracking，工具是否跨职能复用。
- 组织扩张信号：Product Manager、FDE、Deployment Strategist、GRC、Security、Sales、Enterprise、Customer Success 等岗位变化。
- 业务基础设施：登录、数据持久化、支付、security、compliance、deployment、collaboration。
- 数字：ARR、MAU、paid users、headcount、launch date、growth cadence。
- 反方与失败案例：retrofit、模型卡点、benchmark risk、existing codebase 限制。

如果发现正式报告需要的证据只在旧 analysis、style reference 或记忆里出现，而 source note 没有，优先回到原 source 补 source note；不要在报告里绕过 source note 规则。

## 10. 公司级 Notebook 与 Theme Map

当一批高价值 source note 写完后，可以生成公司级 notebook，但 notebook 是二次汇总，不是替代 source note。

推荐路径：

```text
companies/{slug}/analysis/{Company}_research_notebook_{date}.md
companies/{slug}/analysis/{Company}_theme_map_{date}.md
```

Notebook 做什么：

- 按主题汇总 source notes 里的厚证据。
- 保留 source note 路径，方便回查。
- 让分析阶段可以整体浏览材料，不必重读所有 raw transcripts。

Theme map 做什么：

- 从 notebook 中整理几条主线 / thesis spine。
- 区分强证据、弱证据、缺口和反方。
- 为正式报告搭结构。

不要在 source note 里提前写大而全的报告结构。Source note 的职责是保留证据；theme map 和 report 才负责主线。

## 11. Verification

写完后至少检查：

```bash
test -s companies/{slug}/vault/{source}/essence/{file}_source_note.md
rg -c '^## ' companies/{slug}/vault/{source}/essence/{file}_source_note.md
rg -c '^“' companies/{slug}/vault/{source}/essence/{file}_source_note.md
rg -n 'Evidence anchors|Tags:|Report use|Fact Bank|Open Questions|Candidate Mainlines|Coverage Notes|关键引用|近原文|原文定位|可用于哪些分析角度|这段材料说明' companies/{slug}/vault/{source}/essence/{file}_source_note.md
awk '/^“/ && length($0) < 80 {print FILENAME ":" FNR ":" length($0) ":" $0}' companies/{slug}/vault/{source}/essence/{file}_source_note.md
```

理想状态：

- 文件非空。
- high-relevance blocks 数量和引用数量大致一致；新格式通常每个 block 一条长译引。
- forbidden labels 检查为空。
- short quote 检查为空；如果有命中，要逐条判断是否是独立完整的数字 / 法律事实，否则返工。
- 逐条回看 source note，确认它覆盖了 source 中所有高价值机制、动作、数字和组织细节。

## 12. Done When

- 输入 source 已完整读完，而不是只扫标题、关键词和开头。
- relevance 已判断；低相关或重复 source 有可追踪记录。
- 高相关 source 输出到正确的 `vault/{source}/essence/`。
- 每份 source note 有多条 insight blocks，厚度足以支持后续报告。
- 每个 block 都是自然判断段 + 一条足够长、连续、有上下文的中文译引，没有工具性尾巴。
- block 数、中文译引数、禁用字段检查、短 quote 检查均已通过；并行写作时，主线程已完成跨 worker 总验收。
- source note 覆盖了材料里的主要机制、数据、组织动作、产品动作、岗位变化和反方。
- 后续 `analysis` 可以直接读 source note 写报告，raw transcript 只用于核验。
