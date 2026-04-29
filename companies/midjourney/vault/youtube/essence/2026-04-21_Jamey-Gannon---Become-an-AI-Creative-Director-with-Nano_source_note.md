---
company: midjourney
source_type: youtube
type: source_note
status: done
source_path: companies/midjourney/vault/youtube/transcripts/2026-04-21_Jamey-Gannon---Become-an-AI-Creative-Director-with-Nano.md
source_title: "Jamey Gannon - Become an AI Creative Director with Nano Banana and Midjourney"
source_date: 2026-04-21
created_at: 2026-04-22
speaker: "Jamey Gannon / Ridd"
source_weight: A
relevance: high
quote_language: zh_translation_from_en_transcript
---

# Jamey Gannon / Become an AI Creative Director — Source Note

## AI 创意工作的核心从 prompt skill 转向 direction skill

Jamey 把 AI creative director 的问题定义得很清楚：多数人失败不是因为 prompt 不够长，而是没有方向、不知道要做什么、给错信号、用错模型。这个判断对 Midjourney 很关键，因为它把产品使用从自然语言操作升级为创意管理能力。Midjourney 的重度用户不是 prompt engineer，而是能把视觉方向、reference、模型分工和审美判断串起来的人。

“我觉得大多数人用 AI 做不好主要有三个原因：第一是缺少方向，不知道自己到底要做什么；第二是过度提示，没有给 AI 正确的信号；第三是用错工具、用错模型或者用错方式。所以我常说 AI 是 direction problem，不是 prompt problem。” —— Jamey Gannon, Dive Club, 2026-04-21

## 图片参考比文字提示更强，因为模型比人更会读取潜在视觉信息

Jamey 用 Hailey Bieber 图像解释了为什么图片是一千个词。人类可能只说红背景、卫衣、性感姿势，但 LLM / vision model 会读取衣服质地、发丝、肤色、戒指、表情、墙面质感等大量 latent information。她的结论是，试图用文字穷尽视觉信息是输给模型的战斗；更好的方法是把 mood board、style references 和 image references 作为主要输入。Midjourney 的用户教育重点因此应该是视觉输入，而不是 prompt 模板。

“如果把一张 Hailey Bieber 的图交给 ChatGPT 或 Gemini，让它极细地描述并写 prompt，它能写出三段，提到卫衣的厚度、戒指、肤色、头发落下来的方式和表情；人当然也能练到很会说，但你永远不会比模型更擅长把这些潜在视觉信息读出来并使用它。” —— Jamey Gannon, Dive Club, 2026-04-21

## Mood board、SRF 和 personalization code 构成了 Midjourney 的专业调参层

Jamey 的流程从方向和 mood board 开始，再根据输出偏差切换到 SRF、去掉污染色、叠 profile code。她把 personalization code 形容为通过排名图片向 Midjourney 注入自己的审美，让输出不只停留在 mood board 平均值上。这里的采用证据是，Midjourney 专业用户已经形成一套不依赖官方说明的 tacit operating system，用视觉投票、参考图组合和反复对照来控制风格。

“我会先从方向和 mood board 开始，把图片复制到 Midjourney 的 mood board 里生成一个 style code；但 mood board 有时会把图片平均掉，所以我会把同样的图片作为 style references 放进 prompt，再去掉导致画面过绿的那张图，之后叠上我为 2025 aesthetic 做的 personalization code，让结果更 crisp、更真实，也更像我自己的审美。” —— Jamey Gannon, Dive Club, 2026-04-21

## Midjourney 是 aesthetic engine，Nano Banana 是 reasoning edit engine

这条访谈给出很清晰的模型分工语言：Midjourney 是 aesthetic engine，负责让东西有感觉、不像普通 AI 图；Nano Banana Pro 是 reasoning engine，擅长听指令、现实感和文字。这个分工本身就是 AI 创意 stack 的市场结构信号：Midjourney 在高端品牌工作流中的角色不是全能工具，而是最重要的视觉风格源头，后续编辑、文字和精确替换由其他模型补齐。

“我 90% 的时间用 Midjourney 和 Nano Banana Pro；Nano Banana Pro 是 reasoning engine，擅长听指令、现实感和文字，甚至整页文字都能很准，而 Midjourney 是 aesthetic engine，它能做出真的有感觉的东西，不会一直像那种 stark AI 图。” —— Jamey Gannon, Dive Club, 2026-04-21

## 专业 AI 编辑要一步一步做，overprompting 会杀掉可控性

Jamey 在 Flora / Nano Banana 里修 runners 图的过程，是很好的 professional workflow 证据。她不会一次要求模型改鞋、改袜子、改短裤、保留女性、改男生、保留构图，而是分步操作，每次只要求一个明确变化。这个原则把 AI 编辑从掷骰子变成可控生产：Midjourney 负责好的起点，后续模型负责小步、可验证的修正。

“如果我要修这张跑步者图片，我会一步一步做，比如先说把男人的鞋和袜子换成黑色；这样模型一次只需要听一件事，结果会好很多。很多人卡住是因为他们期待模型同时理解太多要求，鞋是白的、短裤是灰的、不要改女人、只改男人，过度提示会把生成毁掉。” —— Jamey Gannon, Dive Club, 2026-04-21

## 可交付的一致性来自 master prompt，而不是单张漂亮图

Jamey 把可用于品牌的 AI 工作定义为 master prompt：包含参数、reference photos、image reference、profile codes 等，可以让客户用一个词生成相近风格的 cat、dog 或产品图。这个交付方式很像品牌系统而非图片库。Midjourney 的 professional adoption 因此具有产品化潜力：creative director 把隐藏在自己操作里的 reference system 变成客户可复用的生成接口。

“我努力得到的是一个 master prompt，也就是所有参数、参考照片、可能的 image reference 和 profile codes；有了它，品牌方可以直接复制使用，甚至只输入 cat 或 dog 这样一个词，也能得到大概率符合这个品牌视觉系统的结果，这比只交付一个漂亮 one-shot 更有用。” —— Jamey Gannon, Dive Club, 2026-04-21

## AI designer 这个标签有时间窗口，长期会变成默认能力

Jamey 对个人业务定位的判断很适合做 market adoption 证据。她认为未来 6-12 个月，把自己定位成 AI designer 仍有商业价值，因为客户知道 AI 能带来以前做不到、或能省时间省钱的产出；但长期说自己是 AI designer 会像说自己是 Figma designer 一样多余。这个变化说明 Midjourney adoption 会从差异化卖点进入行业基础设施阶段，早期掌握者先拿到溢价。

“接下来 6 到 12 个月，把自己说成 AI designer 可能是有利的，因为现在来找 AI 工作的人知道它能做以前不可能的东西，或者能帮他们省很多钱和时间；但最终这会像说自己是 Figma designer 一样奇怪，因为 Figma 已经是标准，AI 也会变成标准。” —— Jamey Gannon, Dive Club, 2026-04-21

## 稀缺性回到 creative direction：参考从哪里来、为什么选、如何判断仍是人的能力

访谈后半段强调 taste 和 reference repertoire。Jamey 说真正好的 AI 图像来自日常的 mood boarding、Pinterest / Cosmos 归档、跨领域文化输入、电影、时尚、烹饪、音乐和旅行。AI 把执行速度放大，但没有替代创意总监对参考、气质和故事的选择。对 Midjourney 来说，这解释了为什么专业用户会持续付费：工具越强，越能放大已有审美资产。

“如果你想靠视觉谋生，taste 必须成为生活的一部分；我一直在 mood boarding，手机和浏览器里都有 Pinterest、Cosmos 插件，看到购物网站、X、Instagram 甚至一个蛋白冰淇淋帖子里有酷的画面，我都会存下来。真正让你成为 creative director 的不是读一本教科书，而是电影、文学、音乐、时尚和生活经验变成你的 reference repertoire。” —— Jamey Gannon, Dive Club, 2026-04-21

## AI 改变独立设计师的公司形态，小团队可以吃掉原来 agency 的一部分经济性

Jamey 对 agency route 的反思，是 AI-org 视角里很有价值的组织证据。传统品牌设计师要扩大收入，常被建议开 agency；但 agency 会带来销售、项目管理、B player、薪资压力和毛利稀释。AI 让独立创意人或极小团队能承接更高价值项目、保留更多收入、保持控制权。这是 Midjourney 对服务业组织形态的影响：它让高 taste 的 solo operator 更像微型工作室，而不是必须扩成人海 agency。

“以前大家总说你应该开 agency、招人、接更多客户，但对品牌设计师来说，找一个 junior 很难，合同只有一万到一万五美元时，找人帮忙基本就是把项目拆掉；现在如果你很 lean，可能只需要一个 contractor，甚至自己加 AI，就能接五万美元项目，保留大部分钱，也不用背 payroll 和持续找客户的压力。” —— Jamey Gannon, Dive Club, 2026-04-21
