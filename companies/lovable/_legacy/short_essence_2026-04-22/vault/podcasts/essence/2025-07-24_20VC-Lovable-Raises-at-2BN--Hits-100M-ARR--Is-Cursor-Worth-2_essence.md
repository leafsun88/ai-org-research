---
company: lovable
source_type: podcasts
type: source_essence
status: done
source_path: companies/lovable/vault/podcasts/transcripts/2025-07-24_20VC-Lovable-Raises-at-2BN--Hits-100M-ARR--Is-Cursor-Worth-2.md
source_title: "20VC: Lovable Raises at $2BN & Hits $100M ARR"
date: 2025-07-24
created_at: 2026-04-21
relevance: high
speaker: "Harry Stebbings / Jason Lemkin / Rory Driscoll"
essence_version: 1
---

# 20VC: Lovable Raises at $2BN & Hits $100M ARR

## 第三方投资人真正改变判断的，是亲手 vibe coding 后意识到“非工程用户市场”刚刚开始

这条圆桌不是 Lovable 管理层访谈，但相关性很高，因为它记录了投资人从旁观者变成用户后的认知变化。Jason Lemkin 的判断很直接：vibe coding 才刚开始，非开发者市场只走了几个月，开发者市场也不到一年。对 Lovable 来说，这个外部反馈比融资新闻更有价值，它证明产品不只是在 AI 圈内被讨论，而是在懂 SaaS、懂市场的投资人身上触发了“以前做不到的事现在能做”的体验。这是 AI 应用层爆发的典型信号。

“I've learned so much in one week. It's crazy. It's the biggest firehose. I think your investment in Lovable is even better than I realized a week ago. These apps, you can't stop. It's really a tsunami. Vibe coding has just started. We're only six months into non-developer vibe coding and less than a year into it for developers. The things you can do on these platforms are something you could never do before, and that's where you make money in venture.” —— Jason Lemkin, 20VC Roundtable, 2025-07-24

## Lovable 比 Cursor 更难做，因为它服务的是不懂背景知识的用户，也因此更可能长出厚 wrapper

圆桌里对 Lovable vs Cursor 的区分很有用：Cursor 面向 proficient engineer，用户自己懂背景、懂测试、懂架构，工具只需要提升开发效率；Lovable 面向更少技术背景的人，必须替用户处理更完整的问题，包括安全、部署、约束、工作流和错误边界。这让 Lovable 的任务更难，但也让它更有机会长出厚的 product wrapper。如果它真能把“非工程用户也能安全生成可运行软件”做稳，价值会比 IDE 插件更接近平台。

“Lovable or Replit is building for a business developer person who is technically savvy but not an engineer. They want to solve the whole problem, so the platform has to do a lot for you. Cursor is selling to the software engineer, where the implied assumption is that the engineer understands a lot of the background stuff. In one sense Cursor writes for a proficient user; Lovable is building a tool for a less proficient user.” —— 20VC Roundtable, 2025-07-24

“If I use my spreadsheet approach, I might say go invest in Cursor. But if I want to build something enduring for a generation, I want to do Lovable. If these are wrappers, another Windsurf can emerge. But Lovable, on the TAM expansion, is a much bigger opportunity if every human can use it.” —— Jason Lemkin, 20VC Roundtable, 2025-07-24

## Security 会变成 Lovable 的 defensibility，因为 agent 触碰生产环境后必须被“装甲化”

这条材料对 Lovable 的风险讲得比 founder 自己更尖锐：vibe coding 的危险不是生成代码，而是 agent 可能触碰 production database、改真实环境、拿走数据。圆桌里把 Lovable 的防御性放在“armor around AI”上：它必须对 Claude / model 输出加上安全、限制、预览、staging、审计和部署边界。这和用户后来要求的 controllable speed 完全一致。Lovable 越服务非工程用户，越不能只卖快，必须把工程团队过去默认知道的安全常识产品化。

“I did not understand that the agent could help me build the website and the platform, but also change any line of code even when it was out in the wild, in the real world. We have preview, staging and production servers; it's been done since the dawn of web software. If you're a business person, you don't know what's going on. Enterprises are terrified because an agent will go out and change things in its database or take data.” —— Jason Lemkin, 20VC Roundtable, 2025-07-24

“Lovable is going to build thicker and thicker wrappers because they have to do security. They have to contain the AI. These guys are going to build armor around it, and that armor is going to be very defensible.” —— 20VC Roundtable, 2025-07-24

## Anthropic dependency 不是短期死穴，但会成为平台分润压力

圆桌对 Anthropic / Cursor / Lovable 关系的讨论很有投资价值：短期 Anthropic 没必要切掉最大客户，因为客户增长解释了它自己的收入加速；长期平台公司会像 Microsoft 一样“grind everyone down”，通过价格、访问、产品重叠拿走更多价值。Lovable 的启示是，它必须避免成为可替换薄 wrapper，把真正的用户上下文、应用生命周期、安全体系和企业工作流留在自己层里。否则模型平台上游收租时，应用层毛利会被挤压。

“If Cursor is doing a billion, what percent of that is going to Anthropic? What percent explains the magnificent Anthropic acceleration in the last six months? You're like: knock yourself out. I'll have a slightly competing product; for now, let a thousand flowers bloom. At some point, when things get tougher, just like Microsoft did in the 90s, the platform provider starts to grind everyone down and take more share.” —— 20VC Roundtable, 2025-07-24

“It would be very stupid of Anthropic to cut off probably the largest customer to these products. They are not stupid, so I don't think they will. But when they cut Windsurf off, it was ruthless. You have to assume it's going to happen again.” —— 20VC Roundtable, 2025-07-24

## Lovable 的竞争问题不是模型强弱，而是能不能把普通用户的完整问题接住

圆桌最后形成的判断是，开发者工具市场可能更快出收入，因为每个工程师都能买 200 美元订阅；Lovable 的更大机会在于把“每个人都能 build”变成平台。但这要求 Lovable 比 Cursor 做更多事情：理解模糊需求、处理应用架构、安全、部署、支付、协作、用户不会说清楚的问题。这个难度本身就是护城河的来源。它也说明 Lovable 后续组织必须补 enterprise、security、support、quality，而不是停留在爆款 demo。

“Every engineer is going to get a subscription to Claude Code. If I have my spreadsheet team, I can tell them to invest in those guys. But if I use the seed-guy approach and ask what could be enduring for a generation, I look at Lovable. The spreadsheet says invest in Claude or Cursor; the trillion-dollar bet says Lovable because the TAM expands if every human can use it.” —— 20VC Roundtable, 2025-07-24

