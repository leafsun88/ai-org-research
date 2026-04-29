---
company: lovable
source_type: podcasts
type: source_note
status: done
source_path: companies/lovable/vault/podcasts/transcripts/2025-11-03_I-Ranked-Every-Vibe-Coding-App-Cursor-vs-Claude-Code-vs-Lova.md
source_title: "I Ranked Every Vibe Coding App (Cursor vs Claude Code vs Lovable)"
source_date: 2025-11-03
created_at: 2026-04-22
speaker: "The Startup Ideas Podcast hosts"
source_weight: B
relevance: high
quote_language: zh_translation_from_en_transcript
---

# I Ranked Every Vibe Coding App (Cursor vs Claude Code vs Lovable)

> 这是第三方用户/创业者视角的 ranking 讨论；本 note 只保留 Lovable 与 AI coding/app-builder 竞争心智相关证据，不把主观排名当成事实排名。

## AI coding tool 的团队信任会直接进入用户选择

讨论者把 Windsurf 降级，不是因为技术一定差，而是因为创始人离开、团队被收购后的信任破裂。这个外部视角对 Lovable 有用：AI coding/app-building 工具承接用户代码、产品进度和创业资产，用户不是只买一个功能，而是在押注背后的团队会继续维护、扩展和对齐用户利益。Lovable 的 founder-led brand、社区和不出售叙事，都会影响这种信任。

“Windsurf 我不会说技术上是 D tier，但因为团队发生的事情、创始人某种程度上离开，然后 Devin 把他们收走，这种情况下我相信技术可能还是好，但还剩多少信任？我认识 Windsurf 里的人，他们都很棒，但我大概再也不会用 Windsurf。用这些工具时，你是在信任构建这个工具背后的团队；如果一个 founder 就这样离开，这会给用户和投资人什么信心？所以很尊重地说，我会把 Windsurf 放到 D tier。” —— The Startup Ideas Podcast hosts, 2025-11-03

## Cursor/Windsurf 的默认客户仍是 developer，Lovable 的使用者定义更宽

访谈里提到 Cursor 团队明确说自己仍为 developers 构建，非技术用户使用很有趣但不会改变产品决策。这个证据帮助区分 Lovable 的战略位置：它不是 IDE 的低配版，而是 app builder/creation platform，默认服务 non-developer 和 semi-technical builder。产品选择会因此不同：Lovable 必须降低集成、后端、部署和安全的认知负担，而 Cursor 可以保留更高技术复杂度。

“如果你去问 Windsurf 或 Cursor 的团队，他们会告诉你，我们是在为开发者构建。他们的 focus 是 developers。我确实跟一个 Cursor 的人聊过，说现在很多非技术人也在用你们的工具，这会不会改变你们的构建方式、影响决策？他直接说不会，他们就是为 developers 构建；看到非开发者使用当然很酷，但主要人群还是 developers。从团队和业务角度看，这也说得通。” —— The Startup Ideas Podcast hosts, 2025-11-03

## Lovable 的用户痛点是 integration 和 backend，不是前端生成本身

讨论者对 Lovable/Bolt 的 pain point 识别很准：早期困难在 backend、注册、连接、复制 API keys 等 integration steps。对开发者这可能 trivial，对非技术人是 headache。Lovable 的价值就在于抽象掉这些步骤，让项目启动时自动拉取、连接、配置后端能力。这与 Anton 所说 opinionated stack 和 primitives 战略互相印证：非技术市场的瓶颈是系统拼装，不是单个页面生成。

“Lovable 和 Bolt 的痛点其实主要是 integrations。你需要一个后端，这很难；你得注册、连接、复制 API keys。对开发者来说这些都是小事，但对非开发者来说就是头痛。我的理解是，他们已经把这些东西抽象掉了。所以当你启动一个 Lovable project 时，我猜它会调用 API，把那些信息为你抓取并连接好，这让事情变得更容易。” —— The Startup Ideas Podcast hosts, 2025-11-03

## 用户心智里 Lovable 与 v0/Bolt 是 app-builder 桶，不是 IDE 桶

这期 ranking 的价值不在谁排 A 或 B，而在自然分类：Lovable、Bolt、v0 被放在 app builder/非技术友好工具组；Cursor、Claude Code、Codex、Windsurf 被放在更 technical coding side。这个心智边界对 Lovable 有双重含义：它能用 simplicity 吃到更大 non-coder 市场，但如果要赢 enterprise/professional workflow，也必须证明 app-builder 不等于 toy builder。

“你看 Lovable、v0、Bolt、Claude Code、Cursor、Codex、Windsurf 这些工具，我们会先把它们放在一张图上看技术性。Cursor 当然需要技术能力，打开它、fork repo、npm install、npm run，这些我都不指望非技术人直接会。Lovable、Bolt 和 v0 则是在更非技术友好的区域；如果我是一个 vibe coder、不懂代码，我可能会选 v0、Lovable、Bolt 这一类，而更技术的人还是会跑去 Claude Code、Codex、Cursor 这些工具做更深的工作。” —— The Startup Ideas Podcast hosts, 2025-11-03

## Lovable 牺牲一部分后端自由，换来非技术用户的可用性

主持人偏向 v0 的理由之一是 Vercel marketplace 和后端选择更多，而 Lovable 默认选择 Supabase 等更 opinionated 的路径。这个外部反馈说明 Lovable 的 trade-off 很清楚：技术用户会在自由度上挑剔，但非技术用户更需要默认答案。Lovable 未来如果上探 enterprise，需要在“默认简单”和“高级可替换”之间找到结构，而不是直接变成另一个 IDE。

“从工程视角看，如果我要做一个产品，也许 Lovable 能让我很快起一个漂亮页面。但 v0 有 Vercel marketplace，集成选择更多；比如 Lovable 会在某种程度上替你选好后端，像 Supabase，这有好处也有坏处，取决于你要做什么类型的 app。Vercel 和 v0 看起来会非常紧密地绑在一起，如果我要构建一个真的要给用户用的产品，这也是我愿意押的一个方向。” —— The Startup Ideas Podcast hosts, 2025-11-03

## 非技术用户真正需要的不是五个 prompt 成功，而是接受软件构建的迭代心态

结尾建议非常适合作为 Lovable 用户成功/教育的外部证据：很多非技术用户会在五到十个 prompts 后没做成就沮丧，但软件本来就需要 planning、testing、alpha、beta 和反复修正。Lovable 降低了进入门槛，但没有取消 taste、耐心、验收和迭代能力。Lovable 社区、教程、chat mode 和 ambassador 体系的长期价值，就在于训练这种 builder mindset。

“给非技术人的建议是，过去几个月这么多新工具出现后，必须有一个 mindset shift。很多人五个 prompts 没做成东西就很沮丧；但说实话，你凭什么觉得一个功能完整、有人会用、甚至会付钱的软件，五六个 prompts 就能做完？软件需要时间、需要规划、需要测试，有 alpha、有 beta，最后才有最终版本；软件也是一种艺术。感谢这些工具让非技术人也能构建东西，但我们也需要认真对待它。你的第一版没成功，Lovable 用坏了，那又怎样？换一个工具再试一次。很多非技术人没有意识到，真正做出东西是需要时间的。” —— The Startup Ideas Podcast hosts, 2025-11-03

## 选择工具也变成选择 founder 和公司，Anton 的 public presence 是 Lovable 的资产

讨论者最后建议用户去关注各家公司 founder，看自己信任谁、相信谁。这是很强的 category signal：在 AI coding/app-builder 赛道，产品还在快速变化，团队稳定性和 founder narrative 会影响 adoption。Anton 的 Twitter、访谈、欧洲 champion 叙事、长期不出售口径，都是 Lovable 在工具心智之外建立信任的方式。

“我最后给人的建议是，去关注这些公司的所有 founder：v0 的 Guillermo、Codex 的 Sam Altman、Lovable 的 Anton、Bolt 的 Eric Simmons、Replit 的 Amjad 等等。关注他们，然后看你相信谁。如果你真的和 Eric 有连接，或者真的和 Amjad、Sam Altman、Anton 有连接，那就选那个平台，因为你其实是在押一个人、押一家公司。这也是为什么押 Windsurf 的人最后被 Windsurf 了。” —— The Startup Ideas Podcast hosts, 2025-11-03
