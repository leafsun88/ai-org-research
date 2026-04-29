---
company: Midjourney
research_key: MIDJOURNEY
type: manual_substack_search_report
date: 2026-04-21
status: current
---

# Midjourney Manual Substack Search 2026-04-21

## 脚本状态

`fetch_web_sources.py --target MIDJOURNEY --channels substack --max-queries 6` 已跑通，但当前环境缺 `PERPLEXITY_API_KEY / PPLX_API_KEY`，所以脚本没有拿到 Substack URL。

本轮已修复 manifest：`config/company_targets.json` 现在有 Midjourney 专属 `channels.substack.queries`，下次补上 Perplexity key 后可直接复跑。

## 高价值候选

### ProductGrowth: How Midjourney Hit $500M ARR With Zero VC and Zero Marketing

- URL: https://www.productgrowth.blog/p/how-midjourney-hit-500m-arr
- Type: Substack-like newsletter / growth analysis
- Relevance: high
- Why keep: 这篇把 Midjourney 拆成 bootstrapped、no free tier、小团队、Discord 到 web app 迁移、Meta licensing、资本效率几个模块，和我们要写的商业模式 / 组织效率 / GTM 很贴。
- 注意：文中 $500M ARR、107 employees、Meta licensing 等数字需和其他来源交叉验证，不单独当事实。

### Wokescreen / CrowdSource: The rise of AI art / Midjourney CEO's AI art theft

- Search result URL: https://rumble.com/v2i0f9j-clip-midjourney-ceo-confesses-to-using-artists-work-for-ai-generated-images.html
- Linked Substack: https://wokescreen.substack.com/p/the-rise-of-ai-art-what-it-means
- Type: creator-rights / copyright critique
- Relevance: medium
- Why keep: 适合做版权争议和艺术家视角的反方材料。它不是组织/商业模式核心材料，但可以帮助分析 Midjourney 的长期 regulatory / reputation risk。

### Centennial World / Infinite Scroll

- URL: https://music.amazon.in/podcasts/9a8ad0f1-70af-43eb-8135-fa39efa0309d/episodes/9ce8bcb8-37f2-46f6-b0a6-5d0aa838a32d/infinite-scroll-mini-tech-scroll-roblox-protests-disney-x-midjourney-lawsuit-moshi-monsters-kickstarter-tinder-trust-safety-interview
- Linked Substack: https://centennialworld.substack.com/
- Type: social media / tech culture newsletter + podcast
- Relevance: low-medium
- Why keep: 只在 Disney / Universal lawsuit 时间线上有用；深度不足，不建议做 essence。

### Leveling Up: The future of business is 90% cheaper and 10x faster

- URL: https://newsletter.levelingup.com/p/the-future-of-business-is-90-cheaper-and-10x-faster-2f86
- Type: business newsletter
- Relevance: low-medium
- Why keep: 把 Midjourney 放进“AI 小团队高收入”的横向叙事，但对 Midjourney 本身没有足够一手细节。

## 不是 Substack 但应纳入 web/founder voice 的材料

### Forbes: Midjourney Founder David Holz On The Impact Of AI On Art, Imagination And The Creative Economy

- URL: https://www.forbes.com/sites/robsalkowitz/2022/09/16/midjourney-founder-david-holz-on-the-impact-of-ai-on-art-imagination-and-the-creative-economy/
- Type: founder interview
- Relevance: high
- Why keep: David Holz 对 mission、professional users、commercial license、dataset、artist opt-out、cost-cutting vs ambition expansion 的原声都在这里。它不是 Substack，但价值高于大多数 Substack 二手文。

### Stratechery: An Interview with Midjourney Founder David Holz

- URL: https://stratechery.com/2022/an-interview-with-midjourney-founder-david-holz-about-generative-ai-vr-and-silicon-valley/
- Type: founder interview / paid
- Relevance: high
- Why keep: 付费墙后高价值 founder interview。当前只作为 URL index，不写成已获取全文。

## 当前判断

Midjourney 的 Substack 高价值材料不多。真正值得进入分析的是 ProductGrowth 这类商业模式拆解，以及 Wokescreen 这类版权反方材料；但 founder voice 的主战场仍然是 iHeart / Forbes / Stratechery / Discord office hours，不在 Substack。
