---
company: lovable
source_type: youtube
type: source_note
status: done
source_path: companies/lovable/vault/youtube/transcripts/2026-04-21_How-He-Vibe-Coded-His-1MYear-Education-Platform.md
source_title: "How He Vibe Coded His $1M/Year Education Platform"
source_date: 2026-04-21
created_at: 2026-04-23
speaker: "Muhammad Alerusi"
source_weight: A
relevance: high
quote_language: zh_translation_from_en_transcript
note_version: 1.0
quote_style: single_long_translated_excerpt_per_block
---

# How He Vibe Coded His $1M/Year Education Platform - Source Note

> 这篇最重要的不是“不会写代码也能做平台”，而是一个教育业务如何把学生、老师、排课、作业、运营 KPI 和迁移流程全部塞进一套可维护的 workflow。

## 他不是想自己当程序员，而是想拿回产品控制权

这个案例的起点很像很多 SMB 创业者的真实痛点：外包团队可以写代码，但创始人失去了速度、控制权和理解系统的能力。他和 agency 合作了两年，越来越觉得推进太慢，也不够掌握背后的逻辑，所以他开始学的不是“怎么从零写代码”，而是“怎么看懂开发者语言”。这一步很关键，因为他的 Lovable 使用方式，本质上是在把创始人从被动提需求的人，变成能直接决定产品方向的人。

“我和一个软件开发团队合作了大概两年，但我开始意识到我们推进得没有我想要的那么快，我感觉自己被限制住了。作为一个创业者，很多时候你都想完全控制部署出去的东西和速度，所以这很低效。于是我想学软件开发，但不是为了说我以后自己来开发，而是我想知道一切是怎么工作的，想学会开发者的语言，想知道后端在发生什么，这样我就能和开发者说同一种语言，直接告诉他们该做什么。” —— Muhammad Alerusi, 2026-04-21

## 教育平台的真实复杂度，不在课程本身，而在学生、老师和运营层的多边 workflow

他说自己的平台已经不是一个简单的 course site，而是一套在线教育机构的操作系统：学生侧有课程、测验、作业和排课，老师侧要看作业、发 loom 反馈、管理课堂，管理层则要看效率、占用率、未来三天预约情况，以及什么时候该招人。这个结构说明 Lovable 在教育场景里的价值，不只是把前端做出来，而是把原本分散的经营动作收拢成一个可以实时操作的后台。

“我们有学生看到的界面，有课堂，有排课器，能看到自己和老师安排好的所有课程。还有老师用的界面，老师可以检查作业，给学生发 loom 视频，查看社区，甚至给某些学生删掉或创建课程，还能发 Google Calendar 的 evergreen link。然后还有最高层的管理后台，也就是我和 operations manager 使用的地方，我们可以追踪老师的效率、占用率，以及接下来三天到底还有多少学生在预约，快不快到 100% occupancy，需不需要再招一位老师。” —— Muhammad Alerusi, 2026-04-21

## Lovable 把原来由 Calendly、Zapier 和 Airtable 拼起来的视图，压成了一个后台

这条线索很适合写进 Lovable 的业务影响：他原本为了看老师效率，要把 Calendly、Zapia、Airtable 三套软件串起来，而且还要等 CSV 或中间表。现在他直接在管理 UI 里看 KPI，甚至能判断什么时候 hire、什么时候 fire。这里的经济含义很明确，就是把经营视图从工具拼接状态变成单一控制面，从而减少中间损耗和等待时间。

“以前我为了追踪这些东西，要把 Calendly、Zapia 和 Airtable 三个软件连在一起。Calendly 会把数据发给 Zapia，我还要为 zap 付费，然后 Zapia 再发到 Airtable，我也为 Airtable 付费。结果就是我得为了在 Airtable 的界面里看到老师效率，硬生生把三套软件串起来，更别说有时候我还得等 CSV 文件，整个过程太复杂了。现在我直接在 Lovable 里把管理后台和所有 KPI 做出来了，这样我就知道什么时候该 hire，什么时候该 fire，谁高效，谁不高效。” —— Muhammad Alerusi, 2026-04-21

## 他把 bug 变成个人知识库，这说明 AI 开发真正的护城河是失败记忆的复用

这篇最有意思的 workflow 细节，不是“prompt 多少次”，而是他会把每次卡住的 bug 变成一个可复用的 reference，再让 chat 读这些历史记录，判断当前问题是不是旧问题的变体。他还会让 Lovable 输出 copy-pasteable documentation 和代码解释。这说明 AI 开发最值钱的能力之一，不是单次生成，而是把错误模式变成组织记忆。

“每次我卡在一个 bug 上，我就会给自己做一个 reference。我会写下这个问题为什么没成功，是不是和 RLS policies 有关，是什么什么什么，然后把它上传到代码库里，当成以后用的参考。我会告诉 chat 去读我以前卡住过的这些 reference，看看现在这个问题是不是和以前那些问题有关系。慢慢地，我开始把每一个 bug 都记下来，做成自己的 glossary，甚至像百科全书一样，把这些过去的 bug 都整理起来，这样我就能继续开发我脑子里想到的任何东西。” —— Muhammad Alerusi, 2026-04-21

## 这个案例的增长不是纯技术胜利，而是 personal brand 和 audience distribution 的胜利

他不是先从冷启动 SaaS 开始，而是先有了 YouTube、Instagram 和真实受众。120,000 YouTube 订阅者、持续做内容、做 podcast、做 email list，这些都让他在推出新产品时有了天然分发。接近 100 万收入的教育业务，加上 Lovable 帮他把平台做快，最后才形成一个“产品 + 品牌 + 内容”的复合增长模型。

“对我来说，personal branding 太重要了。你要有自己的 audience，要让大家知道你是某个细分领域的人，在我这里就是阿拉伯语。只要你真的围绕这个身份做内容，就会很容易把相关的产品推出去。我的做法基本上就是做内容，这就是一个 numbers game，你得不断发内容，尝试 joint ventures，参加 podcasts，建立 email list，尽可能多地提供价值，慢慢地它就会复利起来。我们 YouTube 现在已经有 120,000 个订阅者，而且今年大概率会跨过七位数收入。” —— Muhammad Alerusi, 2026-04-21

## 迁移过程之所以顺，是因为 Lovable 先把 onboarding 做成了可控流程

他补了一句很关键的话：平台迁移不是理所当然会顺利的，但他通过 Lovable 做出了一套 onboarding 过程，所以客户迁移是他整个业务历史上最顺的一次。对教育平台来说，这意味着 Lovable 不只是用来做新功能，也能把一个老业务的迁移和切换做成更轻的 customer workflow。

“迁移过程当然会有点麻烦，毕竟从一个软件迁到另一个软件，客户总会觉得有一点 headache。但我最后是用 Lovable 做了一个 onboarding process，这次迁移是我们这个业务历史上最顺的一次。” —— Muhammad Alerusi, 2026-04-21

## 这条故事最后落回一个很朴素的判断：先把自己会的事情变成可复制的产品

他对观众的建议并不玄学，而是先用 Lovable 把自己的想法和行业经验变成产品，再把它推给市场。对于研究 Lovable 业务影响来说，这类案例的重要性在于它展示了一个非常典型的 SMB / education 路径：不是技术公司变教育公司，而是创始人先有行业理解，再用 AI 把自己原来需要外包的能力收回到自己手里。

“我现在会跟身边的创业者说，你们真的得开始用 Lovable，开始自己搭产品，把它放到市场上，甚至把它卖出去。” —— Muhammad Alerusi, 2026-04-21
