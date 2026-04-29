---
company: lovable
source_type: youtube
type: source_note
status: done
source_path: companies/lovable/vault/youtube/transcripts/2026-04-21_How-Lovable-Manages-100-Daily-Changes-Vibe-Coding-Shado.md
source_title: "How Lovable Manages 100+ Daily Changes, Vibe Coding & Shadow AI"
source_date: 2026-04-21
created_at: 2026-04-23
speaker: "Eigor Andre Shinko"
source_weight: A
relevance: high
quote_language: zh_translation_from_en_transcript
---

# Lovable 的 100+ Daily Changes 把安全工作改造成变更节流系统

## AI-native 公司的安全问题，先看变更速率，不是先看漏洞名单

Lovable 这类 AI 原生公司在安全上真正爆炸的不是某一个漏洞，而是变化速率本身。Eigor 把问题讲得很直白：开发者用 AI agent 并行跑，改动数量会从“每天几次”跳成“每天五十、一百次”，而旧的 CI/CD、审计、人工 review 体系是按低变更频率设计的。安全团队不再只是检查状态是否安全，而是要在高速 churn 里维持可控边界，这意味着安全组织本身必须像变更系统一样工作。

“我看到的是，随着大家采用更多 AI agent，而且还把它们并行跑起来，整个变化速度和变化数量都会爆炸。每个开发者都想更高产、都想解决最难的问题，这当然有工具来配合；但在 Lovable，我们正站在这条变化曲线的最前面，所以我们看到的是别人六个月、一年后才会遇到的事。对安全来说，变化就是风险。你可以把系统维持在一个相对安全的状态，但如果这个状态一天变一百次，你就需要完全不同的办法，单靠人已经不够了。” —— Eigor Andre Shinko, AI Security Podcast, 2026-04-21

## 不要为了 AI 而 AI，先找能控住风险的 air pockets

Eigor 对组织落地 AI 的建议不是“全员上 AI”，而是先找可控的 air pockets。对银行、传统企业和大组织来说，最合理的切入口是无数据或低风险的原型、内部工具和局部流程，而不是一开始就把核心生产系统和敏感数据全开。这个判断很重要，因为它把 AI adoption 从口号拉回到组织设计：先定义问题，再决定谁能接触什么，最后才谈工具。

“我会建议大家先找这些 air pockets。你可以把它想成在一个正在进水的洞里找还能呼吸的地方。先从安全的局部开始，比如做简单原型，不接真实数据，先做个登陆页、内部工具、或者只是把某个想法可视化出来。等人们真的开始喜欢它了，再慢慢找到更多可以放 AI 的地方。不要为了 AI 而 AI，也不要为了展示而硬上。先让它解决具体问题，如果它真的能把某个环节提速十倍，你根本不需要在公司内部卖弄‘这是 AI’，大家自己就会感受到价值。” —— Eigor Andre Shinko, AI Security Podcast, 2026-04-21

## AI agent 像另一名开发者，生产权限必须有人类门禁

Lovable 的安全思路不是把 AI 当成黑盒外挂，而是把它当成会继承开发者权限的“另一名开发者”。这会直接推导出一个组织设计结论：开发环境可以相对宽松，但生产 secret、敏感权限和 escalation 路径必须有人类控制。Eigor 强调的“blessed path”和“healthy friction”其实是在说，AI 能帮你跑得更快，但组织仍要保留让人回到可审计路径上的门槛。

“如果你是一个能访问很多东西的开发者，而你又想让 AI 帮你做事，你基本上就是在把你的权限、凭据和知识都一并交给它。所以你要把它看成另一个开发者。比如说，开发环境的 secret 可以比较容易拿到，但生产 secret 就应该需要额外审批、额外升级权限。AI 本身做不了这个升级，这反而是好事，因为这会带来健康的摩擦，让人回到被祝福的路径上。我们以前在 DevSecOps 里就做过这些事，只是现在需要把这些概念重新应用到 AI 上。” —— Eigor Andre Shinko, AI Security Podcast, 2026-04-21

## 真正的 adoption 靠技能、连接器和教育，不靠把 Copilot 塞给所有人

这段访谈里最有价值的组织信号，是 Lovable 内部的 AI adoption 不是靠“人人装一个工具”，而是靠连接器、skills、MCP server 和内部培训。Eigor 说得很明确：如果你想让 AI 真正做事，就要先把数据源、日志、审批和动作封装成能被 agent 调用的技能，再让团队知道这些技能能做什么。这说明 Lovable 的 AI 化不是 UI 层的热闹，而是组织基础设施层的铺设。

“很多公司以为，只要给每个人装上 Copilot 之类的东西，AI adoption 就会自己发生。但真正重要的是那些不那么性感的工作：你要先做出很多好用的 skills，打通数据连接，必要的时候还要自己搭 MCP server，然后再教大家这些东西怎么用。比如我们有一个 incident responder skill，当出现可疑告警时，agent 可以直接接手调查，把结果带回来。这个 skill、这些连接和知识共享才是 adoption 的底座，不是发一个工具就完了。” —— Eigor Andre Shinko, AI Security Podcast, 2026-04-21

## 安全产品和供应商都要跟上变更量，否则就是被业务节奏碾过去

Eigor 还给了一个很实用的采购判断：AI 原生公司会把安全工具按每天成千上万次扫描、持续变化的节奏来压测，所以供应商必须能吞下这种 volume。换句话说，Lovable 的安全团队不是在问“这个产品能不能找漏洞”，而是在问“它能不能在我们这种变化速度里持续工作”。这类公司一旦进入超高速增长，安全能力本身就会变成业务可扩张性的前置条件。

“工具的性能要求已经变得非常高。我们希望它在很短时间内完成扫描，而且一天要能跑成千上万次。对一家还很年轻的公司来说，这其实已经成了采购标准的一部分：它能不能跟上我们的 change pace？这个节奏在我们把它引进来之后到真正跑进生产环境之前，可能还会再翻十倍。所以，问题不只是我们怎么用 AI，而是供应商能不能撑住这条变化曲线。” —— Eigor Andre Shinko, AI Security Podcast, 2026-04-21

