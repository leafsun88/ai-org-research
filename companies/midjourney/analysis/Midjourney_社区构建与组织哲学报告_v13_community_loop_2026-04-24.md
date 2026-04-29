---
company: Midjourney
type: organization_philosophy_report
version: v13_community_loop
date: 2026-04-24
status: draft
source_layer: external_reference + selected_evidence
focus: community building + organization
block_style: curated_dossier
---

# Midjourney：社群构建与组织哲学

## 摘要

Midjourney 最值得研究的地方，不止是它做出了一个强图像模型。更关键的是，它先把“共同想象”组织成了一个可运行的社群系统。Discord 在这里承担产品入口、onboarding、学习场、作品展示、support、moderation、审美反馈和模型改进。很多公司会拆成产品、社群、教育、客服、增长和安全团队的工作，在 Midjourney 早期被压进同一个公共空间。

这套社群结构解决的是一个很基础的问题：大多数人单独面对“你可以想象任何东西”时，并不知道自己要什么。Midjourney 把生成过程默认放在公共频道里，让用户看见别人如何 prompt、如何失败、如何选择、如何继续变体。dog、space dog、Aztec space dog 这个早期故事不是段子，它就是产品设计的核心：社群让想象力在彼此的提示词和图像上继续搭建。

社群也改变了 Midjourney 的组织形态。公司可以保持小团队，因为学习、反馈、作品分发和一部分 support 被社群吸收；公司又必须补治理、法务、财务和支持系统，因为超大社群会把算力滥用、色情暴力反馈回路、deepfake 风险、IP 诉讼和 API 边界推到组织中心。Midjourney 的组织更像 founder taste、小团队、GPU 现金流、Discord 社群和内容治理互相咬合起来的 creative operating system。

全文保留组织档案结构，但读法更集中：先解释 David Holz 为什么把 Midjourney 定义成想象力基础设施，再看小团队如何承接超大 Discord 社群，最后看社群规模如何倒逼治理、support 和 moderation 系统化。五个支柱是：humanist infrastructure、founder-led defaults、self-funded small team、community-as-organization、governance as product capability。

## 目录

- 组织哲学：用默认值组织共同想象
- 创立历史：从 Leap Motion 到 Discord 社群
- Founder 的社群洞见
- 小团队如何支撑超大社群
- 社群操作系统：Midjourney 如何把用户组织起来
- 社群治理：规模越大，安全越像产品能力

## 1. 组织哲学：用默认值组织共同想象

Midjourney 的公开语言很稳定：independent research lab、small self-funded team、human infrastructure。这些词限定了公司要做什么，也限定了它暂时不做什么。它没有先融资、先开放 API、先做企业采购软件，也没有把社群拆成传统客服和营销部门。它先做的是一个公共想象空间，让用户在同一套默认值里学习、生成、展示和反馈。

#### 使命陈述

| 表达层级 | 原文 | 来源 |
| --- | --- | --- |
| 使命 | "An independent research lab exploring new mediums of thought and expanding the imaginative powers of the human species." | 
| 文化 | "We're a small, self-funded, fully-distributed team... Come help us scale, explore, and build humanist infrastructure focused on amplifying the human mind and spirit." | 
| 三支柱 | "We are a small self-funded team focused on design, human infrastructure, and AI." | 


### 组织哲学：产品默认值就是社群治理

Midjourney 的组织哲学有三个实际后果，全部都会落到社群怎么运行上。

第一，product taste 是组织中心。David Holz 对默认值很敏感：内容是否默认公开、首页奖励什么、模型偏向什么美学、哪些内容不鼓励，都会改变用户如何学习、社群吸引什么人、模型获得什么反馈。

第二，社群是基础设施。Discord 让用户看到别人怎么想、怎么写 prompt、怎么从 dog 变成 space dog，再变成更奇怪的视觉语言。Midjourney 的社群在生成需求，而不只是承接需求。

第三，商业约束会回到产品纪律。生成运行在云端，用户订阅直接支付推理成本，公司必须在算力、速度、质量和价格之间持续取舍。不融资不是姿态，而是让这些取舍继续由 founder taste、用户体验和现金流决定。


## 2. 创立历史：从 Leap Motion 到 Discord 社群

Midjourney 的创立史不是从 Discord bot 开始，而是从 David Holz 对 Leap Motion 的反向选择开始。Leap Motion 证明过一件很昂贵的事：技术可以非常先进，但硬件、平台、生态和时机没有同时成熟时，组织会被融资叙事、开发者生态和平台想象拖进过早扩张。Midjourney 后来的不融资、小团队、先社群、先现金流，都能从这里找到解释。

### Leap Motion 教训：不要在时机成熟前搭平台

Leap Motion 融过大量资金，也做过硬件、开发者生态和平台合作，但最终没有进入大众日常。Midjourney 几乎反过来：不先搭硬件生态，不先开放 API，不先建立企业销售组织，而是先把一个能立刻使用、立刻分享、立刻付费的体验放进 Discord。这里的组织选择不是保守，而是 Holz 对时机和组织复杂度的重新判断。

> “到后来，Leap Motion 已经大约 100 人，是一个不小的组织，David 也几乎跑了十年，但它还是没有真正工作起来；没有清晰路径能让 Leap Motion 设备进入数百万美国人或电脑用户手里，原始愿景没有合在一起。2019 年他们把公司卖给 UltraHaptics，价格大约 3000 万美元，这对员工、投资人和创始人都不是一个很好的结果。” —— John Coogan, Power Law, 2023-06-20

### 创立母题：先做想象力基础设施，再做图像产品

David 离开 Leap Motion 后，真正想做的不是 AI 画图公司，而是围绕 reflection、imagination、coordination 三个方向建立一个能长期工作的 home。图像生成只是 imagination 先出现了足够好的技术窗口。这个母题很重要，因为它解释了 Midjourney 为什么会把产品做成公共想象空间，而不只是单人设计工具。

> “我其实从来不太想要一家公司，我更想要一个家；Midjourney 对我来说像是未来十年可以待着的地方，和很酷的人一起做我在乎、也希望对别人有益的项目。如果只用三个词概括主题，就是反思、想象和协调；文明要继续繁荣，就必须创造很多新东西，而创造新东西需要这三种能力，也需要围绕它们的新基础设施。” —— David Holz, What Future, 2022-11-10

### 2021：自筹启动，先找想象力入口

- Holz 在 2021 年 8 月离开 Leap Motion / Ultraleap 体系后，以个人资金启动 Midjourney。
- 早期团队约 10 人，重点不是先搭公司机器，而是找一个能承载“想象力基础设施”的产品切口。
- 组织默认值从一开始就是 founder-led、self-funded、小团队和低管理层。

### 2022：Discord open beta 把公开生成变成默认体验

- Midjourney 进入 Discord 私测和 open beta，把“公开生成”变成默认体验。
- Holz 接受 The Verge、The Register、PC Gamer、Forbes 等采访，明确表达 self-funded、research lab、imagination engine 等核心叙事。
- 公开发布后数月内证明订阅收入可以支撑模型推理成本，公司不需要靠免费流量或 VC 叙事换增长。

### 2023：社群出圈后，治理和运营层开始成型

- Discord 社群规模从百万级继续扩张，Colorado State Fair、Pope puffer coat 等事件让 Midjourney 进入大众媒体视野。
- Midjourney 取消 free trial，说明算力成本、滥用治理和 public image risk 已经进入商业核心。
- General Counsel、Chief of Staff、Head of Finance 等岗位陆续补齐，组织开始拥有更明确的运营、财务和治理层。

### 2024：Web 和 hardware 信号出现，控制面开始回收

- Web alpha 从高使用门槛逐步开放，Midjourney 开始把复杂创作控制面从 Discord 收回到自有界面。
- Patchwork、Rooms、Moodboards 等信号说明公司开始从 image bot 走向 creative workspace 和多人世界构建。
- Hardware 方向浮出水面，Ahmad Abbas 的背景让这条线更像真实组织投入，而不是概念扩展。

### 2025：Video 和 IP 诉讼把治理压力推到前台

- V7、Video V1 和 Disney / Universal 诉讼同时出现，说明 Midjourney 从图像工具进入更复杂的创意平台阶段。
- CFO 交接、社群负责人变动、legal 压力上升，显示组织从 founder-led product lab 进入更复杂运营期。

### 2026：Workspace、personalization 和治理压力叠加

- V8、web workspace、personalization、style system、support system 和 API / IP 问题共同推高组织复杂度。
- Midjourney 的问题不再只是生成好图，而是能否把创作流程、社群、算力、治理和权利管理变成稳定平台。


## 3. Founder 的社群洞见

### 1. Imagination over Art：产品目标是扩展想象力

> "We aim to enhance the imaginative capabilities of humanity." — Forbes, 2022/9/16

Midjourney 避开 art 这个词，因为 art 会把讨论带进职业替代、版权争议和机器是否能成为艺术家的老问题。Holz 更愿意把产品定义为 imagination vehicle。这个定义让 Midjourney 不必把自己限制成设计工具、图库工具或 Photoshop 插件，而可以继续围绕“人如何生成想象”扩展。

### 2. Engine, Not Replacement：模型是交互引擎，而非替代者

Midjourney 的基本立场是放大人的 agency，而不是把人的判断交给模型。组织上，这意味着公司需要保留大量 human-in-the-loop 的产品结构：prompt、variation、ranking、style reference、personalization、社群互学和创作者展示。模型不独立完成作品，它更像让人不断选择、修正和发现偏好的引擎。

> "We see this technology as an engine for the imagination." — The Verge, 2022/8/2

#### 交互经验：Midjourney 延续了 Leap Motion 的 interface 思维

2015 年 SVVR 演讲里，David 已经在用很接近 Midjourney 的方式思考界面。他说 Leap Motion 虽然做硬件，但本质上主要是 software company，硬件只是让“手进入计算”发生的载体。他展示 block demo 时强调，真实交互不能只靠 physics engine，也不能只靠 game engine，而要构建介于两者之间的 interaction engine。

这个前史很重要。Midjourney 也在做类似的中间层：它把 prompt、四张图、variation、upscale、ranking、style reference、community learning 串成一个界面，让用户觉得自己在直接操作想象力。

> “在我伸手去抓这个 block 之前，我想说，因为这里并没有真实 block，如果我只用 physics engine，我的手会直接穿过物体；一旦穿过去，physics engine 尽力模拟时，它很可能会从我手里滑走。所以为了让这件事 work，我们必须构建一个完全不同的 engine，不是 physics engine，也不是 game engine，而是介于两者之间的东西，我们叫它 interaction engine。现在你可以看到手指其实有一点在 block 里面，但没关系，我仍然可以驱动这样的 physical interaction。” —— David Holz, SVVR, 2026-04-22

### 3. Beauty as Default：默认审美会塑造社群

这条原则直接塑造产品美学和安全边界。Midjourney 没有把自己设成“用户想要什么都生成”的中性机器，它会在默认审美、名人生成、政治图像、色情、gore 和首页分发上持续做取舍。内容治理在这里不是独立合规问题，而是产品默认值的一部分。

> "The world needs more beauty... I don't think the world needs more deepfakes." — The Register, 2022/8/1

### 4. Society over Business：公司形态服务社会边界

Holz 排斥 CEO 头衔，更偏好 founder，这不是 PR 口径，而是组织结构设计的起点。Midjourney 没有把自己搭成典型 venture-backed startup，也没有先建立可融资、可汇报、可销售的组织形态。它更像 founder 直接管理一个研究产品化系统。

> "I prioritize societal concerns over commercial ones." — Forbes, 2022/9/16

> "The title of CEO feels overly corporate." — Forbes, 2022/9/16

### 5. Home for Ten Years：公司先是长期项目的家

David Holz 对 Midjourney 的第一层定义很反商业化。他没有把公司说成图片生成 SaaS、设计师生产力工具或企业创意平台，而是把它说成未来十年可以和一群人一起做重要项目的地方。这个起点解释了 Midjourney 后来一系列不标准动作：不急着融资、不先做 enterprise、不先开放 API、不把产品压成 Photoshop 插件，也不把路线交给短期增长指标。

Midjourney 的 founder 命题是 reflection、imagination、coordination。图像生成只是 diffusion 先突破出来的切口，背后更像一套让人构造新东西的基础设施野心。

> "It's just about having a home for the next 10 years to work on cool projects that matter." — The Verge, 2022/8/2

> “我其实从来不太想要一家公司，我更想要一个家；Midjourney 对我来说像是未来十年可以待着的地方，和很酷的人一起做我在乎、也希望对别人有益的项目。如果只用三个词概括主题，就是反思、想象和协调；文明要继续繁荣，就必须创造很多新东西，而创造新东西需要这三种能力，也需要围绕它们的新基础设施。” —— David Holz, What Future, 2022-11-10


### 6. Imagining Together：共同想象是社群的核心资产

这是 Midjourney 选择 Discord 而不是独立 iOS app 的根本原因。很多用户单独面对“你可以想象任何东西”时并不知道要什么；在群体里，人会从别人的 prompt 和图像继续搭建。这种共同想象能力，是 Midjourney 社群最核心的组织资产。

> "It's kind of like a hive mind of people, super-powered with technology." — The Verge, 2022/8/2


### 7. Technology Becomes Non-technical：非专业用户才是新行为的入口

David 在 2015 年就说，随着 digital medium 和现实世界融合，technical 会变成 non-technical，原来只有抽象思考者、程序员和工程师能处理的问题，会被有身体直觉、社交直觉、情绪直觉和审美直觉的人处理。Midjourney 正是这个假设在图像创作上的商业化。

它让很多不会 Photoshop、不会摄影、不会 3D、不会写代码的人进入视觉生产。组织上，它也天然偏向 consumer-first 和 community-first，因为真正的新行为常常先出现在非专业人群里，而非预算周期很长的企业流程里。

> “现在很多 technological problem solving 是由 abstract thinkers 完成的；我们处理 nanometer scale 的东西，但作为人类，我们并不和 nanometer scale 的东西互动。可是现在我们正在把 abstract 变成 concrete，所以 physical、intuitive、social、emotional intelligence 也能解决 abstract problems。像 Jane Goodall 这样能探索森林的人，突然也可以探索 brain；以前这种事会被限制给那些能用非常 technical、programmatic 方式操作 computer 的人。于是 technical 变成 non-technical，之后还会出现某种 new technical，而我甚至不知道那是什么。” —— David Holz, SVVR, 2026-04-22


### 8. Taste Formation：Diffusion 的机会是审美来回互动

Midjourney 切进图像生成，不是因为 David 想追 AI art 热词，而是因为 diffusion model 让人与模型之间第一次出现了足够快、足够强的审美来回互动。这里的关键不是模型能不能画 dog，而是用户看见四张候选图以后，如何意识到自己更想要哪一种 dog，如何继续变体，如何在社群里被别人刺激出 space dog、Aztec space dog。

所以 Midjourney 的产品表面是 prompt box，真实操作面是 taste formation。模型质量只是入口，用户如何判断、如何迭代、如何形成审美偏好，才是产品真正的壁垒。

> “大概一年半前，旧金山的 AI 人都在同一些圣诞派对上，大家都在说 diffusion model 好像不一样。我当时想，这里会有一个人类侧的问题，它不只是做图片，而是某种来回互动；里面有很多东西很难通过优化一个程序里的单一数字解决，甚至可能牵涉 taste，而没人真正知道 taste 是什么。我觉得自己在这件事上可能有东西可以贡献。” —— David Holz, What Future, 2022-11-10

### 9. Imagination Vehicle：Midjourney 不该变成自动艺术家

David 有意避开 art 这个词，因为 art 会把讨论带进行业替代、版权防御和“机器是不是艺术家”的老问题。他更愿意把 Midjourney 看成想象力交通工具。汽车比人跑得快，但人不会砍掉腿；生成模型也一样，它扩展人类 agency，不替代人类 agency。

这个隐喻直接影响产品和组织：Midjourney 要优化的是人和模型的共同探索，而不是把人的判断全部外包给模型。它解释了公司为什么早期不追 deepfake 和仿真照片，也解释了为什么 weird、chaos、style reference、personalization 这些“不完全听话”的功能在 Midjourney 里如此重要。

> “我尽量不用 art 这个词，因为它真正关乎的不是艺术，而是想象力；有时人会把想象力用于艺术，但通常不只如此。我更像是在创造一种机器增强的想象能力，有点像 vehicle：汽车比我们快，但我们没有砍掉自己的腿，真要去远处时我们坐车。所以这更像想象力的船、车和飞机，帮助人探索审美可能性的海。” —— David Holz, What Future, 2022-11-10

### 10. Default Values：默认设置会传播创造者价值观

David 把产品默认值看成价值观传播机制。MySpace 默认给你一个朋友 Tom，Facebook 则从“没有朋友”开始，这种细节会塑造社交系统的气质。Midjourney 的 front page、公开生成、禁词、默认模型审美、photo-realism 边界、首页多样性，本质上都带着创造者的价值观。

这意味着 Midjourney 很难完全用传统 PM 指标管理。它需要有人判断什么反馈回路应该被鼓励，什么默认审美会污染社区，什么功能虽然有需求但会把系统带向不想去的地方。

> “我的哲学是，创造者会把自己的价值观注入他们创造的东西，不管他们知不知道，而且这些东西会在创造者不在场时继续传播那些价值。MySpace 一开始就告诉你有一个朋友，那个人是 Tom，是做 MySpace 的人，这会让你觉得这里可以交朋友、Tom 在乎你；但你进入 Facebook 时没有朋友，Mark 也当然不是你的朋友，这些很深的细节都是带着真实价值观的人做出来的。” —— David Holz, What Future, 2022-11-10


## 4. 小团队如何支撑超大社群


Midjourney 没有公开完整 org chart。公开材料能看到的是一个 founder-led、小管理层、低 title 密度的组织：David Holz 仍在产品、治理和方向判断中心；Chief of Staff、Legal、Finance、Hardware、Community / Support 围绕这些约束补位。对这家公司来说，组织结构不能只按内部汇报线理解，还要看哪些工作被 Discord 社群吸收，哪些工作又因为社群过大而回到公司内部。


#### 公开资料下的功能架构图

下图根据 Midjourney 旧版团队页、LinkedIn、TheOfficialBoard、Crunchbase、公开职位和访谈材料整理，只代表公开资料能看见的功能分布，不等同于内部正式汇报线。更准确的读法是：Founder 仍在产品方向、默认值和治理中心；工程研究、硬件、legal / finance、community / support / moderation 围绕约束展开。

#### 核心人物

| 姓名 | 岗位 | 公开职业介绍 |
| --- | --- | --- |
| David Holz | Founder | Midjourney 创始人。此前共同创立 Leap Motion 并任 CTO；公开履历还包括 NASA Langley Research Center 和 Max Planck Institute 的研究经历。这个背景解释了 Midjourney 为什么一直把“界面、交互、想象力扩展”当成同一件事。 |
| Caleb Kruse | Chief of Staff / Operations | 公开资料列为 Midjourney Chief of Staff。早年在 Leap Motion 也以 Chief of Staff 身份参与 Interaction Engine / Blocks 演示，是 David 硬件与交互时代延续到 Midjourney 的运营协调层。 |
| Ahmad Abbas | Head of Hardware | 2023 年底加入 Midjourney 任 Head of Hardware。此前五年多参与 Apple Vision Pro 硬件开发，短暂任职 Neuralink，更早在 Leap Motion 做硬件工程。这个履历让 Midjourney 的 hardware / 3D data capture 信号更像真实投入，而不是概念扩展。 |
| Max Sills | General Counsel | Midjourney General Counsel。公开会议 bio 显示，他曾领导 Google 的 open source legal team，也创办 Open Advising PC，为早期 AI 公司提供嵌入式法律团队。这个岗位对应的是版权、开源、AI IP、诉讼和 API / 平台治理压力。 |
| Amy Kux | CFO | 第三方高管目录列为 Midjourney CFO；LinkedIn 公开页显示她是有 20 多年经验的 startup finance / operations executive。这里更适合把她理解为 Midjourney 财务职能专业化的公开信号。 |
| Bhavin Patel | Head of Finance / FP&A | 公开资料显示其在 Midjourney 负责 finance / FP&A；此前曾任 MoonPay VP of FP&A、Included Health Strategic Finance，并有 Autodesk、PwC 等财务分析经历，Wharton MBA / CFA 背景。对应订阅收入、GPU 成本、treasury 和财务规划。 |
| Erik Martin | Community / Former Head of Community | 长期社群组织者。Community Club 与 SF New Tech 等公开资料显示，他曾服务 Reddit、Depop、Nike、WeWork、Teal、Commsor 等 community-powered businesses，并与 Midjourney 社群岗位相关。这个背景对应 Discord 社群、guides、moderation 和用户信任。 |
| Philip Rosedale | Advisor | Midjourney 早期 advisor。Second Life / Linden Lab 创始人、RealNetworks 前 CTO、High Fidelity 创始人之一。这个履历把 Midjourney 的“共同想象”和虚拟世界 / 用户生成经济传统连在一起。 |

#### 结构性说明：内部小团队与外部社群共同构成组织

公开材料显示，Midjourney 的组织不像典型“创始人 + CTO + COO + VP Engineering + Sales”的公司化形状。它的中间层少，且很多关键岗位围绕约束而生：GPU 现金流需要 finance，IP 和输出风险需要 legal，hardware 需要现场工程，超大社群需要 support 和 moderation。新的 executive / project management 信号可以作为待核验项，但不在这里承重。

### 10 人团队同时背模型、社群和治理，早期没有职能缓冲层

2022 年 office hours 里，Midjourney 最真实的状态是一支约 10 人团队同时处理当前模型、下一代模型、web 功能、组织流程、网页创作流程、Discord 社群和内容安全。这种组织还不是清晰职能分工后的产品机器，而是 founder 直接把技术路线、用户反馈、社群治理和商业约束放在一起取舍。

这解释了 Midjourney 为什么能快，也解释了为什么时间表经常不确定。小团队的效率来自判断链短，但代价是所有关键主题都挤在少数人身上。

> “我们现在大概只有 10 个人，所以有时候真的很挣扎；一边要把当前系统调好，一边要准备下一代系统，还要分心做网页功能、组织流程、网页创作流程和一些还不能讲的新功能。问题不是我们不知道方向，而是内部同时有很多东西都看起来又热、又好、又重要，我们很难把自己砍到更少的事项上。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

### David 的小组织理论：知识劳动不随人数线性扩张

David 对组织规模的判断很极端：知识劳动组织的有效性大致按人数的对数增长。这个判断不一定适用于所有公司，但很适合 Midjourney 的业务结构。Midjourney 可以大规模扩张 GPU 成本，因为订阅收入能覆盖；它不必同步扩张 headcount，因为模型、社群、Discord / web 界面和自动化基础设施承担了很多杠杆。

如果把收入增长只理解成人效高，会错过机制。Midjourney 是把成本放进 GPU，把学习放进社群，把审美判断放进 founder 和用户反馈，把一部分 support 放进社群互助。

> “David 非常专注于保持组织小。他说，对 intellectual labor 来讲，一个组织的有效性大致按人数的对数增长；这意味着 1000 人可能只比 100 人有效两倍，而一个 10000 人公司可能比 100 个 100 人公司低效 25 倍。所以保持组织小非常关键，但这不意味着成本结构不能扩张，他们显然花了很多钱在 GPU 上，只是 subscription 会为这些 GPU 付费。” —— John Coogan, Power Law, 2023-06-20

### 小团队纪律来自 Leap Motion 的昂贵教训

Leap Motion 到后期约 100 人，融资、硬件合作、开发者生态和平台叙事都做过，但原始愿景没有进入大众日常。Midjourney 几乎把这条路反过来：先不造硬件，不先做 App Store，不先开 API，不先给企业采购周期做定制，而是把核心体验放到 Discord 里，让用户立刻使用、学习和付费。

这不是创始人迷信小团队。它来自一次昂贵经验：过早平台化、过早组织膨胀和外部生态不成熟，会把技术愿景拖进太复杂的组织负担。

> “到后来，Leap Motion 已经大约 100 人，是一个不小的组织，David 也几乎跑了十年，但它还是没有真正工作起来；没有清晰路径能让 Leap Motion 设备进入数百万美国人或电脑用户手里，原始愿景没有合在一起。2019 年他们把公司卖给 UltraHaptics，价格大约 3000 万美元，这对员工、投资人和创始人都不是一个很好的结果。” —— John Coogan, Power Law, 2023-06-20


## 5. 社群操作系统：Midjourney 如何把用户组织起来

Midjourney 最特殊的地方，是把社群变成组织的一部分。Discord 同时承担用户意图生成、学习、support、QA、传播、moderation、审美反馈和模型改进。很多公司会拆成产品、客服、教育、研究、市场和安全团队的事，在 Midjourney 这里被压进同一个社群操作系统。

### 150 万 Discord 用户把社群变成产品实验场

2022 年 David 已经把 Midjourney server 说成世界最大的 Discord server，并公开向用户征集如何让巨大 server 变好的建议。这不是普通 community management，它更像一个和 Discord 平台共同扩容的组织实验：Midjourney 的用户规模、频道结构、反馈收集、规则执行和基础设施 bug，都在逼 Discord 和 Midjourney 一起学习超大社群怎么运行。

这解释了为什么 Midjourney 的社群能力很难被简单复制。别人可以接 Discord bot，但很难复制一个已经把 prompt 学习、作品展示、用户支持、moderation 和模型反馈压在同一个巨大公共空间里的操作系统。

> “Discord server 已经到 150 万了，我们现在是世界上最大的 Discord server，而且很快可能比后面几个最大的加起来还大。随着服务器变大，事情会变得有点奇怪，因为 Discord 也没有见过这么大的社区；如果有人知道怎样让一个巨大 server 变得更好，请把想法丢到 feedback channel，我们真的会读。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

### 社群先解决想象力问题：用户需要彼此启发

Midjourney 用 Discord 做前端，常被理解成临时低成本方案。David 的核心判断更深：大多数人单独面对“你可以想象任何东西”时不知道自己要什么；群体会让想象力在彼此想法上继续搭建。

这就是 Midjourney 社群的第一性价值。它先让用户在群体里发现自己可以要求什么，再把用户带到模型面前。

早期测试里的 dog、space dog、Aztec space dog，是这个设计的原型故事。公共频道的价值不止是展示结果。它让一个人的普通意图，被另一个人的扩展、第三个人的审美跳跃推成新的视觉语言。

> “如果你把他们放进一个 group，他们会说 dog，别人会说 space dog，再有人会说 Aztec space dog；突然之间，人们理解了可能性，你就在创造一种增强想象力的环境。” —— David Holz, The Verge, 2022-08-02

> “David 在 The Verge 采访里的说法是：我们去年 9 月开始测试 raw technology，很快发现大多数人并不知道自己想要什么。你说，这里有一台机器，你可以用它想象任何东西，你想要什么？他们说 dog；你说真的吗？他们说 pink dog。于是你给他们一张狗的图片，他们说 okay，然后就去做别的事了。但如果你把他们放进一个 group，比如 Discord server，他们会说 dog，别人会说 space dog，再有人会说 Aztec space dog；在 community setting 里，人们会在彼此的想法上继续搭建。” —— No Text To Speech / David Holz via The Verge, YouTube, 2026-04-21

### Discord 的价值是让学习发生在同一个房间

Discord 给 Midjourney 提供了移动端、桌面端、图片展示、结果按钮、slash command、bot 和可扩展基础设施。更关键的是，它本来就是协作环境。用户能看到自己的生成结果，也能看到别人怎么写 prompt、怎么选择、怎么继续迭代。

很多人把 Discord 理解成早期没有资源做 App 的折中方案，但 Holz 的判断更像产品哲学：如果做一个 iOS 单机生成器，公司就必须自建社交网络；如果放在 Discord 里，用户天然在同一个房间里观看、模仿、提问和扩展彼此的 prompt。Discord 给 Midjourney 的不是流量，而是共同想象的场地。

> “很多人问我们，为什么不直接做一个能生成图片的 iOS app？但人们想一起做东西；如果你在 iOS 上做这件事，就必须自己做一个社交网络，而那非常难。” —— David Holz, The Verge, 2022-08-02

这正好解决了 Alan Kay 当年给 David 的问题：不要只想 feature，要想用户怎样学习。

> “Discord 对这门生意有几个很强的地方：首先它是预制、可扩展的前端，移动 app 开箱即用，很多人低估了在 iOS 和各种设备上做一个好键盘有多难；Discord 支持图片、结果下面的按钮、slash commands、bots，桌面和移动都能用。更重要的是，它是协作环境，用户进聊天室看到别人做东西，立刻能复制 prompt，再做自己的版本。” —— John Coogan, Power Law, 2023-06-20

### 默认公开把每次生成变成公共教材

Midjourney 的默认公开不是普通社群设置，而是学习系统的基础。新用户能看到别人如何写 prompt、如何迭代、如何把一个普通意图推进成有审美方向的图像。Stealth Mode 只有更高付费层级才开放，也让“公开生成”从默认选项变成社群规范：大多数创作先进入公共学习池，商业和隐私需求再额外付费。

> “如果你需要隐私，那通常意味着你是某种商业用户；所以我们把私密模式放在更高的付费层级里。” —— David Holz, The Verge, 2022-08-02

### Slash command 和新手区把学习变成现场表演

Midjourney 的 slash command 不是纯技术接口，而是公共频道里的社交动作。/imagine 让每次创作都成为可被观看的事件，/blend 和 /describe 让二创和逆向学习变得自然，U / V 按钮把“选择和变体”显性化。新手区则把这些动作浓缩成学习剧场：新人不是先读文档，而是先看大量陌生人怎样提问、失败、重试和变好。

| 机制 | 表面功能 | 社群作用 |
| --- | --- | --- |
| /imagine | 文生图，生成四张候选 | 把个人意图变成公共事件，其他人可以即时学习 prompt。 |
| /blend | 合并多张图片 | 降低二创门槛，让图像风格可以被继续搭建。 |
| /describe | 上传图片反推 prompt | 把风格学习和 prompt 逆向工程变成产品能力。 |
| U / V 按钮 | 放大或变体某张图 | 让审美选择、偏好形成和迭代路径在公共频道可见。 |
| Newbie rooms | 分流新用户 | 用高密度公共生成替代传统 onboarding。 |

> “新手频道的优势是，你可以看到其他人怎样 prompt，并从他们那里学习。” —— ASLA tutorial, cited in AI Community Building Report

### Daily Theme 和 Office Hours 把回访习惯做进社群

Daily Theme 让用户每天有一个回来的理由，Office Hours 则让产品方向和 founder 判断直接暴露在社群里。每周 David 花数小时在 Discord Stage 回答问题，这不只是客服或公关，而是路线图预告、产品测试、治理解释和信任积累的复合机制。

> “我们会做 office hours，我会在语音里坐四个小时，和大概一千个人一起回答问题。” —— David Holz, The Verge, 2022-08-02

### 新手、审美和反馈一起进入产品循环

#### 先降低进入门槛，社群才有规模


Midjourney server 的规模不能按普通 Discord server 理解。新用户会被分到不同 group，只看到有限 newcomer rooms。这样做是为了让大量不熟 Discord 的普通用户也能进入。这个结构说明 Midjourney 的社区运营已经是产品 onboarding 的一部分。

加入门槛也被刻意压低。Midjourney 没有简单套传统 captcha / verification，因为任何摩擦都会挡住普通用户；但它又必须处理 bot 和免费滥用，因为每次滥用都在消耗服务器成本。

> “Midjourney server 非常独特，因为你加入服务器时会被分到不同 group；比如我看这个用户，他在 group four，这意味着他只能看到非常有限的一部分 newcomer rooms。我认为服务器里大概有 200 个 newcomer rooms，但因为这个产品被很多媒体宣传过，从 Daily Dose of Internet 到 John Oliver，很多不熟 Discord 的人都会进来，所以这个 Discord server 必须对新用户相对友好，这也是为什么他们让用户可见的频道更少。” —— No Text To Speech, YouTube, 2026-04-21

#### 用户也是审美数据的提供者

Midjourney 的数据闭环不是简单吞自己的生成图。David 把分工讲得很清楚：互联网教模型概念，用户教模型 beauty、expression 和 what people actually want。用户生成、选择、喜欢、ranking、变体和放弃，都是审美反馈。

> “图片本身来自互联网；用户生成的图主要不是用来教它猫是什么。如果系统已经能画猫，它不需要再看自己生成的猫来学习猫；但如果有某张猫的图片大家都特别喜欢，那就教会它一些东西。所以互联网教它概念，用户更多是在教它 beauty、expression，以及人们真正想要什么。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

### Ranking system 把社群选择转成模型改进

Midjourney 的 Ranking system，是一整套把用户审美选择收集起来，再送回产品和模型的偏好数据系统。按 Midjourney 现在的官方文档，它至少包含三类图像任务：选喜欢的图来建立 Personalization 数据；给 Explore 页面的内容投票；在新版本发布前做二选一评分，用来帮助新模型 fine-tune 和 calibrate。

社群本身就是构建产品的重要组成。这说明 Midjourney 的产品、社群和模型研发不能被拆成孤立部门。前端上的一次排序，可能同时影响用户体验、社群分发和模型训练。Midjourney 的组织也很难按普通“research + product + community”三段式理解，因为社群行为本身就是研发输入。

> “我们试着改了一些 ranked images 的工作方式，因为有机会从里面拿到更多数据；现在还不知道能不能成功，所以如果大家看到 rank image 有什么问题，请告诉我们。这个 ranking system 很实验性，但如果它跑得好，可能会同时改善算法表现，也让 ranking 本身变得更好。” —— David Holz, Midjourney Office Hours, 2023-07-26

### Front page 分发规则决定社群审美宽度

Midjourney 首页不是简单 gallery。David 2023 年提到调整 front page 规则，让同一个人的图片不能连续占据太多位置，避免首页被少数用户接管。这个细节很小，但结构影响很大：分发规则会塑造用户学习路径、审美趋同程度和模型反馈宽度。

如果首页只奖励少数重度用户，社群会变窄；如果分发更丰富，用户看到的可能性、prompt 学习和审美反馈都会变宽。

> “我们稍微收紧了 front page 的规则，让你不会在首页看到同一个人的两张以上图片。之前首页有时会被少数人接管，现在结构上已经不可能了，我觉得这让 front page 更丰富。我们还在为未来版本做更复杂的首页算法，希望它能好很多；我们正在投入很多精力思考，怎样让人更容易探索其他人在 Midjourney 上做出的图片。” —— David Holz, Midjourney Office Hours, 2023-07-26

#### 三次出圈把公共图片变成增长渠道

Midjourney 的增长不是广告买出来的，而是公共生成本身制造了可传播事件。Colorado State Fair 把 AI art 推进艺术争议，Pope puffer coat 把 V5 的照片级真实感推给大众，关闭 free trial 则把增长边界转成品牌和治理信号。每一次出圈都在放大同一个机制：用户生成的公共图像会替公司做传播，公司再用治理和付费墙守住系统。

| 时间 | 事件 | 增长/组织影响 |
| --- | --- | --- |
| 2022 年 8-9 月 | Colorado State Fair 获奖争议 | 把 Midjourney 从创作者圈带进大众媒体和艺术争论。 |
| 2023 年 3 月 | Pope puffer coat 病毒传播 | V5 能力被大众看见，同时 deepfake 风险被放大。 |
| 2023 年 3 月 | 暂停免费试用 | 算力成本、trial abuse 和全球流量暴增迫使公司守住付费边界。 |

> “Due to a combination of extraordinary demand and trial abuse we are temporarily disabling free trials.” —— David Holz, 2023-03-28

### 规则是在选择社群会长成什么样

Midjourney 对 porn、gore 和 shock image 的治理逻辑非常产品化：允许什么，什么就会形成反馈回路，进而吸引对应人群、驱逐另一批用户。David 不把 moderation 讲成抽象价值观，而是讲成 social system design。

这解释了为什么 Midjourney 的安全治理从早期就和社群、模型、前台展示和默认审美缠在一起。它要做的是安全的通用艺术探索空间，不让最高刺激反馈占据整个系统。

> “我们必须非常小心 feedback loop，因为如果有人做很血腥的内容，所有喜欢血腥的人都会来，然后大家都在做 gore；色情也是一样。很多社交网络会被它们允许的反馈回路主导，我们不想让这个系统被最糟的反馈回路主导。总有人会做 AI porn 服务，但我们更想做一个安全空间，聚焦一般性的艺术探索。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## 6. 社群治理：规模越大，安全越像产品能力

Midjourney 的治理不是独立后台职能，而是产品能力。它要同时处理开放社群、算力滥用、色情和暴力反馈回路、API 扩张、Hollywood IP、专业用户版权和未来 licensing。难点在于，很多风险正好和用户付费价值绑定在一起。


#### 风险如何改变组织

Midjourney 的风险不能只看“法务会不会赢诉讼”。真正的问题是：当公司从 Discord 社群和订阅产品走向 API、品牌授权、专业工作流和平台合作时，过去靠 founder、moderators、社群默认值和词表维持的治理方式，能不能变成可审计、可授权、可规模化的产品系统。

### API 被延后，是因为社群治理还不能外溢

2023 年 David 对 API 的回答非常关键。Midjourney 暂时不做 API，不是因为没有需求，而是因为要先解决 moderation。一旦开放 API，公司就不只要管理自己平台上的用户，还要管理 API service 里的使用。

这句话把商业上限和组织瓶颈连在一起。API 能带来更大分发和收入，但如果治理系统没有规模化，它会把外部风险带进公司。

> “我们现在没有计划做 API。我觉得我们得先解决 moderation，因为一旦有 API，我们就不只是管 Midjourney 自己平台上的用户，还要去管 API service 里的使用；我们现在没有时间同时 moderation 这两边。如果以后有 API，我们也许会赞助 hackathon，但现在大概会先按住。” —— David Holz, Midjourney Office Hours, 2023-07-26

### 早期安全治理靠实时社群操作，不靠政策文件

Midjourney 不是等到 Disney / Universal 才开始治理。2022 年 David 已经每周做四小时 office hours，直接和用户讨论边界；遇到 bikini 图片争议，他拉了 12 位女性做 panel，并按她们结论把默认展示改成隐藏；同时有约 40 个 moderators 可以用 slash ban 快速处理词语。

这条证据很组织化：Midjourney 早期治理不是单纯政策文件，而是 founder、用户代表、moderators、词表、展示默认值和模型行为共同组成的实时操作系统。它能支撑社群阶段，但未必天然支撑 API、品牌客户和全球 IP 授权阶段。

> “我每周做四个小时 office hours，尽量和很多人直接聊；有一次我拉了十二位女性上来，问她们对 bikini 图片怎么看，要不要禁，我说会照她们说的做。她们几乎一致说不要禁 bikini，但希望把它们隐藏起来，不要让我们被迫看到某些男人生成的 bikini 图，于是我们就这么做了；同时我们有大概 40 个 moderators 盯着，他们有 slash ban 命令，可以马上让某些词不能再用。” —— David Holz, What Future, 2022-11-10

### Support 和 moderation 必须变成可积累系统

2023 年 David 对 help site 和客服的描述，说明 Midjourney 已经意识到社群规模不能只靠即时答疑。几百万用户不可能都获得实时 support，正确方向是把新问题沉淀进 FAQ、搜索、文档和客服流程，让系统随着回答变好。

这是从社群公司走向平台公司的关键组织转化：把原本依赖 moderators、office hours 和社群热心人的知识，沉淀成可搜索、可复用、可训练新用户的支持系统。

> “我们也在做新的 help 网站，可能会是 midjourney.com/help 之类的东西，里面会有很多文档、好用的搜索；如果找不到答案，也可以联系 Midjourney 的客服拿到回复。它不会是实时的，我不觉得以我们现在的规模还能给几百万用户做实时支持；但我们会有团队回答问题，并且每当他们回答了 FAQ 里没有的问题，就把它加进去。我们想把 moderation 和答疑系统化，让它们随着时间变好，而不是像现在这样只是一直在那里、不会积累。” —— David Holz, Midjourney Office Hours, 2023-07-26

### 理想的 moderation 是让模型理解边界

David 2022 年对 moderation 的目标讲得很清楚：长期不是靠越来越长的词过滤，而是让模型理解 nude、blood、gore、冒犯性输出之间的细微差别。也就是说，治理不只是 policy team 的工作，也不是 community team 的工作，它必须进入模型训练和输出控制本身。

这对 Midjourney 的组织要求很高。它需要把 trust & safety、model behavior、用户申诉、社群反馈、法律风险和产品体验接在一起。如果做成，安全会成为模型能力的一部分；如果做不成，API、enterprise、IP licensing 都会被卡住。

> “目标应该是几乎没有词过滤，除了 slur 之类的词以外，你可以有语言自由，但图像仍然不会变成冒犯性的东西。比如你要求 nude person，它可能会做裸露感，但用树枝或物体挡住关键部位；它可以有 blood，但不做 gore。我们需要让系统学会这些细微差别，随着它学得更好，过滤就能慢慢放松。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07
