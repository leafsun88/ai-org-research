---
company: Midjourney
research_key: MIDJOURNEY
type: podcast_additional_search_report
date: 2026-04-21
status: current
---

# Midjourney Additional Podcast Search 2026-04-21

## 本轮动作

- 按 `config/company_targets.json` 增补 podcast query：`How Computers Dream David Holz`、`What Future David Holz Midjourney`、`Stratechery David Holz Midjourney interview`、`bootstrapped no VC`、`Discord community`、`aesthetic technology` 等。
- 执行 `python3 scripts/discovery/fetch_podcasts.py --target MIDJOURNEY --min-duration-min 10`。
- 新 staging curated episode 数：104；原 vault curated episode 数：76；按 title 粗去重新增 38 条。
- 已同步 metadata 到 `companies/midjourney/vault/podcasts/metadata/`。
- 已转录新增最高价值 founder 原声：`How Computers Dream with David Holz`。

## 新增最高价值材料

### How Computers Dream with David Holz

- Source: iHeart / What Future with Joshua Topolsky
- Date: 2022-11-10
- Duration: 58 min
- URL: https://www.iheart.com/podcast/1119-what-future-with-joshua-t-103516818/episode/how-computers-dream-with-david-holz-104410959/
- Local transcript: `companies/midjourney/vault/podcasts/transcripts/2022-11-10_How-Computers-Dream-with-David-Holz.md`
- Value: David Holz founder 原声长访谈。它比已有 Power Law 二手叙事更适合回答 founder worldview、Midjourney 为什么先走 Discord/community、AI art 与 imagination 的边界、版权争议和产品哲学。
- Transcription path: Groq URL 失败，原因是媒体 URL 302；DashScope URL fallback 成功，输出 80,111 chars。

### How Computers Dream with David Holz [Rerelease]

- Source: iHeart / What Future with Joshua Topolsky
- Date: 2023-08-03
- Duration: 56.2 min
- URL: Apple Podcasts metadata
- Value: 与 2022-11-10 原版高度重复，本轮不重复转录。

### Stratechery interview with David Holz

- Source: Stratechery / Ben Thompson
- Date: 2022-08-02
- URL: https://stratechery.com/2022/an-interview-with-midjourney-founder-david-holz-about-generative-ai-vr-and-silicon-valley/
- Value: 高价值 founder interview index。当前页面为 Stratechery 会员内容，不假装已拿到全文；已有一条 Stable Discussion 播客转述了其中关于用户年龄层、词汇量和多产品形态的片段。

## 其他新增方向

- Civitai creator community：`The TED AI Show: Building an AI creator community...`，不是 Midjourney 材料，但适合横向理解 AI creator community / marketplace。
- Midjourney video model news：多条 2025-06-19/20 news roundup，只适合作为产品时间线，不适合做深度 essence。
- Midjourney revenue/no VC：新增 metadata 多为二手估算或泛 AI 小团队案例，后续应优先和 ProductGrowth / official / web source 交叉验证。
- Midjourney Discord community：新增少数 community-led growth 相关 episode，可选做横向材料；优先级低于 David Holz 原声和 Discord office hours。

## 当前判断

本轮真正需要进入下一步 essence 的新增 podcast 只有一条：`How Computers Dream with David Holz`。其他新增 37 条里，大部分是 news roundup、教程、泛 AI 小团队案例或重复 rerun；可以保留 metadata，但不急着转录或 essence。
