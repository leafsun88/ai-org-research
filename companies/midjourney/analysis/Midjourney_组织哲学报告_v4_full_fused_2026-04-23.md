---
company: Midjourney
type: organization_philosophy_report
version: v4_full_fused
date: 2026-04-23
status: current
source_layer: external_reference + source_note
focus: organization
block_count: 50
reference_preservation: full_body
---

# Midjourney 组织哲学与架构研究报告

**研究日期：** 2026 年 4 月
**研究范围：** 官方资料、David Holz 访谈、LinkedIn、TechCrunch 等媒体报道、startup databases（Contrary Research、Crunchbase、Levels.fyi、Stanford CRFM 等）
**语言说明：** 中文主体叙述，保留英文专有名词（人名、公司名、产品名、岗位名等）。

---

## 一、执行摘要（Executive Summary）

Midjourney 是全球生成式 AI 领域一家极为罕见的组织实验样本。它在 2026 年估算年化收入接近 $500–600M，却只有约 **107–163 名员工**（Quantumrun、The Agent Times, Apr 2026），零外部融资，没有董事会，没有公开的 CTO/COO/VP Engineering。创始人 David Holz 将其定义为 **"an independent research lab exploring new mediums of thought and expanding the imaginative powers of the human species"**（Midjourney 官网），而非一家传统意义上的 startup。

这份报告将 Midjourney 的组织特征归纳为七个核心支柱：

1. **Humanist Infrastructure 使命** — "expanding imaginative powers"，而非 "building God"
2. **Self-funded、无 VC** — Holz 用个人资金起步，2022 年即已盈利
3. **极度扁平、极度精简** — 人均年收入约 $4.6M，全球软件行业顶级水平
4. **Community-as-Organization** — Discord 社区同时是产品、训练数据源与准组织层
5. **Leap Motion Alumni 信任圈** — 核心高管多来自 Holz 上一家公司
6. **Distributed + SF Core 双轨制** — Hardware 团队 SF 在岗，其余可远程
7. **AI 内嵌于 workflow** — Community signals 直接驱动模型迭代，Discord Office Hours 取代 PR 层

---

## 二、组织哲学（Philosophy Summary）

#### 2.1 使命陈述的三重官方表达

| 表达层级 | 原文 | 来源 |
|---------|------|------|
| Homepage 使命 | "An independent research lab exploring new mediums of thought and expanding the imaginative powers of the human species." | midjourney.com |
| Careers 文化 | "We're a small, self-funded, fully-distributed team... Come help us scale, explore, and build humanist infrastructure focused on amplifying the human mind and spirit." | Midjourney Jobs |
| About 三支柱 | "We are a small self-funded team focused on **design, human infrastructure, and AI**." | Midjourney About |

这三句话构成 Midjourney 的"宪法"：它刻意避开 "AI company"、"startup" 这类词，而用 **research lab** 与 **human infrastructure** 自我定义。

#### 2.2 Holz 的六条核心信念（Leadership Principles）

尽管 Midjourney 从未公开发布 values framework，但综合 Holz 在 The Verge、Forbes、The Register、PC Gamer、Nathan Ma 访谈中的一贯表达，可以提炼出以下六条隐性 leadership principles：

**① Imagination over Art（想象力优先于艺术）**
> "We aim to enhance the imaginative capabilities of humanity. Our objective is to foster human creativity rather than to create machines that are imaginative, which is a crucial distinction." — Forbes, 2022/9/16

产品不是为了生成艺术，而是服务 "imagination" 这个更根本的人类能力。

**② Engine, Not Replacement（做引擎，不做替代者）**
> "We see this technology as an engine for the imagination... Cars are faster than humans, but that doesn't mean we stopped walking." — The Verge, 2022/8/2

AI 是放大器不是替代者，这是公司回应 artist backlash 与 Disney/Universal lawsuit 的基本立场。

**③ Water, Not Tiger（AI 是水，不是老虎）**
> "People see AI as a tiger... but the danger of a flowing river of water is very different... We're making surfboards rather than making water." — The Verge, 2022/8/2

AI safety 不是靠禁止，而是靠教人"游泳、造船"——这塑造了 Midjourney 相对宽松、community-led 的内容治理哲学。

**④ Beauty as Default（美是默认目标）**
> "The world needs more beauty... I don't think the world needs more deepfakes." — The Register, 2022/8/1

这一原则直接塑造了产品的美学偏好（反 photorealism、反 deepfake）、内容政策（屏蔽名人、反政治生成）与招聘审美。

**⑤ Society over Business（社会优先于商业）**
> "I prioritize societal concerns over commercial ones." — Forbes, 2022/9/16

> "I am the founder and CEO, though I prefer to be referred to simply as the founder. The title of CEO feels overly corporate, and we are not a conventional business; we function as an applied research lab creating products." — Forbes, 2022/9/16

Holz 本人排斥 "CEO" 头衔，更倾向 "founder"——这不只是 PR，而是组织架构设计的起点。

**⑥ Imagining Together > Imagining Alone（共同想象 > 独自想象）**
> "We found that people really like imagining together... It's kind of like a hive mind of people, super-powered with technology." — The Verge, 2022/8/2

这是 Midjourney 选择 Discord 而非独立 iOS app、把所有图像 default-public 的根本原因。

---

#### 2.3 补充组织证据：使命、founder taste 与 self-funded governance

这些补充证据加厚上面的组织哲学层：David Holz 为什么把公司定义为 home、为什么把产品称为 imagination vehicle，以及为什么不把融资和规模化管理当作默认路径。

### A01 — Midjourney 的起点不是公司最大化，而是一个长期工作的 home

David Holz 对 Midjourney 的第一层定义很反商业化。他没有把公司说成图片生成 SaaS、设计师生产力工具或企业创意平台，而是把它说成未来十年可以和一群人一起做重要项目的地方。这个起点解释了 Midjourney 后来一系列不标准动作：不急着融资、不先做 enterprise、不先开放 API、不把产品压成 Photoshop 插件，也不把所有路线交给短期增长指标。

Midjourney 的 founder 命题是 reflection、imagination、coordination。图像生成只是 diffusion 先突破出来的切口，背后更像一套让人构造新东西的基础设施野心。

“我其实从来不太想要一家公司，我更想要一个家；Midjourney 对我来说像是未来十年可以待着的地方，和很酷的人一起做我在乎、也希望对别人有益的项目。如果只用三个词概括主题，就是反思、想象和协调；文明要继续繁荣，就必须创造很多新东西，而创造新东西需要这三种能力，也需要围绕它们的新基础设施。” —— David Holz, What Future, 2022-11-10


### A02 — Diffusion 的机会是 taste-driven back-and-forth，不是“机器会画画”

Midjourney 切进图像生成，不是因为 David 想追“AI art”热词，而是因为 diffusion model 让人与模型之间第一次出现了足够快、足够强的审美来回互动。这里的关键不是模型能不能画 dog，而是用户在看见四张候选图以后，如何意识到自己更想要哪一种 dog，如何继续变体，如何在社区里被别人刺激出 space dog、Aztec space dog。

所以 Midjourney 的产品表面是 prompt box，真实操作面是 taste formation。模型质量只是入口，用户如何判断、如何迭代、如何形成审美偏好，才是产品真正的壁垒。

“大概一年半前，旧金山的 AI 人都在同一些圣诞派对上，大家都在说 diffusion model 好像不一样。我当时想，这里会有一个人类侧的问题，它不只是做图片，而是某种来回互动；里面有很多东西很难通过优化一个程序里的单一数字解决，甚至可能牵涉 taste，而没人真正知道 taste 是什么。我觉得自己在这件事上可能有东西可以贡献。” —— David Holz, What Future, 2022-11-10


### A03 — “Imagination vehicle” 限定了 Midjourney 不该变成自动艺术家机器

David 有意避开 art 这个词，因为 art 会把讨论带进行业替代、版权防御和“机器是不是艺术家”的老问题。他更愿意把 Midjourney 看成想象力交通工具。汽车比人跑得快，但人不会砍掉腿；生成模型也一样，它扩展人类 agency，不替代人类 agency。

这个隐喻直接影响产品和组织：Midjourney 要优化的是人和模型的共同探索，而不是把人的判断全部外包给模型。它解释了公司为什么早期不追 deepfake 和仿真照片，也解释了为什么 weird、chaos、style reference、personalization 这些“不完全听话”的功能在 Midjourney 里如此重要。

“我尽量不用 art 这个词，因为它真正关乎的不是艺术，而是想象力；有时人会把想象力用于艺术，但通常不只如此。我更像是在创造一种机器增强的想象能力，有点像 vehicle：汽车比我们快，但我们没有砍掉自己的腿，真要去远处时我们坐车。所以这更像想象力的船、车和飞机，帮助人探索审美可能性的海。” —— David Holz, What Future, 2022-11-10


### A04 — Midjourney 的产品价值观来自 David 对默认值的敏感

David 把产品默认值看成价值观传播机制。MySpace 默认给你一个朋友 Tom，Facebook 则从“没有朋友”开始，这种细节会塑造社交系统的气质。Midjourney 的 front page、公开生成、禁词、默认模型审美、photo-realism 边界、首页多样性，本质上都不是中性设计，而是在传播创造者的价值观。

这意味着 Midjourney 很难完全用传统 PM 指标管理。它需要有人判断什么反馈回路应该被鼓励，什么默认审美会污染社区，什么功能虽然有需求但会把系统带向不想去的地方。

“我的哲学是，创造者会把自己的价值观注入他们创造的东西，不管他们知不知道，而且这些东西会在创造者不在场时继续传播那些价值。MySpace 一开始就告诉你有一个朋友，那个人是 Tom，是做 MySpace 的人，这会让你觉得这里可以交朋友、Tom 在乎你；但你进入 Facebook 时没有朋友，Mark 也当然不是你的朋友，这些很深的细节都是带着真实价值观的人做出来的。” —— David Holz, What Future, 2022-11-10


### A05 — Leap Motion 前史让 David 更在意交互层，而不是单点技术指标

2015 年 SVVR 演讲里，David 已经在用很接近 Midjourney 的方式思考界面。他说 Leap Motion 虽然做硬件，但本质上主要是 software company，硬件只是让“手进入计算”发生的载体。他展示 block demo 时强调，真实交互不能只靠 physics engine，也不能只靠 game engine，而要构建介于两者之间的 interaction engine。

这个前史很重要。Midjourney 也在做类似的中间层：不是简单把文字丢给模型，而是在 prompt、四张图、variation、upscale、ranking、style reference、community learning 之间搭出一个让人觉得自己在直接操作想象力的界面。

“在我伸手去抓这个 block 之前，我想说，因为这里并没有真实 block，如果我只用 physics engine，我的手会直接穿过物体；一旦穿过去，physics engine 尽力模拟时，它很可能会从我手里滑走。所以为了让这件事 work，我们必须构建一个完全不同的 engine，不是 physics engine，也不是 game engine，而是介于两者之间的东西，我们叫它 interaction engine。现在你可以看到手指其实有一点在 block 里面，但没关系，我仍然可以驱动这样的 physical interaction。” —— David Holz, SVVR, 2026-04-22


### A06 — “技术变成非技术”是 Midjourney 的深层组织假设

David 在 2015 年就说，随着 digital medium 和现实世界融合，technical 会变成 non-technical，原来只有抽象思考者、程序员和工程师能处理的问题，会被有身体直觉、社交直觉、情绪直觉和审美直觉的人处理。Midjourney 正是这个假设在图像创作上的商业化。

它让很多不会 Photoshop、不会摄影、不会 3D、不会写代码的人进入视觉生产。组织上，它也天然偏向 consumer-first 和 community-first，因为真正的新行为常常先出现在非专业人群里，而不是预算周期很长的企业流程里。

“现在很多 technological problem solving 是由 abstract thinkers 完成的；我们处理 nanometer scale 的东西，但作为人类，我们并不和 nanometer scale 的东西互动。可是现在我们正在把 abstract 变成 concrete，所以 physical、intuitive、social、emotional intelligence 也能解决 abstract problems。像 Jane Goodall 这样能探索森林的人，突然也可以探索 brain；以前这种事会被限制给那些能用非常 technical、programmatic 方式操作 computer 的人。于是 technical 变成 non-technical，之后还会出现某种 new technical，而我甚至不知道那是什么。” —— David Holz, SVVR, 2026-04-22


### B06 — 不融资不是姿态，而是组织治理选择

David 对投资人的拒绝，不只是“创始人个性”。它让 Midjourney 在早期不必把路线改写成 VC 容易理解的 enterprise SaaS、平台 API 或广告增长故事。公司可以把商业闭环维持在一个很朴素的结构里：云端生成要花钱，用户订阅付费，公司拿一点 margin，再把现金流换成 GPU、服务器和模型迭代。

这会直接影响组织形态。没有外部融资压力，Midjourney 可以暂时不搭销售组织、不把 professional workflow 作为唯一主线、不为了 board narrative 提前平台化。它的治理核心仍然是 founder taste、订阅现金流和用户留存，而不是融资节奏。

“我想做一个很诚实的生意：这个东西不能跑在你的电脑上，要跑在云端，算力要花钱，我们从中拿一点 margin，这就是业务。很多投资人来找我们，愿意给很多钱，但我会问我拿来花在哪；他们说有钱总是好的，或者说重点不是钱而是建议。到现在为止，我还没有听到一个足够有说服力的理由。” —— David Holz, What Future, 2022-11-10


---

## 三、组织结构图（Org Structure Diagram）

#### 3.1 宏观结构（2026 年 Q1 估计版）

Midjourney **未公开任何 org chart**，Stanford CRFM FMTI 2025 在 "Organization Chart" 一项给其 **0/1** 分。以下是根据 LinkedIn、RocketReach、Contrary Research、媒体报道重建的结构：

```
                        ┌──────────────────────────────┐
                        │  David Holz — Founder (CEO)  │
                        │  (偏好 "founder" 头衔)         │
                        └──────────────┬───────────────┘
                                       │
                    ┌──────────────────┴──────────────────┐
                    │                                     │
         ┌──────────▼──────────┐              ┌──────────▼──────────┐
         │  Caleb Kruse        │              │    Advisor Circle    │
         │  Chief of Staff     │              │  Philip Rosedale     │
         │  (ex-Leap Motion)   │              │  (Second Life)       │
         └──────────┬──────────┘              │  Nat Friedman (informal) │
                    │                         │  Daniel Gross (SSI)  │
                    │                         │  Shengjia Zhao (OpenAI) │
                    │                         └──────────────────────┘
   ┌────────────────┼─────────────────┬────────────────┬───────────────┐
   │                │                 │                │               │
┌──▼──────┐  ┌─────▼────────┐  ┌─────▼───────┐  ┌─────▼───────┐  ┌───▼─────────────┐
│ Research│  │ Hardware     │  │ Legal       │  │ Finance     │  │ Community / Ops │
│ & Eng.  │  │ Ahmad Abbas  │  │ Max Sills   │  │ Amy Kux CFO │  │ (Head 空缺，     │
│ (~60–70 │  │ Head of HW   │  │ Gen. Counsel│  │ Bhavin Patel│  │  2025/5 Erik    │
│ 无公开 VP)│  │ (ex-Apple    │  │ (ex-Google) │  │ Head of Fin.│  │  Martin 离职)    │
│         │  │ Vision Pro)  │  │             │  │             │  │                 │
│ ~40人   │  │ SF in-person │  │             │  │             │  │ Thomas Calloway │
│ 模型/产品 │  │ 子团队       │  │             │  │             │  │ VP, Special     │
│ 工程师    │  │ (ME/EE/FW)   │  │             │  │             │  │ Projects        │
└─────────┘  └──────────────┘  └─────────────┘  └─────────────┘  └─────────────────┘
                                                                          │
                                                          ┌───────────────┴──────────┐
                                                          │  Discord Community       │
                                                          │  三层模型:                 │
                                                          │  • Dedicated Support     │
                                                          │    Team (FTE, paid)      │
                                                          │  • Moderators            │
                                                          │    (转为 FTE，$80–100K)  │
                                                          │  • Guides (volunteers)   │
                                                          └──────────────────────────┘

                                 外部战略合作
                                       │
                                       ▼
                              ┌────────────────┐
                              │  Spellbrush     │
                              │  (YC W18, ~30人) │
                              │  Niji・journey   │
                              │  联合开发 anime   │
                              │  模型 (V7, 2026) │
                              └─────────────────┘
```

#### 3.2 核心人物（Named Leadership，截至 2026 Q1）

| 姓名 | 岗位 | 加入时间 | 背景关键词 | 来源 |
|------|------|---------|-----------|------|
| **David Holz** | Founder & CEO | 2021/8 | ex-Leap Motion CTO, NASA Langley, Max Planck | TIME 100 AI 2025 |
| **Ahmad Abbas** | Head of Hardware | 2023/12 | ex-Apple Vision Pro (5yr), Neuralink, Leap Motion | LinkedIn |
| **Amy Kux** | CFO | 2025/4 | 接替 Nadia Ali | LinkedIn post |
| **Caleb Kruse** | Chief of Staff | 2023/5 | ex-Leap Motion CoS, Stanford, Nat Geo Explorer | LinkedIn |
| **Max Sills** | General Counsel | 2023/2 | ex-Google open source legal | LinkedIn |
| **Bhavin Patel** | Head of Finance | 2023/5 | ex-MoonPay VP FP&A, Wharton | LinkedIn |
| **Thomas Calloway** | VP, Special Projects | 2024/8 | SF-based | LinkedIn |
| **Nadia Ali** | 前 CFO → Advisor | 2022/1 – 2025/5 CFO | ex-Leap Motion；现 Emergence AI CFO | LinkedIn |
| **Erik Martin** | 前 Head of Community | 2023/12 – 2025/5 | ex-Reddit, Nike, Depop | LinkedIn |
| **Philip Rosedale** | Advisor | 2022/3 | Second Life / Linden Lab 创始人 | The Org |

**Leap Motion 人脉圈：** Holz、Abbas、Kruse、Ali 四位核心人物均来自 Leap Motion。这是一个典型的 trusted-network hiring 模型——不靠 open recruiting，靠"可信邻居的可信邻居"。

#### 3.3 职能分布（基于 LeadIQ/ElectroIQ 2024 数据，131 人基数）

| 职能 | 占比 | 估计人数 |
|------|-----|---------|
| Engineering / Research | ~45–53% | ~60–70 |
| Product | ~15–19% | ~20–25 |
| Design | ~11–15% | ~15–20 |
| Marketing & Community | ~8–11% | ~10–15 |
| Hardware | 新增且独立 | 2024/8 公开，SF 在岗，约 10 余人起步 |
| Finance / Legal / Ops | 余下份额 | ~10 |

来源：ElectroIQ、Contrary Research。

---

#### 3.4 补充组织证据：小团队、算力优先与运营瓶颈

组织结构图能看到 Midjourney 的外部形状；逐源笔记补上的，是这个小组织为什么能承载模型、社区、网页、moderation 和算力调度，以及它正在补哪些中间层。

### B01 — 10 人团队同时背模型、社区、网页和 moderation，说明 Midjourney 的早期组织没有职能缓冲层

2022 年 office hours 里，Midjourney 最真实的状态是一支约 10 人团队同时处理当前模型、下一代模型、web 功能、组织流程、网页创作流程、Discord 社区和内容安全。这种组织不是清晰职能分工后的产品机器，而是 founder 直接把技术路线、用户反馈、社区治理和商业约束揉在一起取舍。

这解释了 Midjourney 为什么能快，也解释了为什么时间表经常不确定。小团队的效率来自判断链短，但代价是所有关键主题都挤在少数人身上。

“我们现在大概只有 10 个人，所以有时候真的很挣扎；一边要把当前系统调好，一边要准备下一代系统，还要分心做网页功能、组织流程、网页创作流程和一些还不能讲的新功能。问题不是我们不知道方向，而是内部同时有很多东西都看起来又热、又好、又重要，我们很难把自己砍到更少的事项上。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07


### B05 — David 的小组织理论很硬：知识劳动不随人数线性扩张

David 对组织规模的判断很极端：知识劳动组织的有效性大致按人数的对数增长。这个判断不一定适用于所有公司，但很适合 Midjourney 的业务结构。Midjourney 可以大规模扩张 GPU 成本，因为订阅收入能覆盖；不必同步扩张 headcount，因为模型、社区、Discord / web 界面和自动化基础设施承担了很多杠杆。

如果把收入增长理解成“人效高”，会错过机制。Midjourney 是把成本放进 GPU，把学习放进社区，把审美判断放进 founder 和用户反馈，把一部分 support 放进社区互助。

“David 非常专注于保持组织小。他说，对 intellectual labor 来讲，一个组织的有效性大致按人数的对数增长；这意味着 1000 人可能只比 100 人有效两倍，而一个 10000 人公司可能比 100 个 100 人公司低效 25 倍。所以保持组织小非常关键，但这不意味着成本结构不能扩张，他们显然花了很多钱在 GPU 上，只是 subscription 会为这些 GPU 付费。” —— John Coogan, Power Law, 2023-06-20


### B07 — 新高管、工程招聘和 project management 招聘说明 Midjourney 正在补运营瓶颈

到了 V8 / video / web workspace / community project / hardware project 这些方向同时出现时，纯 founder-led 小团队会遇到新的协调成本。Midjourney Korea 对 office hours 的二次转述提到新 executive team、工程师招聘和 project management staff，这条不能当作 founder 原声逐字稿，但作为组织信号很重要：Midjourney 可能正在从“少数人判断 + 社区反馈”转向更复杂的产品组合管理。

这里的关键不是公司终于要变“大公司”，而是它必须补一个过去故意压低的层：运营效率、项目节奏、跨功能协调和未公开项目管理。也就是说，Midjourney 下一阶段的组织问题不是招多少销售，而是如何在保持小团队判断密度的同时，让多个高复杂度项目不互相拖慢。

“关于公司增长和领导层，一个新的 executive team 已经加入，用来提高 operational efficiency 并解决 bottlenecks；他们计划继续招聘工程师和 project management staff，所以有了新的负责人以后，会招聘相关人员。创始人 David 目前正在准备官方 announcement video，并管理新项目，未披露项目包括功能项目、社区项目和硬件相关项目，也在等待内部批准和媒体准备。” —— Nam-kyoung Cho / Midjourney Korea, 2026-04-21


---

## 四、Hiring Practices（招聘实践）

#### 4.1 招聘哲学

Holz 的原则很简单："hire top talent and trust them to get on with it"（Over the Anthill, 2024）。配合极度扁平结构，本质上是一种 **low-management-overhead** 的运作方式。

四点可验证的招聘特征：

1. **Founder-led 早期招聘**：2021 年最初的 10 位 engineer 由 Holz 亲自招募（Nathan Ma 访谈, 2025/6）。
2. **信任圈再激活**：多位高管来自 Leap Motion。
3. **Email 渠道**：2024 年 Hardware 团队通过 `hardware@midjourney.com` 这种极简方式招人（Ars Technica）。
4. **LinkedIn 直发**：绝大多数 open role 在 LinkedIn 而非猎头渠道发布。

#### 4.2 2025 Q4 – 2026 Q1 Open Roles（样本）

以下所有 hardware 岗位均为 SF Bay Area 现场办公：

- Mechanical Engineer, Consumer Hardware
- Firmware Engineer, Consumer Hardware
- Electrical Engineer, Consumer Hardware
- Mechanical Engineering Technician

其他职能：Treasury Manager、Senior Tax Accountant、Accounts Payable Specialist、Billing Infrastructure Engineer、Data Engineer、Community Moderator（fully remote, $80K–$100K）。

来源：LinkedIn /company/midjourney、Weekday.works。

#### 4.3 薪酬（Levels.fyi, 2025/11 数据）

| Level | Median Total Comp |
|-------|-------------------|
| L3 (SWE II) | $194K |
| L4 (SWE III) | $283K |
| L5 (Senior SWE) | $401K |

人均年收入（revenue per employee）约 **$4.6M**（107 人 / $500M ARR），属于全球 software 行业顶级效率水平（CompaniesHistory.com）。

---

#### 4.4 补充组织证据：招聘纪律、社区支持与内部验证层

招聘实践不只体现在 LinkedIn open roles，也体现在 Midjourney 如何把早期信任圈、Guides、Moderators 和社区支持纳入产品迭代。

### B04 — 小团队纪律来自一次昂贵的 Leap Motion 组织教训

Leap Motion 到后期约 100 人，融资、硬件合作、开发者生态和平台叙事都做过，但原始愿景没有进入大众日常。Midjourney 几乎把这条路反过来：先不造硬件，不先做 App Store，不先开 API，不先给企业采购周期做定制，而是把核心体验放到 Discord 里，让用户立刻使用、学习和付费。

这不是创始人迷信小团队，而是经历过过早平台化、过早组织膨胀和外部生态不成熟之后，对公司边界的重新选择。

“到后来，Leap Motion 已经大约 100 人，是一个不小的组织，David 也几乎跑了十年，但它还是没有真正工作起来；没有清晰路径能让 Leap Motion 设备进入数百万美国人或电脑用户手里，原始愿景没有合在一起。2019 年他们把公司卖给 UltraHaptics，价格大约 3000 万美元，这对员工、投资人和创始人都不是一个很好的结果。” —— John Coogan, Power Law, 2023-06-20


### D09 — Guides 和 Moderators group 变成中间版本的内部验证层

V7.1 被放在 Guides 和 Moderators group 里测试，是一个很小但很有组织含义的信号。Midjourney 不一定把每个小版本都推给全体用户，而是先让 veteran users 和治理/教学层参与验证。这样可以减少普通用户学习成本，也能在 release 前发现 prompt interpretation、审美变化和社区反应。

这说明 Midjourney 的社区不是一个平面人群，而是有分层的：普通用户、新手频道、power users、guides、moderators、office hours 和官方教学共同组成产品验证网络。

“内部在 Guides 和 Moderators group 做 V7.1 测试，这意味着 V7.1 已经出来了；他们确认 prompt interpretation accuracy 有改善，但也说重大改进很少，而重大改进必须在视觉上明显。Midjourney 内部说 7.1 充当 V8 系统的 verification layer，与其把重点放在 7.1 自身性能提升，不如用它测试 V8 features。” —— Nam-kyoung Cho / Midjourney Korea, 2026-04-21


### C10 — 社区支持已经变成产品功能，而不是售后附属品

V8 quick start 结尾提醒会员可以获得 24/7 prompting community support、FAQ/tutorial site、events calendar 和 prompt battles。这说明 Midjourney 的组织杠杆不止来自模型，也来自一套持续训练用户的社区教育系统。模型越强、参数越多、V8 / V8.1 的学习曲线越陡，用户越依赖 prompt craft voice channel、教程、社区 FAQ 和活动。

这里的组织含义是，Midjourney 把一部分 support、training 和 customer success 外部化到社区里，但又通过官方 Discord、课程和活动保持方向感。它不是没有支持组织，而是支持组织长得不像传统 SaaS 的客服团队。

“我想提醒你们，会员可以得到 24/7 的 prompting community support；如果你需要帮助，可以随时来到这些频道，通常会有人出现帮你，所以不要一个人飞。我们也有一个网站，正在慢慢汇总所有 community FAQs 和 tutorials，今天我分享的大部分内容都在上面，还有很多活动日历和 prompt battles。” —— Clarinet, Midjourney Quick Start, 2026-04-21


---

## 五、Remote Work Policy（远程工作政策）

Midjourney **没有发布过正式 remote policy**，但从岗位设置可反推：

| 职能 | 办公形态 |
|------|---------|
| Hardware Engineering | **SF 在岗** — 硬生硬性强制 |
| Finance / Legal / Ops | US remote 可 |
| Community Moderator | fully remote |
| Research / Product Engineering | 混合；北美为主，有海外远程 |

地理分布（2024/9，131 人时样本）：

| 地区 | 占比 |
|------|-----|
| North America | 46% |
| Asia | 28% |
| Europe | 19% |
| South America / Africa / Oceania | 合计约 7% |

来源：LeadIQ via ElectroIQ。

HQ 地址：San Francisco（156 2nd St）与 South San Francisco（611 Gateway Blvd）两处登记，后者见于 H-1B 申请文件（ZoomInfo）。

---

## 六、AI Integration in Operations（AI 在内部运营中的应用）

这是 Midjourney 最独特的组织能力——**用 AI 替代传统公司的多个职能层**。

#### 6.1 Community-as-Training-Data

Holz 最早、也最有洞见的一段话：

> "If you look at the v3 stuff, there's this huge improvement. It's mind-bogglingly better and we didn't actually put any more art into it. We just took the data about what images the users liked, and how they were using it. And that actually made it better." — The Register, 2022/8/1

在传统公司里，这一层需要 data labeling ops、专业 RLHF 团队、PM 与 research 对接机制——Midjourney 把它全部外包给了 **Discord 社区的 likes / upscales / re-rolls**。用户的"点赞"信号就是训练信号。

#### 6.2 Discord Office Hours = No PR Layer

Holz 每周（通常周三）在 Discord 语音房间里一次 **主持 4 小时、最多 1,000+ 用户同时在场** 的 office hours，直接宣布政策、讨论 roadmap、回答投诉。

> "We also do these office hours where I'll sit on voice for four hours with like 1,000 people and just answer questions." — The Verge, 2022/8/2

经典实例：2023/3 宣布停掉 free trial（"Due to a combination of extraordinary demand and trial abuse..."）；2023/4 著名的 "We're going to try just banning negativity."（The Verge Command Line）；2024/3 自愿在大选前屏蔽 Trump/Biden 图像（PCMag）。

这相当于把 PR、Community Management、Product Marketing 三个部门折叠成"CEO 自己 + Discord"。

#### 6.3 GPU-First Resource Allocation

Contrary Research 的分析指出，Midjourney 把大部分收入反向投入到 GPU capacity，而非 GTM 或 Sales 团队。它没有 Sales 团队、没有 API、没有 Partnership 团队——连 B2B 都用 consumer subscription 形式售卖。Holz 曾在内部暗示："we got too profitable, so I increased server costs"（意思是主动做亏损以优先改善用户体验）。

#### 6.4 Founder Coding in 2026

2026/1/4 Holz 在 X 上发帖：

> "ive done more personal coding projects over christmas break than i have in the last 10 years. its crazy. i can sense the limitations, but i *know* nothing is going to be the same anymore." — @DavidSHolz

Elon Musk 回复："We have entered the Singularity." 这条发帖不是段子，而是 Holz 对 AI-augmented workflow 的个人认可——也是 Midjourney 未来继续保持 **小团队 × 高产出** 的哲学基础。

---

#### 6.5 补充组织证据：AI 运营、社区反馈与 creative workspace 迁移

AI Integration 不是内部用几个工具提效，而是把社区行为、ranking、front page、release 节奏、support、moderation 和未来 web workspace 接成同一个反馈系统。

### B02 — 年度订阅现金先换 GPU 供给，Midjourney 的财务纪律直接服务产品体验

Midjourney 的 bootstrapped 不是“没拿钱”的故事，而是一种资源排序。2023 年 office hours 里，David 开场讲的不是新功能，而是把年度订阅带来的现金提前锁定为未来一年 GPU 供给。独立 web、mobile、compute、成本优化、未来 video 和 3D，都要建在这个基础设施优先级上。

这和典型 AI 应用公司不同。很多公司先融资买算力，再找 PMF；Midjourney 先用用户付费证明 PMF，再把现金流转成推理体验和未来模型路线的确定性。

“我们现在的主要优先级还是建设自己的平台：独立的 Midjourney web、独立的 mobile，并且投资更多服务器。我们觉得接下来一年会有很多 GPU 短缺，所以基本上是在拿年度订阅的钱问：用这笔已经确定的钱，能不能为下一年买下足够好的供给，让我们有快速而充足的 compute。长期看，我们想有自己的界面、可靠的算力，并且把基础设施优化到以后做 video 和 3D 时不用靠涨价来支撑。” —— David Holz, Midjourney Office Hours, 2023-07-26


### B03 — Midjourney 的稀缺资源不是钱，而是 GPU allocation 和全球 inference 调度

Power Law 2023 把 Midjourney 说成第一个真正有大规模 PMF 的 AI model，重点在 inference。很多 AI 公司训练贵但真实使用不够大，Midjourney 则要用大量 GPU 为真实用户生成图像。David 没有用融资换增长，而是和云厂商谈 GPU 供应，并用全球调度把空闲算力用于生成任务。

这条机制让 Midjourney 的“规模”主要体现在计算资源和任务调度，而不是组织人数。用户看到的是 Discord 或 web 上的一次生成，背后是一个以订阅收入支付推理成本、以全球 GPU 排班维持体验的基础设施系统。

“Midjourney 花大量钱在 GPU 和数据中心上生成图像，而且很多成本不是训练，而是真正 inference。David 本可以出去融资，但他做的是打电话给 AWS、Google 和其他有云端 GPU 的大供应商，谈下大额 GPU 供应来扩张；团队还建了全球调度基础设施，比如美国用户的图片可以在日本或韩国夜间的 GPU 上渲染，再传回美国，因为生成本来就要 60 秒，跨国传输那点延迟不重要。” —— John Coogan, Power Law, 2023-06-20


### C04 — 社区不是消费者，而是审美模型的训练者

Midjourney 的数据闭环不是简单吞自己的生成图。David 把分工讲得很清楚：互联网教模型概念，用户教模型 beauty、expression 和 what people actually want。用户生成、选择、喜欢、ranking、变体和放弃，都是审美反馈。

这让 Midjourney 的社区像 AppLovin 的广告数据闭环，但优化目标完全不同。AppLovin 优化 ROAS，Midjourney 优化“什么值得看、值得继续变体、值得被更多人学习”。

“图片本身来自互联网；用户生成的图主要不是用来教它猫是什么。如果系统已经能画猫，它不需要再看自己生成的猫来学习猫；但如果有某张猫的图片大家都特别喜欢，那就教会它一些东西。所以互联网教它概念，用户更多是在教它 beauty、expression，以及人们真正想要什么。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07


### C05 — Ranking system 是把社区行为转成模型改进的中间层

2023 年 office hours 里，David 提到团队正在改 rank images，希望从用户排序中拿到更多数据，让算法和 ranking 本身变好。这说明 Midjourney 的产品、社区和模型研发不能被拆成孤立部门。前端上的一次排序，可能同时影响用户体验、社区分发和模型训练。

这也是为什么 Midjourney 的组织不是普通“research + product + community”三段式。社区行为本身就是研发输入。

“我们试着改了一些 ranked images 的工作方式，因为有机会从里面拿到更多数据；现在还不知道能不能成功，所以如果大家看到 rank image 有什么问题，请告诉我们。这个 ranking system 很实验性，但如果它跑得好，可能会同时改善算法表现，也让 ranking 本身变得更好。” —— David Holz, Midjourney Office Hours, 2023-07-26


### C07 — Front page 规则决定社区看到什么，也决定模型学到什么

Midjourney 首页不是简单 gallery。David 2023 年提到调整 front page 规则，让同一个人的图片不能连续占据太多位置，避免首页被少数用户接管。这个细节很小，但组织含义很大：分发规则会塑造用户学习路径、审美趋同程度和模型反馈宽度。

如果首页只奖励少数重度用户，社区会变窄；如果分发更丰富，用户看到的可能性、prompt 学习和审美反馈都会变宽。

“我们稍微收紧了 front page 的规则，让你不会在首页看到同一个人的两张以上图片。之前首页有时会被少数人接管，现在结构上已经不可能了，我觉得这让 front page 更丰富。我们还在为未来版本做更复杂的首页算法，希望它能好很多；我们正在投入很多精力思考，怎样让人更容易探索其他人在 Midjourney 上做出的图片。” —— David Holz, Midjourney Office Hours, 2023-07-26


### C11 — Style Finder 和 user profile 把社区从 Discord 房间推进到创作者发现层

如果 Style Finder、PCode、user profile、follow、like 和 SREF seed 分享真的连成一条产品线，Midjourney 的社区会从“大家在一个 Discord 里互相看图”升级为“风格、创作者和偏好可以被发现、关注和复用”。这会让社区变成审美分发网络，而不仅是 prompt 支持网络。

这对组织很关键：Midjourney 将不再只是运营 Discord，而是在搭建自己的 creative social graph。用户分享风格，其他人复用，平台收集偏好和 ranking 数据，再反哺 personalization 和模型审美。

“Style Finder 和 Style Creator 都被说成和 personalization 以及 user profile system 紧密连接；personalization 指的是 Pcode，通过个人偏好风格的 ranking 创造某种东西，而 user profile system 可以理解成 Midjourney 版 Instagram。你在 Style Finder 里找到的 style 会分享到你的 user profile，最终就像分享 Instagram 图片一样分享风格，还会提供跟随的 SREF seed 信息，其他用户看到以后可能 follow 你或 like。” —— Nam-kyoung Cho / Midjourney Korea, 2026-04-21


### D03 — Drip release 把社区变成外部 QA 和传播网络

V7 后的 release cadence 说明，Midjourney 社区不是被动接收产品公告，而是每次新参数、新编辑能力、新模型 patch 都会立刻测试、发图、写教程、争论。Secret Playground 这期把 drip release 的价值讲得很清楚：持续掉落 weird、editor 等小功能，比继续等待巨型版本更能维持社区能量。

对小团队来说，这种 release cadence 是组织杠杆。社区同时承担 QA、教育、传播和产品反馈。

“现在这种 dripping system 比继续等 V7 好太多了，我宁愿他们就这样放出来，让我们玩，然后继续下一个东西；它能把 hype cycle 保持住。五六周前，Twitter 上 Midjourney 的东西好像有点安静，现在因为不断有新功能，所有人又回来了，大家都在测试、玩、发结果。它不是一个巨大的 release 把所有东西都淹没，而是每次都有新的东西让人重新进来。” —— Drew / Rory, Midjourney Fast Hours, 2025-04-22


### D04 — 每次大版本都会重置社区知识，用户教育已经是产品能力

V7 材料里，重度用户回到旧 prompt、旧参数、旧内容资产里重新测试 stylize、personalization、remix、draft mode、explore page 和质量边界。Midjourney 的产品速度不只是模型发布速度，还包括社区能否快速重建隐性操作知识。

这件事过去是优势，因为 power users 愿意学习、分享、教学；但模型越复杂，功能越多，官方教育越不能缺席。

“新模型出来时，我喜欢回去翻旧 prompt，看看它们现在还能不能工作；我会看以前那些没分享过的东西，想起当时为了某个画面做过什么，然后也会意识到，过去觉得革命性的图现在看起来已经像旧资产了。真正有用的是重新测试参数和 feature，因为 Midjourney 里很多 incremental changes 不会明说，你只有回到 drawing board 重新实验，才会发现这些大版本和模型变化到底改了什么。” —— Drew / Rory, Midjourney Fast Hours, 2025-04-13


### D08 — V8 不是普通版本迭代，而是会吸走组织注意力的主线工程

V8 相关材料最值得看的是组织节奏，而不是单张图质量。Midjourney Korea 的 office hours 二次转述提到，团队重点转向基于稳定 V7 代码库构建 V8，数据验证和核心系统验证完成后进入大规模训练。这说明 V8 会牵动研发、数据、基础设施、产品教育和社区预期管理。

这也解释了为什么一些旁支功能会显得慢。对小团队来说，下一代模型不是 research team 的孤立项目，而是全公司主线工程：短期 feature release、V7.1、draft mode、personalization、教程和社区节奏都要服从它。

“第一条更新是 V8 开发状态，团队现在的重点是基于稳定 V7 代码库构建的 V8，他们说核心系统已经被验证，这比预期快很多；按照九月的计划，本来十月做数据验证，十一月和十二月再搭系统，但现在十月中旬，数据验证上周已经完成，核心系统也验证过了，现在正在扩大系统规模，并用大数据集在大规模系统上训练。” —— Nam-kyoung Cho / Midjourney Korea, 2026-04-21


### C01 — Discord 让用户生成意图，而不是只承接已有需求

Midjourney 用 Discord 做前端，经常被理解成临时低成本方案。但 David 的核心判断更深：大多数人单独面对“你可以想象任何东西”时不知道自己要什么；群体会让想象力在彼此想法上继续搭建。一个人的 dog 会变成 space dog，再变成 Aztec space dog。

这就是 Midjourney 社区的第一性价值。它不是把用户带到模型面前，而是让用户先在群体里发现自己可以要求什么。

“David 在 The Verge 采访里的说法是：我们去年 9 月开始测试 raw technology，很快发现大多数人并不知道自己想要什么。你说，这里有一台机器，你可以用它想象任何东西，你想要什么？他们说 dog；你说真的吗？他们说 pink dog。于是你给他们一张狗的图片，他们说 okay，然后就去做别的事了。但如果你把他们放进一个 group，比如 Discord server，他们会说 dog，别人会说 space dog，再有人会说 Aztec space dog；在 community setting 里，人们会在彼此的想法上继续搭建。” —— No Text To Speech / David Holz via The Verge, YouTube, 2026-04-21


### C02 — Discord 同时解决移动端、图像展示、slash command 和用户互学

Power Law 2023 拆得很具体：Discord 给 Midjourney 提供了移动端、桌面端、图片展示、结果按钮、slash command、bot 和可扩展基础设施。更关键的是，它是协作环境。用户不只看到自己的生成结果，还能看到别人怎么写 prompt，怎么把普通 dog 改成更复杂的想象。

这正好解决了 Alan Kay 当年给 David 的问题：不要只想 feature，要想用户怎样学习。

“Discord 对这门生意有几个很强的地方：首先它是预制、可扩展的前端，移动 app 开箱即用，很多人低估了在 iOS 和各种设备上做一个好键盘有多难；Discord 支持图片、结果下面的按钮、slash commands、bots，桌面和移动都能用。更重要的是，它是协作环境，用户进聊天室看到别人做东西，立刻能复制 prompt，再做自己的版本。” —— John Coogan, Power Law, 2023-06-20


### C03 — 超大 Discord 的 onboarding 是组织设计，不是一个自然增长结果

Midjourney server 的规模不能按普通 Discord server 理解。新用户会被分到不同 group，只看到有限 newcomer rooms。这样做不是为了藏复杂度，而是为了让大量不熟 Discord 的普通用户也能进入。这个结构说明 Midjourney 的社区运营已经是产品 onboarding 的一部分。

加入门槛也被刻意压低。Midjourney 没有简单套传统 captcha / verification，因为任何摩擦都会挡住普通用户；但它又必须处理 bot 和免费滥用，因为每次滥用都在消耗服务器成本。

“Midjourney server 非常独特，因为你加入服务器时会被分到不同 group；比如我看这个用户，他在 group four，这意味着他只能看到非常有限的一部分 newcomer rooms。我认为服务器里大概有 200 个 newcomer rooms，但因为这个产品被很多媒体宣传过，从 Daily Dose of Internet 到 John Oliver，很多不熟 Discord 的人都会进来，所以这个 Discord server 必须对新用户相对友好，这也是为什么他们让用户可见的频道更少。” —— No Text To Speech, YouTube, 2026-04-21


### C08 — 开放加入和反滥用之间的 tradeoff，是 Midjourney 的真实运营题

Midjourney 的 Discord 不是只要“人越多越好”。普通用户进入必须足够简单，因为这决定 consumer growth 和 prompt 学习；但 bot、免费额度滥用和假账号又会直接消耗 Midjourney 的服务器成本。No Text To Speech 对 moderator 的采访显示，Midjourney 在这个问题上不愿采用太重的传统 verification，因为 false positive 会伤害真实用户。

这是一种典型平台治理取舍：增长、可达性、算力成本、反滥用和用户信任被放在同一张表里。Midjourney 的社区运营因此不是 Discord 管理员工作，而是成本控制和产品增长的一部分。

“Volunteer moderator 说，他们不能谈具体检测方法，这也合理，因为你不会告诉别人你怎么判断 bot；但他们确实没有 Discord 上常见的那种传统 verification，而且他们真的不想要任何会让人更难加入的东西。原因也讲得通：如果你想让一个 Discord server 对所有人开放，就要尽可能简单，让奶奶也能上 Midjourney 生成漂亮的艺术图；同时 Midjourney 有自己的系统检测 bot 和 abuse，因为滥用 Midjourney 最终会让 Midjourney 花钱，别人是在免费使用并消耗服务器。” —— No Text To Speech, YouTube, 2026-04-21


### C09 — 150 万 Discord 不是用户数而已，而是产品和治理实验场

2022 年 David 已经把 Midjourney server 说成世界最大的 Discord server，并公开向用户征集如何让巨大 server 变好的建议。这不是普通 community management，它更像一个和 Discord 平台共同扩容的组织实验：Midjourney 的用户规模、频道结构、反馈收集、规则执行和基础设施 bug，都在逼 Discord 和 Midjourney 一起学习超大社区怎么运行。

这解释了为什么 Midjourney 的社区能力很难被简单复制。别人可以接 Discord bot，但很难复制一个已经把 prompt 学习、作品展示、用户支持、moderation 和模型反馈压在同一个巨大公共空间里的操作系统。

“Discord server 已经到 150 万了，我们现在是世界上最大的 Discord server，而且很快可能比后面几个最大的加起来还大。随着服务器变大，事情会变得有点奇怪，因为 Discord 也没有见过这么大的社区；如果有人知道怎样让一个巨大 server 变得更好，请把想法丢到 feedback channel，我们真的会读。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07


### C06 — Moderation 是反馈回路管理，不是道德口号

Midjourney 对 porn、gore 和 shock image 的治理逻辑非常产品化：允许什么，什么就会形成反馈回路，进而吸引对应人群、驱逐另一批用户。David 不把 moderation 讲成抽象价值观，而是讲成 social system design。

这解释了为什么 Midjourney 的安全治理从早期就和社区、模型、前台展示和默认审美缠在一起。它要做的是安全的通用艺术探索空间，而不是让最高刺激反馈占据整个系统。

“我们必须非常小心 feedback loop，因为如果有人做很血腥的内容，所有喜欢血腥的人都会来，然后大家都在做 gore；色情也是一样。很多社交网络会被它们允许的反馈回路主导，我们不想让这个系统被最糟的反馈回路主导。总有人会做 AI porn 服务，但我们更想做一个安全空间，聚焦一般性的艺术探索。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07


### D01 — 当前 Discord 体验只是未来创作工作台的 tutorial

2022 年 David 已经把 Discord 体验看成未来一两年真正体验的教程。Midjourney 想做 specialized model、web creation flow、organization flow、跳出传统 text-to-image 的功能，以及独立 web experience。Discord 解决了早期学习和分发，但不可能永久承载复杂编辑、资产管理、搜索、移动体验、support 和治理。

这条判断决定了 Midjourney 的产品迁移方向：不是抛弃 Discord，而是在保留社区学习网络的同时，把核心创作和资产控制面收回。

“我觉得现在的 Midjourney 体验在很多方面只是接下来一两年真正会发生的事情的教程，像一个很 intense、很 amazing 的视频游戏的入门体验。我们想做更多高级工具，想展示 specialized model、网页创作流程、组织流程，以及一些跳出传统 text-to-image 的东西，让大家开始感觉到这个东西到底会往哪里去。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07


### D02 — Discord 开始卡住 inpainting，平台迁移从愿景变成执行问题

2023 年 office hours 里，David 提到 inpainting 和更好的 styles 已经差不多准备好，却因为 Discord 需要新的 UI 元件、mobile 支持和 desktop-only 取舍而拖慢。这是一个非常具体的 product-control signal。早期借平台很高效，但产品越复杂，外部平台越可能卡住 release。

Midjourney 从 Discord 走向自有 web/mobile，不是渠道迁移，而是产品控制权回收。

“inpainting 和更好的 styles 已经差不多准备好了，可能会作为 5.3 发出来；但这次又被 Discord 卡住了。我们在 Discord 里做 inpainting 的方式需要一些新的 UI，它们还没有发布，Discord 也在考虑是不是要先让 mobile app 支持，或者我们干脆关掉 mobile 版本、先做 desktop-only。我完全可以接受先发 desktop，如果这样能更快上线；只是这个 release 同时牵涉 Midjourney 和 Discord，所以拖得比我们这边需要的时间久很多。” —— David Holz, Midjourney Office Hours, 2023-07-26


### D06 — V8 把 Midjourney 从 vibe exploration 推向更结构化的生产控制

官方 Quick Start 把 V8 Alpha 课程分成 exploratory prompting 和 prompt adherence，明确这堂课不是教用户随便写诗意短句发现风格，而是教用户在有明确项目目标时控制画布。这说明 V8 的产品性格在变：它更偏 prompt adherence 和 production control，8.1 才可能更适合 aesthetic exploration。

这个方向对专业工作流是必要的，但也会改变 Midjourney 的娱乐属性。过去短 prompt 和 mood board 自动爆出 banger，是 Midjourney 的魅力；现在用户要学会更明确地描述画面、镜头、光线、媒介和可见细节。

“如果你在问自己怎么 prompt，通常说明你脑子里已经有某个东西；prompting 大致有两种，一种是探索审美、写诗意短语、看看会发生什么，另一种叫 prompt adherence，也就是你有一个具体愿景，真的需要那张图，不能让 Midjourney 随机给你东西。今天我们讲的是后者，也就是控制画布。” —— Clarinet, Midjourney Quick Start, 2026-04-21


### D10 — 插件和 API 会等工作流能力成熟后再开放，Midjourney 不想为了生态叙事先平台化

2022 年 David 已经承认 Photoshop、After Effects 或其他 integration 可能有价值，但他没有把 API 当成早期必做项。原因不是没有生态想象，而是他认为 Midjourney 自己还在做更适合专业 workflow 的能力；如果太早只给一个 API，外部开发者未必能做出最好的东西。

这和 Leap Motion 的教训一致：不要先搭平台叙事，再期待生态自己长好。Midjourney 更愿意先把核心体验、工作流能力和使用范式打磨到足够清楚，再决定 integration 由谁做、怎么开放。

“某个时候我们会提供一种方式，让别人可以做 Photoshop plugin 这类 integration，而不一定要我们自己做；也可以是 After Effects 或非 Adobe 的东西。但如果我们现在只是做一个 API，我不确定大家会立刻做出最好的东西。我们正在做很多对专业 workflow 越来越有意思的新功能，然后再想象不同 integration 由谁来做、怎样让别人做。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07


### D05 — V8 Alpha 暴露了“用户愿意重新学习”这条旧 playbook 正在变弱

V8 Alpha 的负面信号不是某几张图不够好，而是重度用户没有像过去一样第一时间冲进去。过去 Midjourney 每次发布都像打开礼物，用户会花几周学习新模型；现在 Nano Banana、ChatGPT image、Reve、Runway、Flora、Weavy 等工具已经进入创作者工作流，用户没有同样的耐心把所有时间押回 Midjourney。

这不是 Midjourney 审美能力消失，而是替代路径变多后，复杂度的容忍度下降了。

“我没有像过去每次发布那样马上冲进去试；以前那感觉像打开圣诞礼物，像等了很久的包裹终于送到门口。但这一次很多人的 workflow 已经变了，其他工具已经进入我们的工作流，我们等 V8 等了太久，所以某种程度上我们已经移动了。” —— Rory Flynn / Drew Brucker, Midjourney Fast Hours, 2026-04-21


### D07 — 竞争正在从 image model 变成 workflow ownership

Midjourney 面临的竞争不只是另一个模型画得更好。Ep.64 后半段显示，同一批视觉创作者已经开始用 Claude Code、Chrome extension、Pinterest alt text、批量下载器、style forensic pipeline、Weavy 和 prompt database 自建工作流。他们把图像、风格、素材、系统提示和项目管理接成自己的创意操作系统。

如果 Midjourney 只保持“最会出漂亮图”，它可能被嵌进别人的 workflow，变成一个 aesthetic node，而不是拥有整个创作流程。

“Claude Code 是发生在我身上最好也最糟的事；最好是因为它让我把事情做完，最糟是我被‘现在能做什么’完全吞掉了。我现在可以做 Chrome extension、Pinterest alt text、批量下载 board、分析 800 张图的风格、把它变成 system prompt，再放进 Weavy 或品牌内容 workflow 里；这些以前都要花很久，现在像积木一样不断被我接起来。” —— Rory Flynn / Drew Brucker, Midjourney Fast Hours, 2026-04-21


---

## 七、Key Quotes（精选金句集）

#### 7.1 关于使命

> "We're not trying to build God, we're trying to amplify the imaginative powers of the human species." — PC Gamer, 2022/8/20

> "What does it mean when computers are better at visual imagination than 99 percent of humans? That doesn't mean we will stop imagining." — The Verge, 2022/8/2

#### 7.2 关于组织

> "It's just about having a home for the next 10 years to work on cool projects that matter — hopefully not just to me but to the world — and to have fun." — The Verge, 2022/8/2

> "We're not like a startup that raises a lot of money and then isn't sure what their business or product is and loses money for a long time. We're like a self-funded research lab... To be honest, we're already profitable, and we're fine." — The Register, 2022/8/1

> "I am the founder and CEO, though I prefer to be referred to simply as the founder. The title of CEO feels overly corporate... we function as an applied research lab creating products." — Forbes, 2022/9/16

> "Midjourney is weird cuz we have no investors. So I just like spent all my money until I had negative $1,000. And then we made money and so we're okay now. I paid myself back." — Nathan Ma 访谈, 2025/6

#### 7.3 关于 Community 与 Discord

> "If you want your own social experience, Discord is really great." — The Verge, 2022/8/2

> "It's kind of like a hive mind of people, super-powered with technology." — The Verge, 2022/8/2

> "We want one beautiful social space for people to make stuff together and not be offended, basically, and to feel safe." — The Register, 2022/8/1

#### 7.4 关于文明尺度

> "In the 1900s, it was common to dream of the 21st century. when was the last time you heard talk of a 22nd century?... dare dream of a 22nd century." — @DavidSHolz, circa 2024–2025

> "The only real question is what do we want to become?" — Nathan Ma 访谈, 2025/6

---

## 八、Evolution Over Time（组织演变时间线）

#### 2021 — Founding

- **2021/8**：Holz 离开 Leap Motion（该公司已于 2019/5 以 $30M 被 Ultraleap 收购，低于 $306M 峰值估值 10 倍，是 Holz 日后拒绝 VC 的心理基础）；以个人资金启动 Midjourney，招募 10 名 engineer。
- **2021/9**：内部 demo。

#### 2022 — 公开上线与盈利

- **2022/2**：Discord 私测开放。
- **2022/7/12**：Open beta 正式上线。
- **2022/8**：Holz 接受 The Verge、The Register、PC Gamer 等媒体集中采访，确认 "~10 people, already profitable, no investors"。
- **2022/9**：Forbes 采访，Holz 首次系统阐述 "society over business" 与 "CEO title feels too corporate"。
- **2022/11**：Stratechery（Ben Thompson）长访谈发表。
- **2022 年底**：收入估计约 $50M；团队仍约 11 人，官网 About 页面公开 founding team 全名。

#### 2023 — 社区风波、法务开战、$200M 里程碑

- **2023/1/13**：艺术家集体诉讼（Andersen v. Stability AI / Midjourney）立案。
- **2023/3**：Trump 假图、Pope puffer coat 假图病毒式传播，迫使 Midjourney 取消 free trial。
- **2023/4**：Discord "banning negativity" 声明；Office Hours 成为标志性沟通工具。
- **2023/2 – 5**：Max Sills（General Counsel）、Caleb Kruse（Chief of Staff）、Bhavin Patel（Head of Finance）接连加入——**核心运营层级首次成型**。
- **2023 年中**：V5 发布；ARR 达到约 $200M，员工数约 40–50。
- **2023/12**：Ahmad Abbas 悄悄加入，title 为 Head of Hardware（对外未宣布，信号在 2024 年 8 月才释放）。

#### 2024 — Web 版、硬件宣布、131 人

- **2024/初**：V6 发布。
- **2024/3**：主动在 2024 大选前屏蔽 Trump/Biden 图像生成。
- **2024/8/12**：midjourney.com web 平台上线，V6.1 同期发布——首次摆脱 Discord-only 入口。
- **2024/8/28**：在 X 宣布 "We're officially getting into hardware"（Midjourney X）。
- **2024/12**：Patchwork（多人 worldbuilding 工具）上线。
- **2024 年底**：员工数约 131 人，ARR 约 $300M；Stripe 认证为 "most globally distributed merchant"。

#### 2025 — Video、$500M ARR、Disney 诉讼

- **2025/4**：V7 上线。
- **2025/4**：Amy Kux 接替 Nadia Ali 出任 CFO；Nadia 转为 Advisor 并加入 Emergence AI。
- **2025/5**：Erik Martin（Head of Community）离职；该岗目前悬空。
- **2025/6/11**：Disney + Universal 起诉 Midjourney——generative AI 公司第一次面对 Hollywood 主要制片厂的正面法律攻势。
- **2025/6/18**：Video V1 上线；Holz 署名 "David" 发布博客。
- **2025/8/27**：Holz 入选 TIME 100 AI 2025。
- **2025 年底**：Warner Bros. 起诉；ARR 估计 $500M；员工数约 107–163。

#### 2026 — V8、Singularity Tweet、竞争加剧

- **2026/1/4**：Holz 的 "nothing is going to be the same anymore" 推文刷屏。
- **2026/2**：Niji V7 personalization profiles 部署；Holz 发布 humanoid robots 视觉宏图。
- **2026/3**：V8 Alpha；The Information 发表 "Can Midjourney Survive Google?" 深度报道。
- **2026/4**：Office Hours 报告 ARR 接近 $600M；员工数估计 163 – 190（LinkedIn profile 可见数）。

来源汇总：Contrary Research、TechCrunch 2024/8/28、PetaPixel 2024/8/29、Variety 2025/6/19、The Agent Times 2026/4。

---

## 九、Analyst 观察与反差点（Analyst Notes）

1. **Headcount 不透明是 intentional。** LinkedIn 上 "11–50 employees" 横幅从未更新。Stanford CRFM 因此给 0/1 分。Midjourney 把不透明当成组织文化的一部分。
2. **Extremely flat org 到了非典型程度。** 在 $500M+ ARR 体量、150+ 人的公司里，没有 CTO、COO、CPO、VP Engineering 是极为罕见的。Chief of Staff 是唯一的协调层。
3. **Leap Motion Alumni 是核心结构性资产。** Holz、Abbas、Kruse、Ali 来自同一家公司，这既保证了执行默契，也意味着组织抗风险依赖于小圈子。
4. **Community Moderation 已完成 volunteer → paid 过渡，但 guides 仍是志愿者。** 2024 年 Reddit 上的一手叙述确认 moderators 已转为 FTE（Reddit, 2024/10）。
5. **Hardware 是真做，但 stealth。** Ahmad Abbas 的 Vision Pro 背景 + 2024/8 至今持续发 SF 现场 hardware 岗位 → 高概率是 spatial computing / mixed reality 方向。
6. **没有 API = 战略选择，不是能力缺陷。** Holz 多次在 Office Hours 表态不做 API，原因是 API 会稀释 community，破坏 "imagining together" 的产品哲学。
7. **Self-funded 的结构性含义：没有董事会、没有 board-level 继任机制。** 如果 Holz 离开，公司治理没有明确继任路径——这是 Midjourney 最大的 key-person risk。
8. **Niji / Spellbrush 合作揭示了 Midjourney 的 partnership 风格：** 不收购、不控股，而是做"模型基础设施 × 美学方向"的分工——这可能是未来更多 vertical partnership 的模板。

---

#### 9.1 补充组织证据：专业采用和外部创意组织形态

原报告的 Analyst Notes 关注公司内部结构；这些证据进一步显示 Midjourney 如何改变外部设计工作室、独立创意人、品牌团队和平台合作的组织方式。

### E01 — 真实设计工作室已经把 Midjourney 用进客户项目，而不是只做概念演示

Stephen Gates 的材料最直接证明了 Midjourney 已经进入付费设计服务。他经营设计工作室 Crazy，过去两年用 Midjourney 和相邻工具给真实客户做 branding、advertising、digital experience、product 和概念内容。客户预算变紧，创意需求更高，AI 让小工作室能产出以前预算不支持的视觉。

这不是“设计师会不会失业”的问题，而是小型设计组织能不能用 AI 吃掉过去需要摄影、制片、retouch、agency team 才能做的一部分工作。

“我们不是在讲 Batman pop-up store 或 Iron Man 变成武士这种理论展示，我们是一家真实设计工作室，过去两年用 Midjourney 和其他工具给真实客户做真实工作；预算越来越紧，客户还想要更多创意，所以我们用这些工具创造他们以前根本没有预算生产的高端产品视觉、广告、活动和品牌内容。” —— Stephen Gates, The Crazy One, 2026-04-22


### E02 — 客户真正付费的是 repeatability，不是第一张漂亮图

专业工作流的核心不是生成一张好图，而是把它变成 campaign。Stephen Gates 说，很多大 agency 或艺术家找到他们，是因为自己做出一张喜欢的 AI 图后，不知道怎样做第二张、第三张、十二张，不知道如何让它们像同一套昂贵拍摄项目。

Midjourney 的商业价值因此不是 one-shot magic，而是 reference、style、prompt、character、finishing stack 和 repeat workflow 的组合。

“我们甚至会被大型 agency 和艺术家雇佣，因为他们做出一张喜欢的图后说太好了，把它变成 campaign 吧，然后发现自己不知道怎么做第二张；做一张不错图不是火箭科学，真正的 trick 是做 12 张，做一整个 campaign，让它们像同一个昂贵拍摄项目，而不是一堆 AI one-offs。” —— Stephen Gates, The Crazy One, 2026-04-22


### E03 — AI 创意交付物从照片本身，转成客户可复用的品牌生成包

Jamey Gannon 的 consistent brand image 流程显示，Midjourney 的 professional adoption 已经开始产品化。她交付给客户的不是照片，而是 final prompt、profile code、stylization、reference photos、image context 和 Figma package。客户拿到的是一套可复用生成接口，而不是一组静态资产。

这对 agency economics 的冲击很大。过去代理商交付照片，客户要更多素材就续费；现在 creative director 可以定义一个视觉空间，让客户在边界内继续生产。

“我通常会在 Figma 里交付，把最终 prompt、用到的 profiles、stylization 和 reference photos 都贴进去；这些图像里大多数甚至 90% 以上都来自同一个 setup。过去创意总监或代理商给你照片，然后说要更多就再来找我们，现在我是在定义这个空间，给你代码和参考，让你能自己继续做。” —— Jamey Gannon / Claire Vo, How I AI, 2026-04-21


### E04 — 高 taste 的独立创意人可以不再被迫扩成 agency

Jamey 对 agency route 的反思，是 Midjourney 对组织形态影响最直接的一段。传统品牌设计师要扩大收入，常被建议开 agency，但 agency 带来销售、项目管理、B player、薪资压力和毛利稀释。AI 让独立创意人或极小团队能承接更高价值项目、保留更多收入和控制权。

这意味着 Midjourney 不只是提升个人效率，而是在改变创意服务业的最小经济单位。一个高 taste 的 solo operator 加 AI，可以更像微型工作室。

“以前大家总说你应该开 agency、招人、接更多客户，但对品牌设计师来说，找一个 junior 很难，合同只有一万到一万五美元时，找人帮忙基本就是把项目拆掉；现在如果你很 lean，可能只需要一个 contractor，甚至自己加 AI，就能接五万美元项目，保留大部分钱，也不用背 payroll 和持续找客户的压力。” —— Jamey Gannon, Dive Club, 2026-04-21


### E05 — Startup 品牌团队用 Midjourney 跟上产品团队每周发布的速度

Perplexity 的品牌案例说明 Midjourney 的价值不只是降低成本，而是改变跨职能节奏。产品团队每周 all-hands 后会聚焦即将发布的功能，品牌团队需要围绕 launch 快速做视觉表达。Midjourney、Luma、Runway 让视觉团队能和产品团队一样快。

对 AI-native 公司来说，品牌不再是季度 campaign，而是每周甚至更高频的视觉实验。Midjourney 把品牌团队从 stock image 和外部摄影制片的节奏里解放出来。

“很多品牌工作其实来自产品团队和 growth 团队，每周 all-hands 会说这周聚焦什么、要发布什么，我们品牌团队就围绕那个 launch 聚起来；因为几乎每周都有大东西要发，时间线很短，所以 Midjourney、Luma、Runway 这些工具让我们有机会和产品团队移动得一样快。” —— Phi Hoang, Dive Club, 2026-04-21


### E06 — Midjourney 是 aesthetic engine，其他模型补 reasoning 和 edit

专业用户并不把 Midjourney 当全能工具。Jamey Gannon 的模型分工很清楚：Midjourney 是 aesthetic engine，负责让东西有感觉、不像普通 AI 图；Nano Banana Pro 是 reasoning engine，擅长听指令、现实感和文字。真实工作流是多模型流水线，Midjourney 负责创造值得继续修的起点。

这既是 Midjourney 的强项，也是边界。如果它不能继续拥有 workspace，专业用户会把 Midjourney 放进更大的工具链里，而不是把完整流程留在 Midjourney。

“我 90% 的时间用 Midjourney 和 Nano Banana Pro；Nano Banana Pro 是 reasoning engine，擅长听指令、现实感和文字，甚至整页文字都能很准，而 Midjourney 是 aesthetic engine，它能做出真的有感觉的东西，不会一直像那种 stark AI 图。” —— Jamey Gannon, Dive Club, 2026-04-21


### E07 — Meta licensing 说明 Midjourney 的资产可以从订阅扩展为平台级审美层

Meta deal 的战略信号是：大平台不只是想要一个图片生成 API，而是想要 Midjourney 这种经过社区调参、prompt 文化和审美反馈训练出来的视觉味道。Instagram、Facebook、WhatsApp、广告和 creative effects 都可能成为 Midjourney aesthetic tech 的分发场。

这条路能放大 Midjourney，但也有代价。Meta 掌握用户关系、分发和广告客户，Midjourney 掌握审美引擎。长期价值分配取决于 Midjourney 是否继续拥有 direct creator relationship 和自有创作界面。

“第一个故事是 Meta 和 Midjourney 合作，Instagram 像是要拿到一支新的画笔；拥有 Facebook、Instagram 和 WhatsApp 的 Meta 刚刚和 Midjourney 做了一笔 licensing deal。Midjourney 是最早的一批图像生成器之一，也是那种梦境感、过于完美、大家过去几年一直在发的图片背后的代表工具；现在可以把它想成 Photoshop 加上一场发烧梦，精致、超现实、非常适合 Instagram。Meta 基本上是在说，我们希望自己的应用看起来也像那样。” —— Chris / Rift Theory, 2025-08-26


#### 9.2 补充组织证据：治理、IP、API、support 与 moderation 产品化

这些治理证据说明，Midjourney 后续的组织复杂度不会只来自更多员工，而会来自 API、IP 授权、Hollywood lawsuit、专业用户版权边界和 support/moderation 系统化。

### F01 — API 被延后，是因为 moderation 容量还不够

2023 年 David 对 API 的回答非常关键。Midjourney 暂时不做 API，不是因为没有需求，而是因为要先解决 moderation。一旦开放 API，公司就不只要管理自己平台上的用户，还要管理 API service 里的使用。

这句话把商业上限和组织瓶颈连在一起。API 能带来更大分发和收入，但如果治理系统没有规模化，它会把外部风险带进公司。

“我们现在没有计划做 API。我觉得我们得先解决 moderation，因为一旦有 API，我们就不只是管 Midjourney 自己平台上的用户，还要去管 API service 里的使用；我们现在没有时间同时 moderation 这两边。如果以后有 API，我们也许会赞助 hackathon，但现在大概会先按住。” —— David Holz, Midjourney Office Hours, 2023-07-26


### F02 — Disney / Universal 案把风险从训练数据推到角色输出

Rob Rosenberg 把 Disney / Universal vs. Midjourney 称为 output phase。前面的训练案主要问模型输入是否 fair use；这个案子直接问 Midjourney 是否向用户输出 Mickey、Darth Vader、Disney princesses、Spider-Man、Minions 等可识别 IP，并从中收费。

这让 Midjourney 的风险和产品价值重合。它越能稳定生成用户想要的文化符号和角色，越容易进入权利方的可主张市场。

“我常开玩笑说，我们现在到了 show me the output 阶段。把大量材料放进模型里是一回事，先不说我是否承认训练 fair use 已经是最终结论；但 Disney 和 Universal 这个案子真正重要的地方，是它聚焦模型到底向消费者输出什么。视觉艺术里，起诉书的说法就是：你把 Mickey Mouse、Darth Vader、Disney 公主这些东西喂进模型，现在又输出让所有人都能认出 Spider-Man、Minions 或其他角色的图像，你在向用户收费，却没有任何权利去创作这些受保护 IP 的衍生作品。” —— Rob Rosenberg, Technically Creative, 2025-09-09


### F03 — 最可行的产业路径不是等判决，而是把授权和 guardrails 做成交易

Rob Rosenberg 的核心建议不是“等法院说清楚”，而是 make a deal。AI 平台、权利方和创作者需要把训练、输出、使用场景、补偿、credit 和 guardrails 写进交易。对 Midjourney 来说，未来真正能卖给 Hollywood 的，不只是“图像好”，而是“你的 IP 可以在生成环境里被可控使用”。

这会把 Midjourney 推向全新的组织能力：BD、rights management、policy、brand safety、输出审计和合同履约。

“我认为最好的前进路径就是坐下来把交易做成。双方需要聚在一起，把问题解决掉，谈出条款。这里当然有钱可以分，而且确定性对所有人都更好：对创意社区更好，对 AI 平台也更好。现在这种猜、等法院判的状态，给技术部署造成了很大停滞。所以当平台愿意站出来拿 license，就可以处理补偿、credit，也可以在协议里写清楚输出端能做什么、不能做什么，以及这些参数和 guardrails 怎么设定。” —— Rob Rosenberg, Technically Creative, 2025-09-09


### F04 — Guardrails 会变成生成式视觉平台的产品功能

授权不是只拿到“能不能用角色”的许可，还要控制 IP 被放进什么语境。Disney、Universal 或任何大品牌都不会允许角色出现在色情、极端政治、仇恨、品牌贬损或不合适商业场景里。Midjourney 如果要做 IP licensing，policy 必须变成产品。

这意味着 prompt 过滤、输出识别、用户分级、使用场景限制、申诉机制、审计日志、品牌 owner 控制台，都会成为商业必要条件。过去的 Discord moderation 不够，治理会成为平台基础设施。

“你当然还要围绕它建立 guardrails。归根到底，你必须确保人们不会用你的 IP 做那些不可说、低俗、贬损品牌的事情；这些都是你不能允许的，所有 licensing deals 里都会包含这些限制。也就是说，许可本身只是第一步，真正难的是让平台能控制上下文，知道哪些用途被允许、哪些用途被禁止，并且让权利方相信这些限制真的能执行。” —— Rob Rosenberg, Technically Creative, 2025-09-09


### F05 — Midjourney 不关掉角色能力，是因为法律风险和用户付费价值绑定在一起

法律播客对 Disney / Universal 案的判断很锋利：为什么 Midjourney 不像一些聊天模型那样严格过滤角色输出？最直接的答案是用户喜欢这样做，而且这就是他们付费购买的能力之一。过滤太严会削弱产品吸引力，过滤太松会放大法律风险。

所以 Midjourney 不能只在“放开”和“一刀切”之间选择。它必须做细粒度治理：哪些用户、哪些场景、哪些 IP、哪些输出、哪些商业用途可以被允许，哪些必须拒绝或转向授权路径。

“为什么 Midjourney 不把这些能力关掉？最明显的答案是用户喜欢这样做，而且这就是他们付费购买的东西，所以为什么要让你的产品变得更差。你在其他模型上不一定能这么做，Claude 或 ChatGPT 可能会拒绝类似请求；但 Midjourney 如果把大量角色、风格和流行 IP 的生成都关掉，产品吸引力会明显下降。这也是这案子锋利的地方：法律风险和用户愿意付费的能力，刚好是同一个东西。” —— A Lawyer's Guide to the Galaxy, 2025-06-17


### F06 — 纯 AI 生成作品的版权缺口，会反过来限制专业用户采用

如果 Midjourney 被用来生成大量新角色、新世界观、新品牌资产，但这些资产的版权状态不稳定，专业用户会在发行、授权、衍生品、游戏和影视开发时犹豫。美国版权局当前对纯 AI 生成作品的立场，会让用户更关心 human input、编辑过程、权利来源和可保护元素。

Midjourney 如果想成为创意生产基础设施，可能需要帮助用户记录 prompt iteration、human editing、reference provenance 和最终作品的人类贡献。版权治理不只是防御诉讼，也会影响客户是否敢把 Midjourney 输出变成资产。

“至少按美国版权局目前的立场，AI created works 不受版权保护。当然也有例外，比如人类输入和互动足够多，创造出了可独立保护的元素。但这会带来一个很大的未来问号：如果这些由 AI 直接创造出来的 IP 不可保护，那些原本给 copyright owners 的 exclusive rights 就不再属于任何人。你说也许没人再有机会写 Superman，但反过来，可能每个人都能写 Superman；问题是这对资产所有权意味着什么。” —— Rob Rosenberg, Technically Creative, 2025-09-09


### F07 — 早期安全治理靠实时社区操作：office hours、女性小组和 40 个 moderators

Midjourney 不是等到 Disney / Universal 才开始治理。2022 年 David 已经每周做四小时 office hours，直接和用户讨论边界；遇到 bikini 图片争议，他拉了 12 位女性做 panel，并按她们结论把默认展示改成隐藏；同时有约 40 个 moderators 可以用 slash ban 快速处理词语。

这条证据很组织化：Midjourney 早期治理不是单纯政策文件，而是 founder、用户代表、moderators、词表、展示默认值和模型行为共同组成的实时操作系统。它能支撑社区阶段，但未必天然支撑 API、品牌客户和全球 IP 授权阶段。

“我每周做四个小时 office hours，尽量和很多人直接聊；有一次我拉了十二位女性上来，问她们对 bikini 图片怎么看，要不要禁，我说会照她们说的做。她们几乎一致说不要禁 bikini，但希望把它们隐藏起来，不要让我们被迫看到某些男人生成的 bikini 图，于是我们就这么做了；同时我们有大概 40 个 moderators 盯着，他们有 slash ban 命令，可以马上让某些词不能再用。” —— David Holz, What Future, 2022-11-10


### F08 — Support 和 moderation 要变成会积累的系统，而不是靠人肉客服池

2023 年 David 对 help site 和客服的描述，说明 Midjourney 已经意识到社区规模不能只靠即时答疑。几百万用户不可能都获得实时 support，正确方向是把新问题沉淀进 FAQ、搜索、文档和客服流程，让系统随着回答变好。

这是从社区公司走向平台公司的关键组织转化：把原本依赖 moderators、office hours 和社区热心人的知识，沉淀成可搜索、可复用、可训练新用户的支持系统。它同时会降低 V8 学习成本、减少重复问题，也为未来 web workspace 和专业用户打基础。

“我们也在做新的 help 网站，可能会是 midjourney.com/help 之类的东西，里面会有很多文档、好用的搜索；如果找不到答案，也可以联系 Midjourney 的客服拿到回复。它不会是实时的，我不觉得以我们现在的规模还能给几百万用户做实时支持；但我们会有团队回答问题，并且每当他们回答了 FAQ 里没有的问题，就把它加进去。我们想把 moderation 和答疑系统化，让它们随着时间变好，而不是像现在这样只是一直在那里、不会积累。” —— David Holz, Midjourney Office Hours, 2023-07-26


### F09 — 最理想的 moderation 不是更长禁词表，而是让模型学会边界

David 2022 年对 moderation 的目标讲得很清楚：长期不是靠越来越长的词过滤，而是让模型理解 nude、blood、gore、冒犯性输出之间的细微差别。也就是说，治理不只是 policy team 的工作，也不是 community team 的工作，它必须进入模型训练和输出控制本身。

这对 Midjourney 的组织要求很高。它需要把 trust & safety、model behavior、用户申诉、社区反馈、法律风险和产品体验接在一起。如果做成，安全会成为模型能力的一部分；如果做不成，API、enterprise、IP licensing 都会被卡住。

“目标应该是几乎没有词过滤，除了 slur 之类的词以外，你可以有语言自由，但图像仍然不会变成冒犯性的东西。比如你要求 nude person，它可能会做裸露感，但用树枝或物体挡住关键部位；它可以有 blood，但不做 gore。我们需要让系统学会这些细微差别，随着它学得更好，过滤就能慢慢放松。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07


---

## 十、参考来源（Primary Sources）

#### 创始人采访 / 直接引语
- The Verge, James Vincent, 2022/8/2
- The Register, Thomas Claburn, 2022/8/1
- Forbes, Rob Salkowitz, 2022/9/16
- PC Gamer, 2022/8/20
- Stratechery, Ben Thompson, 2022/11/10（paywall）
- Nathan Ma YouTube 访谈, 2025/6/1
- @DavidSHolz on X

#### 官方与结构信息
- midjourney.com、jobs 页面
- LinkedIn /company/midjourney
- Stanford CRFM FMTI 2025

#### 行业分析与数据库
- Contrary Research — Midjourney Breakdown
- Levels.fyi — Midjourney Salaries
- ElectroIQ — Midjourney headcount stats
- CompaniesHistory.com — Midjourney Statistics 2026
- Quantumrun — Midjourney Statistics
- The Agent Times, 2026/4

#### 媒体报道
- TechCrunch — Hardware 2024/8/28
- Ars Technica — Hardware 2024/8/29
- PetaPixel — Abbas hire
- Variety — Video V1 & Disney lawsuit
- PCMag — Election image ban
- TIME 100 AI 2025 — David Holz
- Engadget — Free trial ends
- The Verge Command Line — banning negativity

#### 社区与合作
- Spellbrush YC Profile
- Midlibrary — Niji 5 deep dive
- Midjourney Discord Overview docs
- Reddit — Community Moderators thread

---

*报告结束。核心叙述以中文为主，英文专有名词（人名、公司名、岗位名、产品名、产品版本号、职位术语）保留原文，以保持 Midjourney 生态内的术语一致性。*
