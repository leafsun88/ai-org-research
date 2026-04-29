---
company: midjourney
source_type: youtube
type: source_note
status: done
source_path: companies/midjourney/vault/youtube/transcripts/2026-04-21_Midjourney-V8-Launch-Confirmed-for-Year-End-Super-Draft.md
source_title: "Midjourney V8 Launch Confirmed for Year-End! Super Draft, Style Finder, PCode System Revealed"
source_date: 2026-04-21
created_at: 2026-04-22
speaker: "Nam-kyoung Cho / Midjourney Korea"
source_weight: B
relevance: high
quote_language: zh_translation_from_en_transcript
---

# Midjourney V8 Launch Confirmed for Year-End! Super Draft, Style Finder, PCode System Revealed

## Office Hours 口径显示 V8 不是小修，而是全团队级别的主线工程

这条来源是对 Midjourney Office Hours 的二次转述，不能当作 founder 原声逐字稿，但它提供了 V8 roadmap 的细粒度信号：数据验证完成、核心系统验证完成、进入大规模系统和大数据训练，且大部分工程团队聚焦 V8。这个信息解释了 V8 为什么会牵动 V7.1、draft mode、personalization 等旁支功能：Midjourney 的产品节奏被下一代模型主线工程吸走，短期 feature release 会服从 V8 验证。

“第一条更新是 V8 开发状态，团队现在的重点是基于稳定 V7 代码库构建的 V8，他们说核心系统已经被验证，这比预期快很多；按照九月的计划，本来十月做数据验证，十一月和十二月再搭系统，但现在十月中旬，数据验证上周已经完成，核心系统也验证过了，现在正在扩大系统规模，并用大数据集在大规模系统上训练。” —— Nam-kyoung Cho / Midjourney Korea, 2026-04-21

## V8 的发布时间被提前，说明底层验证进展好于原计划

转述里提到 V8 目标从较晚节奏前移到年末前，甚至晚十一月或早十二月。这条对研究有用，因为它呈现 Midjourney 的内部工程 confidence：不是“未来某天会有 V8”，而是已经过了数据与核心系统验证，剩下主要是 scale-up 和 compute 成本。即使时间线有变，这也能作为 launch evidence，说明 V8 在公司资源优先级里已进入临近发布阶段。

“如果没有问题，V8 就会准备好；在大系统上跑需要比预期更久的准备，但实际执行并不会花太长时间，它需要很多算力，所以会有成本，但执行本身不长。反映这种快速进展，我们的目标是在年底前发布，Midjourney 通常说年底时指十二月十五日，但你可以预期大概在十一月底或十二月初，虽然他们也说明日程可能变化。” —— Nam-kyoung Cho / Midjourney Korea, 2026-04-21

## V7.1 更像 V8 的验证层，不一定作为独立用户价值发布

V7.1 的描述很关键：它在 guides 和 moderators 内部测试，prompt interpretation 有提升，但“major improvements”不够明显，所以可能被跳过。这说明 Midjourney 内部会把中间版本当作验证层，而不是每个小版本都推给大众。对产品组织来说，这是一种取舍：宁可把测试和反馈集中在 veteran 用户群里，也不把不够明显的增量发布给普通用户，避免消耗工程和客服资源。

“内部在 Guides 和 Moderators group 做 V7.1 测试，这意味着 V7.1 已经出来了；他们确认 prompt interpretation accuracy 有改善，但也说重大改进很少，而重大改进必须在视觉上明显。Midjourney 内部说 7.1 充当 V8 系统的 verification layer，与其把重点放在 7.1 自身性能提升，不如用它测试 V8 features。” —— Nam-kyoung Cho / Midjourney Korea, 2026-04-21

## Style Finder 比 V8 更像短期可发布功能，目标是让用户快速找到审美空间

这条视频对 Style Finder 的描述比普通 V8 reaction 更有结构：它可能基于大量 SREF seeds，让用户通过关键词、相似图、线条风格、细节选择不断收敛到目标 aesthetic。这个功能如果成型，会把 Midjourney 的交互从“写 prompt”变成“浏览、筛选、选择、保存风格”，也就是 creator workflow 的前端发现层。它和 V8 模型能力是两条线：模型负责生成，Style Finder 负责降低 taste search 成本。

“Style Finder 被说成性能很高，能帮助用户快速找到想要的 aesthetic style，虽然形式还不知道，但我觉得可以理解为已经大致完成；如果你输入 Man 或 Manga 这样的 prompt，可以用 fuzzy search 的关键词搜索找到很多风格，再根据这张图搜索相似风格，也可以继续区分漫画风格里的线条，问你想要这种线条还是更多细节，最后可能显示那个 style 的 SREF seed。” —— Nam-kyoung Cho / Midjourney Korea, 2026-04-21

## Style Creator 的难点不是生成，而是如何客观评价“这是不是我要的风格”

Style Creator 被描述为从零创建风格，而不是简单混合两个 style seed。真正难点在评价：用户可能觉得“喜欢但不对”，平台也难以量化生成风格是否符合意图。这个问题直指 Midjourney 的产品核心：审美系统不像文字准确率或分辨率那样容易打分，模型越走向 taste 和 personalization，评估体系越依赖用户行为数据、偏好排名和社区反馈。

“Style Creator 有些细节被透露出来，我很惊讶它说是从头创建 style；我原本想象它会用 Style Seed Blends，把 A 和 B 混在一起生成新风格，但既然说从零开始，我觉得真的可能是在创造全新风格。它正在测试，但很难评估，我创建了一个 style，可它真的是我想要的吗？我觉得我喜欢它，但又觉得它不一样，所以要客观量化生成出来的 style，方式确实有点模糊。” —— Nam-kyoung Cho / Midjourney Korea, 2026-04-21

## PCode、用户主页和 Style Finder 指向一个“Midjourney 版 Instagram”

视频把 Style Finder、personalization、PCode 和 user profile 连成了一条产品线：用户找到的 style 可以分享到个人主页，其他人 follow、like、复用 SREF seed。这不是附属社区功能，而是 Midjourney 可能的分发和数据飞轮：用户通过风格分享形成社交关系，平台获得偏好排序与 aesthetic ranking 数据，再反哺模型与个性化系统。Midjourney 的社区不只是 Discord support，而是审美数据采集和创作者 discovery 层。

“Style Finder 和 Style Creator 都被说成和 personalization 以及 user profile system 紧密连接；personalization 指的是 Pcode，通过个人偏好风格的 ranking 创造某种东西，而 user profile system 可以理解成 Midjourney 版 Instagram。你在 Style Finder 里找到的 style 会分享到你的 user profile，最终就像分享 Instagram 图片一样分享风格，还会提供跟随的 SREF seed 信息，其他用户看到以后可能 follow 你或 like。” —— Nam-kyoung Cho / Midjourney Korea, 2026-04-21

## Super Draft 的问题暴露了 Midjourney 用户对“速度换质量”的低容忍

Draft mode 和 Super Draft 的信号很重要：团队想把生成压到 sub-second，但当前 performance below expectations，主要是速度做到了、质量不好。Midjourney 的用户基础和其他生产力工具不同，创作者可以接受等待，但很难接受审美降级。V8 宣称五倍速度固然重要，但 Midjourney 的核心 KPI 仍然是“看起来好不好”，速度必须在不牺牲质量的前提下才会被用户认可。

“他们正在优化 Draft mode 的速度和响应性，但说 current performance is below expectations；上周提到可以在一秒以内生成图像，这让我有点不安。对 Midjourney 用户来说，速度并没有那么重要，质量才是最重要的，高质量又快当然令人印象深刻，但高速度低质量不行。Draft mode 刚出来时开发者说我们喜欢它因为太快了，结果用户抱怨为什么质量这么差。” —— Nam-kyoung Cho / Midjourney Korea, 2026-04-21

## Midjourney 的线下 meetup 和 ranking party 是社区运营，也是模型训练数据入口

来源提到 San Francisco 船上 meetup、style ranking party、Fast Hour 奖励等社区动作，这些看似轻运营，但和模型改进紧密相关。Midjourney 鼓励用户参与 style ranking，奖励 fast hours，再把反馈数据用于未来 aesthetic 和模型方向。这是一个明确的社区数据回路：创作者参与越多，平台越理解偏好，模型越贴近用户 taste，反过来增强社区粘性。

“他们说会举办 style ranking party，鼓励用户参与，收集到的 feedback data 会反映到未来 aesthetic 和 model improvements 的方向里；这意味着如果我们努力参与，它会被用来提高我们正在使用的 Midjourney 性能。如果你想让自己使用的服务变好，他们给你一小时免费时间，所以请参与这个 style ranking。” —— Nam-kyoung Cho / Midjourney Korea, 2026-04-21

## 新高管、工程招聘和 project management 招聘说明 Midjourney 正在补运营瓶颈

最后几段提供了组织信号：新 executive team 加入，目标是提升 operational efficiency 和解决 bottlenecks；计划增聘 engineers 和 project management staff；David 在准备官方 announcement video，同时推进未披露项目、社区项目和硬件相关项目。对 Midjourney 这种长期精简、founder-led 的公司来说，这些动作意味着从研究/社区驱动转向更复杂的产品组合管理。

“关于公司增长和领导层，一个新的 executive team 已经加入，用来提高 operational efficiency 并解决 bottlenecks；他们计划继续招聘工程师和 project management staff，所以有了新的负责人以后，会招聘相关人员。创始人 David 目前正在准备官方 announcement video，并管理新项目，未披露项目包括功能项目、社区项目和硬件相关项目，也在等待内部批准和媒体准备。” —— Nam-kyoung Cho / Midjourney Korea, 2026-04-21
