---
company: lovable
source_type: podcasts
type: source_essence
status: done
source_path: companies/lovable/vault/podcasts/transcripts/2025-05-21_Conversation-with-Anton-Osika-Lovable.md
source_title: "Conversation with Anton Osika, Lovable"
date: 2025-05-21
created_at: 2026-04-21
relevance: high
speaker: "Anton Osika"
essence_version: 1
---

# Conversation with Anton Osika, Lovable

## Lovable 的产品定义从一开始就是 operating system，而不是一次性生成网页

Anton 对 Lovable 的一句描述很关键：用户用自然语言描述应用，Lovable 生成前端、后端、AI chat、login、data storage、payments，最后直接发布链接。这不是单点代码生成，而是把从 idea 到可发布产品的多段工作流合到一个界面里。他进一步说 Lovable 要成为新一代创业者构建 AI native businesses 的 operating system。这个 framing 解释了 Lovable 后续为什么自然会补 analytics、SEO、payments、security 和 business lifecycle。

“Lovable is like ChatGPT and Figma had a baby. You explain in plain English, or any language, what application or website you want built, and then it will be created. You can add AI chat features, login, storing data, and generally make it look really nice. When you're done, you get a link that is published on the internet and you can share it with your friends.” —— Anton Osika, Inside AI, 2025-05-21

“We're seeing thousands and thousands of entrepreneurs using Lovable to build whole businesses with payments, connecting Stripe for payments and making money on it. We're building towards being like an operating system almost, where the new generation of entrepreneurs build their AI-native businesses.” —— Anton Osika, Inside AI, 2025-05-21

## Anton 早早排除了训练模型这条路，把 bottleneck 定义成人和 AI 的 interface

这条访谈最重要的判断，是 Anton 明确说“训练自己的模型”不是 Lovable 的 bottleneck。AI 应用公司如果没有这层判断，很容易把精力浪费在 foundation model 竞赛里；Lovable 把焦点放在 human interface，利用模型能力快速上升的 wave，把模型输出变成普通人能使用的软件工作流。这个选择决定了组织配置：Lovable 要找的核心人不是 pretraining researcher，而是能理解用户、产品界面、软件工程和模型编排的工程型产品人才。

“The big unlock I saw is that the last few decades, trillions of dollars of value have been created by people creating software products, but less than one percent of the population can write code. I set out to build this new interface where you don't have to know how to write code. I don't know exactly what this interface will be; now it's chat, point and click, and more direct control, but it will evolve a lot.” —— Anton Osika, Inside AI, 2025-05-21

“Many people thought when I started, oh, you have to train your own models or compete in that space. It was clear to me: no, that's not going to be the bottleneck. The bottleneck is the interface towards the humans. That's what we've been focused on, and focusing on that is the biggest part of our success.” —— Anton Osika, Inside AI, 2025-05-21

## Lovable 的 scaling pain 很具体：每个 token 后面都有自己系统里的 cascade of events

Anton 讲增长挑战时没有泛泛说“流量大”，而是把 Lovable 的系统负载讲到 token 级别：5 万个新项目每天启动，每个项目几十到上百个用户请求，每个请求又有很多 streaming tokens，每个 token 在 Lovable 侧触发一串事件。这解释了为什么 Lovable 早期既是产品公司，也是基础设施公司。用户看到的是 prompt-to-app，组织内部要承受的是实时生成、文件系统、部署、版本、协作和外部服务依赖同时爆炸。

“The first and main growth beast has been the amount of traffic we have to serve while staying up. We have taken down many different services that we relied on and still had to switch them out quickly. One example was when GitHub had an incident and looked into it; it was because we were overloading their cluster. They disconnected us completely, Lovable went down, and we had to quickly scramble and make our own workaround where we did not rely on GitHub.” —— Anton Osika, Inside AI, 2025-05-21

“We have had to rewrite the entire system to handle it. For each token that the large language models output, there is a cascade of events happening on our side. We have 50,000 new projects being started every day; each has tens or sometimes hundreds of requests from the user, and each request has many small tokens streamed through our entire system.” —— Anton Osika, Inside AI, 2025-05-21

## Security 被 Lovable 当成产品责任，而不是用户自己 vibe coding 的后果

Anton 对 security 的口径非常值得留：他没有把非技术用户生成不安全应用的问题甩给用户，而是说 Lovable 要在合理范围内承担责任，并且已经做 security review。他判断未来 AI 会比人类 expert 更可靠，甚至“只有人类做 security reviewer”会不符合 best practice。这条线对企业化很重要，Lovable 要卖的是 controllable speed；如果不能把安全扫描、权限、部署治理接进产品，非技术团队 build 的能力会变成企业风险。

“People create insecure apps on Lovable, and then there is the question: is that our fault or their fault? We want to take as much responsibility as we reasonably can on the security side and add features to ensure users can see if they're introducing security vulnerabilities.” —— Anton Osika, Inside AI, 2025-05-21

“It can definitely be solved. I would like to say we solved 90% of the risks. Today, expert humans are more reliable to find security weaknesses than AI. I do not think that is going to be the case in the future. In the future, having a human as the only security reviewer is going to be disallowed by security best practices. You will need an AI.” —— Anton Osika, Inside AI, 2025-05-21

## Lovable 的 roadmap 从生成走向运营：让 AI 管完整产品生命周期

Anton 在 5 月已经把产品路线讲到很远：现在 Lovable 负责 implementation、deployment、hosting；未来要覆盖 design and validation、feedback、production operation、analytics、迭代决策和业务增长。这说明 Lovable 的目标不是把“写代码”做完，而是把一个软件产品持续演进的循环交给 AI 和团队共同处理。这个判断也解释它为什么会进入企业：企业最痛的不是做一个 demo，而是让 idea 经过验证后安全进入现有系统。

“If you want to build a software product business, you constantly evolve it and look at the next feature to build, make sure you get feedback on those features. There is the design and validation phase, then the implementation and deployment hosting phase, which we are doing now. Once you have something running in production with real users, it becomes more complex. The operation of the entire system as it is evolving is where we can add a lot more.” —— Anton Osika, Inside AI, 2025-05-21

“Building software is not our users' end goal. Their end goal is to build software products that are useful and that they have users for. Helping complete that circle in growing a business or growing a product, improving it over time together with AI and analytics, is what we're working towards.” —— Anton Osika, Inside AI, 2025-05-21

## Anton 给 web developer 的新定位，是把工程师从写代码的人改成现实问题到技术方案的翻译者

Anton 对开发者的回答很有组织意味：他没有讲“AI 替代 web developer”，而是重新定义 engineer 的 value。工程师应该把自己看成把现实问题翻译成技术解决方案的人，而不是会写某种代码的人。这个定义和 Lovable 的产品一致：代码生成会变得便宜，真正稀缺的是理解问题、判断架构、保证质量、连接业务约束。Lovable 越普及，工程师的工作越会往 system judgment 和 quality control 上移。

“As a developer or engineer, you should see yourself as someone translating problems in the real world to a technical solution. You shouldn't see yourself as someone who can write a certain piece of code. If you're a web developer, you're going to be much faster and more proficient using AI to solve technical problems. This is an opportunity for people who have the experience of being an engineer.” —— Anton Osika, Inside AI, 2025-05-21

## Europe 是 hard mode，但 Anton 想把破局本身变成差异化

Anton 对欧洲的讲法不是情绪化自豪。他承认 Europe 离资本、客户和成熟网络更远，是 hard mode；但如果能在这个环境下用极高 velocity 做出全球公司，反而会形成差异化叙事和人才磁场。Lovable 的 Stockholm 叙事不是外宣，它服务于招聘、社区、founder inspiration 和区域生态位：在欧洲成为 AI 应用层最强样本，本身能吸引那些想证明自己不必去硅谷的人。

“There are more difficulties building from Europe for sure. I see it as playing on hard mode in making a successful startup. But if you're able to break the norm in how to build a company and do it on the global stage with very high velocity, despite culture differences and being further away from deeper pockets on the customer side, then being differentiated and having broken that norm can be an advantage. That's what we're betting on.” —— Anton Osika, Inside AI, 2025-05-21
