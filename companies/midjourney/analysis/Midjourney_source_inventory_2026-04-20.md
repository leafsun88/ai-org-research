---
company: Midjourney
research_key: MIDJOURNEY
type: source_inventory
date: 2026-04-20
status: first_pass_collection_with_source_notes
---

# Midjourney Source Inventory

## 当前状态

Midjourney 已按私有 AI 图像/视频生成公司处理，主目录为 `companies/midjourney/`。首轮采集完成了 target manifest dry-run、web seed fetch、podcast metadata、YouTube transcript，并补写了官方产品、careers、收入估算、法律风险和社媒的 source notes。

这轮最有价值的材料是 David Holz 的原声/访谈、官方 careers、官方 product updates、pricing / terms、Meta licensing 报道和 Hollywood lawsuits。收入、员工数、估值仍然全部按第三方估算处理。

## 落盘概览

| Channel | Vault 路径 | 当前产物 | 状态 |
|---|---|---:|---|
| official | `vault/official/` | status / URL index / source note | 官方页脚本未直接抓全文，已浏览器核验并补 source note |
| products | `vault/products/` | status / URL index / source note | V7 / V8 / V8.1 / V1 Video 已核验 |
| jobs_org | `vault/jobs/` | status / URL index / source note | careers 页已核验 |
| founder_voice | `vault/web/founder_voice/` | 2 篇完整访谈 | The Verge / VentureBeat 成功抓取 |
| web_longform | `vault/web/` | 2 篇访谈副本 + legal note | AP / court PDFs 等补为 source note |
| partnerships | `vault/partnerships/` | 1 篇 Meta licensing 报道 | Yahoo/Engadget 镜像成功抓取 |
| funding | `vault/funding/` | status / URL index / source note | Sacra / Contrary / ProductGrowth / Andrew 等估算源补 note |
| social | `vault/social/` | status / URL index / source note | Reddit / Discord 仅索引，未登录抓全文 |
| podcasts | `vault/podcasts/metadata/` | 76 条 metadata | 已生成 curated JSON |
| podcast transcripts | `vault/podcasts/transcripts/` | 1 条 David Holz transcript | ASR 子任务仍有失败与 running |
| youtube | `vault/youtube/` | 3 条 transcript，约 259k chars | 包含 2022 Discord office hours |

## 高价值已抓来源

| Source | 类型 | 路径 / URL | 可用性 | 研究价值 |
|---|---|---|---|---|
| The Verge David Holz interview | founder voice | `vault/web/founder_voice/unknown_ai-image-generation-art-midjourney-multiverse-interview-david-holz.md` | 全文 | 独立 research lab、10 人、无投资者、Discord/social imagination、engine for imagination |
| VentureBeat David Holz interview | founder voice | `vault/web/founder_voice/unknown_midjourney-founder-says-the-world-needs-more-imagination.md` | 全文 | IA/augmentation、consumer-first、拒绝 enterprise SaaS、reflection/coordination/imagination |
| Power Law: David Holz | podcast transcript | `vault/podcasts/transcripts/2023-06-20_David-Holz-Midjourney.md` | 全文 ASR | Leap Motion 背景、bootstrapped company、product before platform、Discord as learning interface |
| Discord office hours with David Holz | YouTube transcript | `vault/youtube/2026-04-20_Discord-Open-Office-Hours-with-MidJourney-Founder.md` | 全文字幕 | 小团队、weekly office hours、模型迭代、community feedback、moderation |
| Careers | official org | `vault/jobs/careers_source_note_2026-04-20.md` | source note | 官方组织语言：community-prioritized features、engineers/founder lead projects、small team |
| Product updates | official product | `vault/products/product_updates_source_note_2026-04-20.md` | source note | V7 default、V1 Video、V8/V8.1 alpha、rating/feedback loop |
| Plans / Terms | official business & policy | `vault/official/official_source_note_2026-04-20.md` | source note | pricing、commercial use gate、public/remix default、PG-13/community constraints |
| Meta licensing | partnership | `vault/partnerships/unknown_meta-licensing-midjourneys-ai-image-120012551html.md` | 全文 | Meta 许可 Midjourney aesthetic technology，说明“taste”可被外部大模型公司采购 |
| Sacra / Contrary / ProductGrowth / Andrew | third-party estimates | `vault/funding/funding_revenue_source_note_2026-04-20.md` | source note | 2023 ARR / 2025 revenue / employee count / no VC 等估算口径 |
| AP lawsuits | legal risk | `vault/web/legal_source_note_2026-04-20.md` | source note | Disney/Universal、Warner Bros. 诉讼与版权风险 |

## 采集结果与失败

- `collect_target.py MIDJOURNEY --dry-run`：通过，路径和 channels 正常。
- Web fetch 首轮：founder_voice 2/4 成功；web_longform 2/8 成功；enterprise_partnerships 1/3 成功；official/products/jobs/social/funding 多数仅 URL index。
- 失败主因：Perplexity API 401 导致 query expansion 不可用；Midjourney 官网/updates/docs/careers 部分页面需要浏览器渲染或反爬处理；Reddit / Discord 无登录与 API 权限。
- Podcast metadata：76 条，噪音较多，真正 founder / org 高价值只有少数。
- Podcast ASR：当前已有 David Holz 一条成功；两条失败为 `FILE_DOWNLOAD_FAILED`；一条德语播客仍 running；其余因本轮 max episode limit 延后。
- YouTube transcript：3 条成功，0 条失败；其中 office hours 内容很长但字幕文件行结构较差，后续引用时建议按关键词检索，不按行号细引。

## 下一步建议

- 优先把 David Holz / office hours 中关于“small team / Discord / user learning / moderation / model cadence / no investors”的原文拆成 quote bank。
- 社区体验需要单独抓 Reddit 高赞帖和 YouTube 评论，不应只靠搜索片段。
- 如果继续做投资报告，需要补：current employee count、Stripe global merchant 原始来源、Meta licensing 原始 X / Bloomberg、court docket 进展。
- ASR 没必要全量转完 76 条；Midjourney 的高价值音频集中在 founder 原声和 office hours，其余多为新闻复述或教程。
