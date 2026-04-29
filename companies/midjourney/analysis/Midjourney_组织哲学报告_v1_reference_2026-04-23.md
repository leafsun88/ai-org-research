---
company: Midjourney
type: organization_reference_report
date: 2026-04-23
status: v1_reference
source_layer: external_reference
focus: organization
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
