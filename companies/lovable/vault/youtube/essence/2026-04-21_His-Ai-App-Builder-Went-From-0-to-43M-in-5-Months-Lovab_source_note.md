---
company: lovable
source_type: youtube
type: source_note
status: done
source_path: companies/lovable/vault/youtube/transcripts/2026-04-21_His-Ai-App-Builder-Went-From-0-to-43M-in-5-Months-Lovab.md
source_title: "His Ai App Builder Went From $0 to $43M in 5 Months | Lovable"
source_date: 2026-04-21
created_at: 2026-04-23
speaker: "Anton Osika"
source_weight: A
relevance: high
note_version: 1.0
quote_language: zh_translation_from_en_transcript
quote_style: single_long_translated_excerpt_per_block
---

# His Ai App Builder Went From $0 to $43M in 5 Months | Lovable - Source Note

## 43M 年收入和 6 万个项目/天，说明 Lovable 已经从 demo 进入 revenue machine

这条访谈最硬的不是标题，而是 Anton 把收入和使用规模直接摆出来：43M annual revenue、每天 60,000 个项目被启动或生成。这个数字说明 Lovable 已经不再只是一个新奇的 AI 工具，而是在进入能持续产生商业价值的阶段。更重要的是，他把“你有一个想法，输入文字，然后直接发布或接 Stripe”讲成了标准流程，这意味着产品已经把创作和上线连成了一条链。

“我们现在的收入是 4,300 万美元一年，而且每天大概有 60,000 个项目被启动、被做出来。最简单地说，你先有一个想法，然后像跟人类软件工程师说话一样，用普通文字把它描述出来，再通过几轮 prompt 继续把它往前推，最后你就可以点一下，把它分享给朋友，或者直接发布到网上，甚至接 Stripe 开始赚钱。” —— Anton Osika, 2026-04-21

## 产品最早的增长不是投放出来的，而是 word of mouth 自己滚起来的

Anton 对增长的解释很克制：先是 Product Hunt，后来是少量 YouTube 视频、我们自己持续发产品更新、再加一点 memes 和内容合作，但真正把曲线推起来的还是 word of mouth。这个结构很重要，因为它说明 Lovable 的分发不是一个单独的增长部门，而是用户在第一次 wow 之后自然扩散出来的结果。换句话说，传播不是附属功能，而是产品体验本身的一部分。

“一开始其实挺慢的，我们先在 Product Hunt 上线，之后才有一点点用户开始用。后来真正起作用的，是 word of mouth。最早有几条 YouTube 视频帮了忙，我们也一直在有节奏地发产品变化、发更新，顺手发一些 memes。现在基本就是这些东西在起作用：产品更新、少量 memes、还有 YouTube 视频。” —— Anton Osika, 2026-04-21

## 从 snake game 到 Lovable，真正的转向是把开发者工具改成全民创作入口

Anton 反复回到 GPT Engineer 的周末 demo：他不是想做一个更快的开发者插件，而是想证明 LLM 可以真的生成软件。等这个证明成立后，方向就变了，目标不再是 1.5% 的开发者，而是 99% 的非开发者。这个转向解释了为什么 Lovable 的产品重心是“从想法到产品”，而不是“从代码到更快的代码”。

“两年多以前我就在想，工程会变得 10 倍更快，所以我想亲自证明这件事。于是我花了几个周末做了一个很粗糙的视频，里面我说 create a snake game，然后它真的帮我做出了一个能跑的蛇形游戏。我突然意识到，也许我比很多人更早看到了这件事，所以我决定不只把它当成开发者工具，而是直接去做一个给所有人用的东西，给那些本来要来回找工程师的人一个真正的 zero to one 入口。” —— Anton Osika, 2026-04-21

## 第二版产品把协作放到了前台，像 Figma 一样让团队一起 prompt

这场访谈里最像“产品升级”的部分，是 Anton 讲第二代 Lovable 不再只是个人试验场，而是开始支持多人协作和并行编辑。这里的类比非常直观：像 Figma 一样，大家可以围着同一个项目一起做，而不是每个人各自单打独斗。对 AI builder 来说，这意味着产品的单位已经从“一个 prompt”变成“一个团队的 workflow”。

“我们的第二个产品版本，核心是让它更 lovable，也更稳定，修掉大量 bug 和 scaling 问题。更重要的是，现在很多人不是一个人做 app，而是和同事、朋友一起做；所以我们开始把协作放到前面，像 Figma 那样，大家可以同时跟进、同时在不同部分上动手，直接一起推动一个项目。” —— Anton Osika, 2026-04-21

## 设计和 backend 一起变成了产品边界，authentication 和 Stripe 是真正的 95%

Anton 对产品边界的说法很实在：最值钱的不是把页面生成出来，而是把真正决定业务能不能跑的部分接上去。authentication、数据持久化、Stripe、外部 API，这些才是软件里最难也最值钱的部分。也正因为如此，Lovable 的竞争不只是“更会生成 UI”，而是“能不能把业务的关键路径一起做出来”。

“我们现在做到的，是不仅能让你很快迭代和编辑界面，还能帮你修 bug、把东西上线。更进一步，你现在可以加用户 authentication、存数据、调用外部 API，比如你自己的 backend、Stripe 做支付，或者在你要做 AI 应用时直接接 OpenAI。说白了，这些已经覆盖了软件里绝大多数的价值。” —— Anton Osika, 2026-04-21

## 教育仍是最大的未解题，Lovable 还缺一个“让人学会用”的层

这篇里 Anton 其实把一个很现实的难点讲得很坦白：产品已经能做很多事，但用户教育还没完全补上。你越要把 Lovable 用到更深的地方，就越需要一点 technical literacy，或者至少有人帮你把关键概念讲清楚。这个点很重要，因为它说明增长的下一阶段不只靠产品功能，而是要把学习路径做出来。

“我们现在还没有完全解决的，是怎么教育用户更好地使用 Lovable。我们很想把钱花在这件事上，让大家更容易学会所有技巧，因为你得稍微懂一点技术，或者身边得有人教你那些关键概念。比如底层到底发生了什么、数据结构是什么、逻辑怎么走，这些东西会明显影响你能不能把产品真正用起来。” —— Anton Osika, 2026-04-21

## 传播和教育会继续吃掉增长，最后要靠更快的 shipping 把欧洲也带起来

访谈的结尾没有停在产品本身，而是把它扩展到欧洲生态：更多触点、更高的学习速度、更强的 shipping cadence，才会让用户真的愿意把信用卡拿出来。Anton 说自己不是最会 marketing，但知道触点越多，用户越容易跨过行动门槛；这说明 Lovable 的增长还会继续和教育、内容、以及欧洲创业文化的提速绑定在一起。

“我们还在持续发产品变化和消息，这些都会有帮助，因为触点越多，越容易到一个阈值，用户就会真的去注册、真的去把信用卡拿出来。对我来说，最想做的还是两件事：一件是让更多不会写代码的人能做公司，另一件是让欧洲这边的人也能更快地 build。我很希望大家把产品拿去试，然后给我们反馈，让我们把 shipping 的速度再拉快一点。” —— Anton Osika, 2026-04-21
