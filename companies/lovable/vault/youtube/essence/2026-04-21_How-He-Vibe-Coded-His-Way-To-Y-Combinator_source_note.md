---
company: lovable
source_type: youtube
type: source_note
status: done
source_path: companies/lovable/vault/youtube/transcripts/2026-04-21_How-He-Vibe-Coded-His-Way-To-Y-Combinator.md
source_title: "How He Vibe Coded His Way To Y Combinator"
source_date: 2026-04-21
created_at: 2026-04-23
speaker: "Ismile"
source_weight: A
relevance: high
quote_language: zh_translation_from_en_transcript
note_version: 1.0
quote_style: single_long_translated_excerpt_per_block
---

# How He Vibe Coded His Way To Y Combinator - Source Note

> 这篇最值钱的地方，是它把 YC、Lovable、物业维护和获客验证连成了一条完整链路：先做出可卖的最小版本，再用真实客户反馈判断问题值不值得放大。

## YC 这条故事的核心不是“零代码神话”，而是先确认问题值不值得做

他说自己在提交 YC 申请的时候，确实是靠 Lovable 做出来的版本，但 YC 之所以接受这条故事，并不是因为代码有多漂亮，而是因为他已经清楚地验证了问题是否值得解决。Brickwise 的出发点来自家族物业经验，他先知道物业维护的痛点，再把 Lovable 当成把问题快速落地的工具。这个机制很适合放进 Lovable 的业务影响里，因为它说明非技术创始人最需要的不是编程技能本身，而是把问题做成可验证原型的速度。

“在我按下 YC 申请提交按钮的时候，答案是肯定的，我有 Lovable 里的 logs 可以证明这一点，我们有一堆为 prompts 付的钱。不过话说回来，我的 co-founder 是世界上最技术的人之一，YC 其实很清楚这一点。他以前在一家后来被 Google 收购的公司当早期工程师，四个工程师做出来的产品在几年里带来了上亿美元收入。对我们来说，申请里最重要的不是当时做出来的东西有多高质量，而是我们能不能识别出一个值得解决的问题。我认为你不一定要花很长时间写高质量代码，才知道自己是不是在做用户真正想要的东西。” —— Ismile, 2026-04-21

## 产品的真实工作流是把租户请求从电话、短信、WhatsApp、邮件一路接进同一条维护管线

他的 AI property manager 不是一个抽象概念，而是一套很清楚的客户 workflow：租户可以随时通过 WhatsApp、SMS、email、phone 联系系统，系统记录整段对话，再根据问题去找 contractor，必要时还能先自己识别照片里的锅炉品牌、型号和 error code，直接告诉租户要不要先放气或者做简单排查。这里最重要的地方，是 AI 不只是前台接待，而是在维护链路里接手了大量原本靠人工协调的步骤。

“现在这个 agent 可以回复 email、回复 WhatsApp、回复 SMS，也可以接电话。只要电话一接通，整个对话就会被记录下来。然后我们会去找能修这个问题的 contractor，如果 landlord 或 property manager 没有自己偏好的 contractor，我们还接了 Google API 来筛选，按质量和地理位置过滤。我们希望能尽快找到一个可以马上上门的人。如果是大公司，已经有自己的 full-time maintenance staff，那我们就直接帮他们联系内部团队。AI 的厉害之处就在于它能同时做很多事，最厉害的 property manager 一次也只能打一个电话，但 AI 可以一次联系 50 个，然后很快给出 10 个 quote，告诉你哪几个超预算、哪几个今天能来。” —— Ismile, 2026-04-21

## 这个产品的经济模型指向“少雇人也能多管物业”，所以客户愿意为效率买单

他说得很清楚，真正买单的是 landlord 和 property management firm，而且通常是管理 1 到 500 套房产的那群人。之所以值钱，是因为传统模型里你想把 200 套扩到 400 套，往往就得按 1.7 倍去增加员工，而 AI 让你只需要 1.2 倍 staff 就能把产出拉起来。这个数字很适合 Lovable 业务场景，因为它说明 customer workflow 的变化可以直接转成 headcount 约束的放松。

“我们面向的 paying customer 通常是 landlord 或 property management firm，而且一般是后者。他们通常在管 1 到 500 套物业，有的更大，有的更小，但核心问题都是需求太多，处理不过来。你如果现在管 200 套，想扩到 400 套，通常就得 hire 大约 1.7 倍的员工，这很难，因为前期成本太高，而且现金流也不一定跟得上。AI 让这件事变得可能，你不一定要 hire 这么快。以前你可能需要 1.7 倍 staff 才能把输出翻倍，但现在可能只需要 1.2 倍，剩下的缺口由产品补上。” —— Ismile, 2026-04-21

## Lovable 的价值在这里很具体：先把一个能卖的最小版本做出来，再决定要不要重工程化

他用到 Lovable 的方式并不是纯 demo，而是先在应用提交之前用 15 到 1700 个 prompts 把最初版本做出来，让真实客户先用，再在 YC 之后继续补工程化。这个思路非常清楚地说明，Lovable 的强项是帮助创始人先证明需求，再把工程复杂度往后推。对分析来说，这比“它能不能做 production app”更重要，因为大多数业务的第一关本来就不是 production，而是 people want this.

“在申请那会儿，我觉得大概是 1,500 到 1,700 个 prompts，才做出了最初版本的雏形，已经有客户开始用，也开始付钱试了。后来进了 YC，我们才在工程层面补了很多东西，把第三方工具和基础设施接得更完整。对我来说，先做出一个 sufficiently useful 的版本，然后把它放到潜在客户面前看他们会不会点头、会不会愿意试、最好愿不愿意付钱，这比一上来就解决规模问题重要得多。” —— Ismile, 2026-04-21

## 他的获客判断很朴素：先找已经被验证过的需求，再用更短的反馈回路去抢速度

他认为很多创始人会把“独一无二”误当成优势，甚至开始纠结 NDA，但真正有效的做法是找已经存在于市场里的问题，再用 Lovable 把验证回路压缩到几周而不是几个月。这种判断对 Lovable 客户故事特别关键，因为它不是在说“AI 会让创业更浪漫”，而是在说“AI 会让你更快知道自己是不是在浪费时间”。

“如果你要做一个 app 或者一个产品，我会先去找已经被验证过的 idea。很多人会想做特别革命性的东西，甚至在分享之前就要求签 NDA。我想说，如果你的 idea 需要 NDA，那你可能把顺序搞反了。你以为从来没人做过、没人想过的东西是好事，但我觉得全世界有 80 亿人，如果真的没人试过，也许是有原因的。更实际的做法是先去做那些市场里已经存在的问题，然后尽快做出一个够好的版本，放给用户看，听他们反馈。” —— Ismile, 2026-04-21

## 这条路线也说明，Lovable 不是只服务非技术人，design 和 product 背景的人反而最容易跑出来

他在讨论用户画像时说得很坦白：真正能把 AI 工具榨出价值的人，往往是那些既懂产品又懂设计、又知道如何和工程师沟通的人。换句话说，Lovable 并不是把所有技能要求抹平，而是把“会提问题、会判断结果、会迭代”这三件事的价值推得更高。

“我见过很多最容易从这些工具里挖出价值的人，通常是产品设计师、产品经理，或者那些虽然不是工程师，但曾经和工程师密切合作过的人。他们最能理解自己在看什么，也更知道怎么把一个想法推进到可交付的状态。对我来说，这就是 Lovable 最有价值的用户画像之一。” —— Ismile, 2026-04-21
