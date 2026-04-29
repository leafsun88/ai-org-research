---
company: Midjourney
research_key: MIDJOURNEY
type: fact_pack
date: 2026-04-20
status: first_pass
---

# Midjourney Fact Pack

## 一句话

Midjourney 是 AI 图像时代最反常识的高人效公司：没有传统 VC、没有重销售、长期小团队，却靠 Discord 社区、付费订阅和极强审美模型做出了全球级消费 AI 产品；它的上限取决于能否把“审美技术”从图片订阅扩成视频、3D、实时模拟和外部模型公司的 taste layer，最大风险来自版权诉讼和企业工作流缺位。

## 公司简介

Midjourney, Inc. 是一家总部位于 San Francisco 的私有 AI 创意公司，由 David Holz 创立。Holz 此前创办 Leap Motion，长期做手势识别、人机交互和 embodied computing。Midjourney 最早在 2021 年作为 independent research lab 启动，2022 年通过 Discord bot 向用户提供 text-to-image 服务。

公司的核心业务是 AI 图像与视频生成。用户通过 Discord 或 midjourney.com 输入 prompt、引用图片或使用风格/角色参考，生成图片、做变体、放大、编辑、扩图，并在 2025 年后用 V1 Video 把图像动画化。官方定价是订阅制：Basic / Standard / Pro / Mega 月价分别为 $10 / $30 / $60 / $120。Midjourney 没有披露财务数据；第三方估算显示其 2023 ARR 约 $200M，2025 收入或 ARR 约 $400M-$500M+，但这些不是公司确认数字。

## 历史发展

| 时间 | 事件 | 来源 |
|---|---|---|
| 2011 | David Holz 创办 Leap Motion，做手势识别与人机交互硬件 | The Verge / Contrary |
| 2019 | Leap Motion 被 Ultrahaptics 收购，后成为 Ultraleap 的一部分 | Contrary |
| 2021 | Holz 离开 Leap Motion 后启动 Midjourney independent research lab | VentureBeat / Contrary |
| 2022 | Midjourney 通过 Discord 提供 text-to-image 服务，The Verge 采访时团队约 10 人、无投资者 | The Verge / VentureBeat |
| 2023 | 第三方估算 Midjourney ARR 约 $200M；Discord 社区已成核心分发与学习空间 | Sacra / Power Law |
| 2024 | Midjourney web app 扩大可用性；第三方研究称 Stripe 认可其全球化商户特征 | Contrary / ProductGrowth |
| 2025-04 | V7 发布 | 官方 docs |
| 2025-06 | V7 成为默认模型；V1 Video 向社区发布 | 官方 updates |
| 2025-06 / 2025-09 | Disney/Universal、Warner Bros. 分别起诉 Midjourney | AP / complaint PDFs |
| 2025-08 | Meta reportedly licenses Midjourney aesthetic technology | Yahoo/Engadget / ProductGrowth |
| 2026-03 / 2026-04 | V8 Alpha、V8.1 Alpha 在 alpha.midjourney.com 测试 | 官方 updates |

## 产品

Midjourney 的产品可以分成四层。

第一层是 Discord / web 生成入口。早期核心是 Discord `/imagine`，所有用户在同一公共空间看别人 prompt、看别人出图、复制与变体。2024 年后 web app 承接更专业的图库管理、参数面板、编辑和探索。

第二层是审美模型。V7 是当前默认稳定模型；官方称其提高 prompt understanding、image quality、image coherence，并引入 Draft Mode 与 Omni Reference。V8/V8.1 仍在 alpha，方向是更快、更便宜、更强 personalization / sref / moodboard / HD / Describe / prompt shortener。

第三层是视频和未来模拟。2025-06 发布的 V1 Video 是 image-to-video，用户用 Animate 把图片变成视频；官方把它描述为 real-time open-world simulations 的 building block。路线是 image、video、3D、real-time model，最后拼成 unified system。

第四层是社区与个性化。Midjourney 的 personalization profiles、moodboards、srefs、ratings、gallery 和 Discord feedback，把用户审美反馈变成产品迭代材料。社区不是外层营销，而是模型学习和用户学习的界面。

## 商业模式

Midjourney 的商业模式非常简单：订阅 + GPU 使用权益 + 商业使用门槛。

官方四档月费是 $10 / $30 / $60 / $120，年付 20% 折扣。Fast GPU Time、Relax、Video、Stealth、并发任务数形成付费梯度。Standard 及以上有无限图片 Relax；Pro/Mega 有无限图片和 SD video Relax；Stealth 只在 Pro/Mega。公司年收入超过 $1M 的商业用户若要拥有资产，需要订阅 Pro 或 Mega。

这个模式的特点是少销售、少免费用户、直接用创作冲动支付 GPU 成本。它和 ChatGPT / Claude 的 token API 逻辑不同，更像“审美算力订阅”。用户越想探索、越追求隐私、越商业化，越自然上升到高价 tier。

## 团队与组织

Midjourney 的组织信号高度一致：小团队、工程师主导、社区优先、founder 深度参与。

Holz 在 2022 年 The Verge 采访中称公司约 10 人、无投资者、没有上市或出售压力。到 2026 年，官方 careers 仍强调团队相对社区和野心非常小，并有意维持这种状态来快速迭代。

Careers 页披露的组织方式非常关键：features are suggested and prioritized by community，projects are led by engineers and founder。它不是产品经理驱动的 roadmap 公司，也不是销售驱动的企业 SaaS 公司，更像一个社区反馈驱动的研究/产品小队。

核心工作域是 research、infrastructure、frontend。Research 关注 diffusion models、reinforcement learning、training optimization、data processing；infrastructure 关注 data center / cluster management、inference optimization、large-scale cloud systems；frontend 关注 web / mobile product design and engineering、新功能原型和 internal tools。Data Engineer 的 JD 指向公司正在补自动化仪表盘、财务规划和增长洞察能力。

招聘标准也很典型：self-directed、communicative、highly proactive；更看 portfolio/projects，而非履历标签。这个标准适合小团队和高不确定产品，但也意味着 Midjourney 可能缺少传统企业软件所需的 sales / implementation / security / compliance 层。

## Founder 认知

Holz 的核心认知不是“AI 画图”，而是“AI 放大人的想象力”。他反复使用 intelligence augmentation 的语言：Leap Motion 是让人更自然地进入计算机，Midjourney 是让人探索新的 thought medium。

最重要的产品洞察是：人单独面对无限可能时往往不会想象，群体才会教人想象。The Verge 访谈里，他讲空白输入框只会得到 dog / pink dog；放进群体后，用户会从别人的 prompt 里理解可能性。这解释了 Midjourney 为什么诞生在 Discord，也解释了为什么公开生成默认值本身就是产品的一部分。

他对商业化也很克制。VentureBeat 2022 年采访里，他明确说 corporate membership 不是 enterprise SaaS，当时无意做企业软件；原因是技术变化太快，consumer side 能让人直接拿来玩和工作，简单性本身很有价值。

## 战略方向

Midjourney 的主线不是从 image app 做成 SaaS 套件，而是从 aesthetic engine 做成 imagination/simulation stack。

短期，V7/V8/V8.1 的目标是提高图像质量、速度、可控性和个性化。中期，V1 Video 把静态图像扩展到 motion；接下来官方路线提到 3D 和 real-time models。长期，官方直接写到 real-time open-world simulations。

另一个值得重视的方向是 taste licensing。Meta reportedly licensing Midjourney 的 aesthetic technology，说明大模型公司也承认 Midjourney 在视觉审美上有独特资产。这个方向的商业模式和 consumer subscription 很不同：它不是把工具卖给创作者，而是把“美感层”卖给模型公司或平台公司。

## Traction 与财务估算

官方没有披露收入、付费用户、员工数或估值。可用口径如下：

- Sacra：估算 2023 ARR 约 $200M，员工约 40-45，人均收入极高。
- Contrary：汇总称 2025 年 Discord server 超过 21M members；2023 revenue reported $200M，2025-05 ARR 估算 $500M；团队仍非常小。
- ProductGrowth：汇总多方估算，称 2024 revenue $300M、2025 revenue $500M、employees 约 107、VC funding $0。
- andrew.ooo：汇总称 2025 revenue $500M、employees 约 163、revenue per employee 约 $3.07M。

这些数字不能混写成事实。更稳妥的表述是：Midjourney 是已被多家第三方研究反复引用的极高人效、self-funded AI consumer subscription 公司；第三方收入估算大致从 2023 年 $200M ARR 到 2025 年 $400M-$500M+，但公司未确认。

## 竞争格局

Midjourney 的优势在审美、社区、个性化和人效；弱点在企业工作流、API、合规和版权保障。

Adobe Firefly / Creative Cloud 的优势是企业工作流和 IP indemnification，更适合品牌、营销和设计团队。OpenAI / Google 的优势是多模态统一入口、API、生态分发和企业安全。Runway / Pika / Veo / Sora 在视频方向更原生。Stable Diffusion / ComfyUI 的优势是开源、可本地化、可定制。Canva / Shutterstock / Getty 等则有现成素材和企业客户。

Midjourney 目前仍像最强的 visual taste engine，而不是最完整的 creative operating system。它的机会在于：如果 V8/V9 + video/3D/real-time simulation 能继续保持审美优势，并通过 web app / licensing / possible API 扩大场景，Midjourney 可能从 consumer AI image app 升级成视觉智能基础层。它的风险在于：如果用户工作流最终被 Adobe/OpenAI/Google/Canva 占据，Midjourney 可能保留高端审美心智，但失去企业预算。

## 法律与政策风险

2025 年 Hollywood lawsuits 把 Midjourney 的核心矛盾摆上台面。Disney / Universal 和 Warner Bros. 的诉讼都围绕训练数据、受保护角色生成、订阅服务是否鼓励侵权等问题展开。Midjourney 的 terms 把用户责任写得很重，也没有公开承诺企业级 IP indemnity。

这对业务影响很直接：创作者个人会为效果买单，但大企业会问两个问题：能不能赔？能不能保证品牌安全？如果答案不清楚，Midjourney 很难进入大型企业的正式创意供应链，只能停留在灵感、草图、个人创作者和部分灰色生产环节。

## 初步投资判断

Midjourney 是一个很漂亮但不典型的 AI 公司样本。它证明了 AI consumer subscription 可以不靠免费补贴、不靠重销售、不靠 VC，也能用极小团队做出全球收入和审美影响力。这个样本的关键不是“11 人做到多少钱”，而是它把 community 变成了 learning interface，把每张图变成了 product demo，把审美差异变成了商业资产。

真正值得继续研究的是两个问题。

第一，Midjourney 的 taste moat 能不能跨形态。图片上的美感优势已经被市场认可；视频、3D、实时模拟会不会继续领先，还是被 Veo/Sora/Runway/Adobe 的工作流和算力压过去？

第二，Midjourney 会不会进入企业预算。Holz 早期选择 consumer-first 是正确的，因为速度和简单性最重要。但 AI 创意工具的大钱最终可能在品牌、广告、游戏、影视、设计和平台授权。Meta licensing 是第一个强信号，说明它的审美资产能被外部平台定价。版权诉讼则是相反的强信号，说明这条路会被权利方反复收费或限制。

当前结论：Midjourney 是视觉生成领域最值得研究的“审美 + 社区 + 小团队人效”案例，但正式投资报告必须把收入和员工数全部标成估算，把版权诉讼和企业合规作为第一风险。
