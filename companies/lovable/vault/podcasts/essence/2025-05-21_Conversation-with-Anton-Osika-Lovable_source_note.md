---
company: lovable
source_type: podcasts
type: source_note
status: done
source_path: companies/lovable/vault/podcasts/transcripts/2025-05-21_Conversation-with-Anton-Osika-Lovable.md
source_title: "Conversation with Anton Osika, Lovable"
source_date: 2025-05-21
created_at: 2026-04-22
speaker: "Anton Osika"
source_weight: A
relevance: high
quote_language: zh_translation_from_en_transcript
quote_style: single_long_translated_excerpt_per_block
---

# Lovable / Inside AI 2025-05-21 — Source Note

> 以下每个 insight block 后面只放一条较长的中文译引，不拆成碎句。译引来自英文 transcript，保留说话人的原意和口吻；如需逐字核验，回到 `source_path`。

## Lovable 的产品定义从一开始就是 operating system，而不是一次性生成网页

Anton 对 Lovable 的一句描述很关键：用户用自然语言描述应用，Lovable 生成前端、后端、AI chat、login、data storage、payments，最后直接发布链接。这不是单点代码生成，而是把从 idea 到可发布产品的多段工作流合到一个界面里。他进一步说 Lovable 要成为新一代创业者构建 AI-native businesses 的 operating system。这个 framing 解释了 Lovable 后续为什么自然会补 analytics、SEO、payments、security 和 business lifecycle。

“我们的设计负责人 Nad 经常说，Lovable 就像 ChatGPT 和 Figma 生了一个孩子。你用简单英文，或者任何语言，解释自己想做什么应用或网站，它就会被创建出来；你可以给应用加 AI chat 功能、登录、数据存储，也可以让它整体看起来很漂亮。做完以后，你会得到一个已经发布到互联网上的链接，可以分享给朋友。我们看到成千上万创业者用 Lovable 构建完整业务，接 Stripe 收款并从中赚钱。我们正在朝着一种几乎像操作系统的方向建设，让新一代创业者在上面构建 AI-native businesses。” —— Anton Osika, Inside AI, 2025-05-21

## 100K 付费用户说明 Lovable 已经从爆款 demo 进入核心工作流

这条访谈发生在 Lovable 发布约六个月后，主持人提到 Anton 刚在 LinkedIn 说公司已经达到 $50M ARR；Anton 进一步给出超过一百万人使用、超过十万人每月付费的数字，并说这些人知道 Lovable 已经是自己 workflow 的核心部分。这里的重点不是数字漂亮，而是 paid users 的语义：用户不只是来体验 AI 新鲜感，而是在把 Lovable 放进持续工作流。

“我们已经有超过一百万人使用 Lovable，也有超过十万人放入信用卡、每个月付费，因为他们知道 Lovable 是自己 workflow 的核心部分。这是在我们六个月前发布之后发生的。人们会把我们和其他欧洲 startup 比较，到目前为止，它看起来像欧洲这个领域里增长最快的公司。” —— Anton Osika, Inside AI, 2025-05-21

## Anton 早早排除了训练模型这条路，把 bottleneck 定义成人和 AI 的 interface

这条访谈最重要的判断，是 Anton 明确说“训练自己的模型”不是 Lovable 的瓶颈。AI 应用公司如果没有这层判断，很容易把精力浪费在 foundation model 竞赛里；Lovable 把焦点放在 human interface，利用模型能力快速上升的 wave，把模型输出变成普通人能使用的软件工作流。这个选择决定了组织配置：Lovable 要找的核心人不是 pretraining researcher，而是能理解用户、产品界面、软件工程和模型编排的工程型产品人才。

“我看到的巨大 unlock 是，过去几十年里，人们通过创造软件产品创造了数万亿美元价值，但会写代码的人远少于 1%。所以我开始做一个新的 interface，让你不需要知道怎样写代码。我也不知道这个 interface 最终会是什么样子；现在它是 chat、point and click，也会有更多直接控制，但它还会演化很多。基于这个 vision，我组建了一支很强的工程师团队。很多人在我开始时以为，你必须训练自己的模型，或者去那个空间里竞争；但我当时很清楚，不，瓶颈不会在那里，瓶颈是面向人的 interface。这就是我们一直专注的地方，我认为这也是我们成功最大的部分。” —— Anton Osika, Inside AI, 2025-05-21

## Lovable 的技术策略是把模型能力吃干净，而不是做 API 上游

Anton 在这条访谈里把 application layer 的定位说得很清楚：Lovable 不做 foundation model，不和底层 API 竞争，而是尽可能用满它们，让 AI 控制软件工程师工作的许多部分。这个判断能帮助后续报告写清楚 Lovable 的公司形态：它不是模型实验室，也不是传统 SaaS；它是一个把 foundation model 能力翻译成软件创建 workflow 的产品和基础设施公司。

“我们聪明地思考怎样让 AI 和大语言模型控制软件工程师所做的许多部分，虽然还不是全部，但已经有很多部分，比如写代码、部署到互联网等等。所以专注在 interface 和 application layer，而不是专注在 API 本身，只是把它们的潜力尽可能发挥出来，这就是让我们成功的原因。当然，我们使用的 foundation models 也在快速变得越来越好，这是我们正在乘上的一股浪潮。” —— Anton Osika, Inside AI, 2025-05-21

## Lovable 的 scaling pain 很具体：每个 token 后面都有自己系统里的 cascade of events

Anton 讲增长挑战时没有泛泛说“流量大”，而是把 Lovable 的系统负载讲到 token 级别：5 万个新项目每天启动，每个项目几十到上百个用户请求，每个请求又有很多 streaming tokens，每个 token 在 Lovable 侧触发一串事件。这解释了为什么 Lovable 早期既是产品公司，也是基础设施公司。用户看到的是 prompt-to-app，组织内部要承受的是实时生成、文件系统、部署、版本、协作和外部服务依赖同时爆炸。

“第一个也是主要的 growth beast，就是我们必须服务的流量规模，同时还要保持在线。一路上我们压垮过很多依赖的服务，还必须迅速把它们替换掉。一个例子是 GitHub 有一次 incident，他们调查以后发现是我们压垮了他们的 cluster；因为工程师可以通过 GitHub 编辑代码，Lovable 把那个 cluster 打爆了，于是他们把我们完全断开，Lovable 就下线了，我们必须立刻找 workaround，做出一个不依赖 GitHub 的版本。我们还不得不重写整个系统来承受这个规模，因为大语言模型输出的每一个 token，在我们这边都会触发一串 cascade of events。我们每天有 5 万个新项目启动，每个项目可能有几十个、甚至上百个用户请求，每个请求又有很多小 token 流经整个系统。” —— Anton Osika, Inside AI, 2025-05-21

## Security 被 Lovable 当成产品责任，而不是用户自己 vibe coding 的后果

Anton 对 security 的口径非常值得留：他没有把非技术用户生成不安全应用的问题甩给用户，而是说 Lovable 要在合理范围内承担责任，并且已经做 security review。他判断未来 AI 会比人类 expert 更可靠，甚至“只有人类做 security reviewer”会不符合 best practice。这条线对企业化很重要，Lovable 要卖的是 controllable speed；如果不能把安全扫描、权限、部署治理接进产品，非技术团队 build 的能力会变成企业风险。

“有人会在 Lovable 上创建不安全的应用，于是问题就变成：这是我们的错，还是他们的错？我们希望在 security 侧承担尽可能多、但合理的责任，并且增加功能，确保用户能看到自己是否引入了 security vulnerabilities。这个问题当然可以解决，我甚至想说我们已经解决了 90% 的风险。今天，expert humans 找安全弱点比 AI 更可靠；但我不认为未来还会这样。未来，如果只有一个人类作为唯一的 security reviewer，会被 security best practices 所禁止；你会需要一个 AI。随着这个方向继续前进，AI 在 security 上越来越强，security 会变成更小的问题。” —— Anton Osika, Inside AI, 2025-05-21

## Lovable 的 roadmap 从生成走向运营：让 AI 管完整产品生命周期

Anton 在 5 月已经把产品路线讲到很远：现在 Lovable 负责 implementation、deployment、hosting；未来要覆盖 design and validation、feedback、production operation、analytics、迭代决策和业务增长。这说明 Lovable 的目标不是把“写代码”做完，而是把一个软件产品持续演进的循环交给 AI 和团队共同处理。这个判断也解释它为什么会进入企业：企业最痛的不是做一个 demo，而是让 idea 经过验证后安全进入现有系统。

“Lovable 让你非常快地启动一个网站或者完整应用，我们想让这件事快得多。这里有很多组成部分：AI 以及我们怎样使用 AI 是很大一部分；还有把所有你需要的东西更顺滑地集成在一起，让最常见功能更容易做出来，比如 payments、authentication 等等。再往前看，如果你想建立一个软件产品业务，你需要不断演进它，思考下一个 feature 应该是什么，并确保你能得到这些 feature 的反馈。所以这里有 design and validation 阶段，然后是 implementation、deployment 和 hosting 阶段，这是我们现在正在做的。但一旦有真实用户在 production 里使用，整个系统的 operation 和演进会变得更复杂，而这正是我们还能加很多价值的地方。” —— Anton Osika, Inside AI, 2025-05-21

## Lovable 未来要完成的闭环，是从软件生成走到产品增长

Anton 明确说，用户的最终目标不是“构建软件”，而是构建有用、有人使用的软件产品。这句话很重要，因为它把 Lovable 的价值从 developer tool 拉到 business outcome：AI 不只帮助写代码，还要帮助用户增长业务、改善产品、结合 analytics 持续迭代。后续 Elena Verna 的 growth 访谈，其实是在补这条产品路线对应的组织能力。

“现在这部分我仍然建议由人类工程师，或者至少半技术的人来处理，因为他们能理解整个系统的 end-to-end。但未来，整个 flow 都会由 AI 处理。更关键的是，构建软件不是我们用户的终点；他们的终点是构建有用的软件产品，并且让这些产品拥有用户。所以，帮助他们完成这个 circle，帮助他们增长一个 business 或产品，和 AI、普通 analytics 一起持续改进，这是我们正在努力的方向。” —— Anton Osika, Inside AI, 2025-05-21

## CMS 和 SEO 这种小需求，说明 Lovable 正在吃掉传统 web stack 的日常维护层

主持人把自己的 use case 讲成 CMS：小网站需要加页面、改标题、更新内容，过去会落入 WordPress 或静态站点工具的复杂性；现在可以直接和 Lovable 对话。Anton 的回应很细，他提到文本可即时编辑、更大的改动还要更快、标准 web practices 如 Google 展示标题也要一键设置。这说明 Lovable 的机会不只在新应用，也在大量存量小网站、内部工具和团队页面的日常维护层。

“你分享这个 use case 很有价值。你也知道，有些文本你可以立刻编辑；但对于更大的改动，它现在还不会像你想要的那样快，我想这也是我们最想改变的事情之一。另外还有一些标准 web practices，比如你想一键设置标题，让人们在 Google 上找到它时能正确展示，这些也是我们正在建设的方向。历史上，人们要么找 web developer，要么用 WordPress 或其他 static website builders。现在你不用再做这种选择；作为非技术用户，你可以得到两个世界的东西：AI 能做 web developer 会做的任何事，而且比你和另一个人类来回 handover 要快得多。” —— Anton Osika, Inside AI, 2025-05-21

## Anton 给 web developer 的新定位，是把工程师从写代码的人改成现实问题到技术方案的翻译者

Anton 对开发者的回答很有组织意味：他没有讲“AI 替代 web developer”，而是重新定义 engineer 的 value。工程师应该把自己看成把现实问题翻译成技术解决方案的人，而不是会写某种代码的人。这个定义和 Lovable 的产品一致：代码生成会变得便宜，真正稀缺的是理解问题、判断架构、保证质量、连接业务约束。Lovable 越普及，工程师的工作越会往 system judgment 和 quality control 上移。

“我通常会描绘一个非常正面的图景，而且我觉得这对大多数工程师是能共鸣的：作为 developer 或 engineer，你应该把自己看成一个把现实世界的问题翻译成技术解决方案的人。你不应该把自己看成一个能写某一段代码的人。如果你是 web developer，你会使用 AI 更快、更熟练地解决技术问题。对那些有工程师经验的人来说，这就是一个机会。” —— Anton Osika, Inside AI, 2025-05-21

## Europe 是 hard mode，但 Anton 想把破局本身变成差异化

Anton 对欧洲的讲法不是情绪化自豪。他承认 Europe 离资本、客户和成熟网络更远，是 hard mode；但如果能在这个环境下用极高 velocity 做出全球公司，反而会形成差异化叙事和人才磁场。Lovable 的 Stockholm 叙事不是外宣，它服务于招聘、社区、founder inspiration 和区域生态位：在欧洲成为 AI 应用层最强样本，本身能吸引那些想证明自己不必去硅谷的人。

“从欧洲创业当然会有更多困难，所以我把它看成是在 hard mode 下做一家成功 startup。但如果你能打破人们对如何建公司的常规认知，并且在全球舞台上非常有野心、非常快地做成，尽管有文化差异，尽管离客户侧更深的钱包更远，那么这种差异化、这种打破常规本身会成为优势。这就是我们正在下注的东西。我很兴奋的不只是我们能作为一家公司为欧洲带来差异，而是能激励一代欧洲公司，让他们拥有和我们正在追求的相似级别的 ambition，去构建我们所说的 last piece of software。” —— Anton Osika, Inside AI, 2025-05-21

## Lovable 在 5 月仍然主动招聘，说明增长瓶颈已经从产品验证转向组织承载力

访谈末尾 Anton 提到 Lovable 在欧洲 actively hiring。结合前文的 100K paying、5 万新项目/天、GitHub 过载、安全审查和产品生命周期路线，这个招聘信号说明公司当时已经越过“有没有需求”的问题，进入“组织能不能承载需求、速度和治理”的阶段。它也是后续岗位变化的早期背景：产品、增长、security、enterprise、support 和 infrastructure 都会被业务自然拉出来。

“大家可以去 lovable.dev，也可以直接搜索 Lovable。如果有人有兴趣和我们合作或者加入我们，我可能有时候比较难联系，但我有 Twitter，Lovable 也有 Twitter；我们也在欧洲积极招聘。” —— Anton Osika, Inside AI, 2025-05-21
