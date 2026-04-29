---
company: 群核科技
research_key: QUNHE
type: source_inventory
date: 2026-04-18
status: first_pass_public_collection
---

# 群核科技 Source Inventory

## 当前结论

本轮已为群核科技建立公司级目录，并收集到港交所招股书、配发结果、展示文件页面、会计师报告、经审计合并财务报表、未经审计备考财务资料、弗若斯特沙利文行业报告、官方站点页面、IPO 官方新闻稿和若干媒体原文 HTML。当前 vault 约 27MB，核心材料以港交所监管披露为主。

需要特别注意：群核科技 2026-04-17 才在港交所上市，当前没有上市后完整年度报告。招股书明确披露，公司不会另行编制并寄发截至 2025-12-31 年度的年度报告，因为相关年度财务资料已经包含在招股书内，并将于 2026-04-30 前发布相关公告。因此本轮“年报”口径应写成：`2025 年度财务资料 = 招股书 + 会计师报告 + 经审计合并财务报表`，后续再追正式公告。

## 目录状态

- `companies/qunhe/vault/regulatory/`：港交所上市文件、招股书、配发结果、行业报告、展示文件页面。
- `companies/qunhe/vault/financials/`：会计师报告、经审计合并财务报表、未经审计备考财务资料。
- `companies/qunhe/vault/official/`：Manycore / Kujiale / Coohom / Coohom Blog / PRNewswire 官方或准官方页面。
- `companies/qunhe/vault/web/`：上市与 IPO 相关媒体页面原始 HTML。
- `companies/qunhe/vault/jobs/`：招聘 URL index 与抓取失败状态。
- `companies/qunhe/vault/funding/`：融资/股东 query 状态，目前 Perplexity quota 阻塞，融资信息主要来自招股书。

## 高价值监管材料

| 文件 | 本地路径 | 来源 URL | 用途 |
| --- | --- | --- | --- |
| English Prospectus | `companies/qunhe/vault/regulatory/20260409_manycore_global_offering_prospectus_en.pdf` | https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0409/2026040900025.pdf | 英文招股书，适合英文名、投资者、全球发售口径 |
| Chinese Prospectus | `companies/qunhe/vault/regulatory/20260409_manycore_global_offering_prospectus_zh.pdf` | https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0409/2026040900026_c.pdf | 中文招股书，事实主源 |
| Prospectus TXT | `companies/qunhe/vault/regulatory/20260409_manycore_global_offering_prospectus_zh.txt` | 本地由中文招股书转换 | 后续检索和引用主文件 |
| Allotment Results | `companies/qunhe/vault/regulatory/20260416_manycore_allotment_results_zh.pdf` | https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0416/2026041601685_c.pdf | 发售价、认购倍数、股份代码、募资额 |
| Listing Documents Page | `companies/qunhe/vault/regulatory/20260409_hkex_listing_documents_page_zh.html` | https://www.hkexnews.hk/listedco/listconews/sehk/2026/0409/2026040900077_c.htm | 展示文件入口，列明会计师报告、财报、行业报告等附件 |
| Frost & Sullivan Industry Report | `companies/qunhe/vault/regulatory/20260409_manycore_frost_sullivan_industry_report_zh.pdf` | https://www.hkexnews.hk/listedco/listconews/sehk/2026/0409/12098824/2026040900099_c.pdf | 行业规模、竞争格局、市场份额 |

## 财务与年报替代材料

| 文件 | 本地路径 | 来源 URL | 用途 |
| --- | --- | --- | --- |
| Accountants' Report | `companies/qunhe/vault/financials/20260409_manycore_accountants_report_zh.pdf` | https://www.hkexnews.hk/listedco/listconews/sehk/2026/0409/12098824/2026040900096_c.pdf | 会计师报告 |
| Audited Consolidated Financial Statements | `companies/qunhe/vault/financials/20260409_manycore_audited_consolidated_financial_statements_zh.pdf` | https://www.hkexnews.hk/listedco/listconews/sehk/2026/0409/12098824/2026040900097_c.pdf | 经审计合并财务报表 |
| Unaudited Pro Forma Financial Info | `companies/qunhe/vault/financials/20260409_manycore_unaudited_pro_forma_financial_info_zh.pdf` | https://www.hkexnews.hk/listedco/listconews/sehk/2026/0409/12098824/2026040900098_c.pdf | 上市后备考财务资料 |

## 官方与产品材料

| 文件 | 本地路径 | 来源 URL |
| --- | --- | --- |
| Manycore 官网首页 HTML | `companies/qunhe/vault/official/manycoretech_home.html` | https://www.manycoretech.com/ |
| 酷家乐官网首页 HTML | `companies/qunhe/vault/official/kujiale_home.html` | https://www.kujiale.com/ |
| Coohom 官网首页 HTML | `companies/qunhe/vault/official/coohom_home.html` | https://www.coohom.com/ |
| Coohom Blog 抓取文本 | `companies/qunhe/vault/official/unknown_blogcoohomcom.md` | https://blog.coohom.com/ |
| PRNewswire IPO 官方新闻稿 HTML | `companies/qunhe/vault/official/20260417_prnewswire_manycore_hkex.html` | https://www.prnewswire.com/news-releases/manycore-tech-debuts-on-hkex-as-the-worlds-first-spatial-intelligence-company-302745593.html |

## 媒体与补充材料

| 文件 | 本地路径 | 来源 URL |
| --- | --- | --- |
| 新浪科技上市报道 HTML | `companies/qunhe/vault/web/20260417_sina_manycore_listing.html` | https://finance.sina.com.cn/tech/2026-04-17/doc-inhuupte2249457.shtml |
| 经济观察网上市报道 HTML | `companies/qunhe/vault/web/20260417_eeo_manycore_listing.html` | https://www.eeo.com.cn/2026/0417/841813.shtml |
| 杭州网/杭州日报报道 HTML | `companies/qunhe/vault/web/20260417_hangzhou_manycore_listing.html` | https://ori.hangzhou.com.cn/ornews/content/2026-04/17/content_9208000.htm |
| 每经网 IPO 报道 HTML | `companies/qunhe/vault/web/20260409_nbd_manycore_ipo.html` | https://www.nbd.com.cn/articles/2026-04-09/4330797.html |

## 当前抓取缺口

- Perplexity API 当前返回 `insufficient_quota`，query 扩展发现受阻；本轮已保留 `_collection_status.json` 和 `_url_index.json`。
- 官网和部分中文媒体页由通用 fetcher 判断为内容过短，但已用 `curl` 保存原始 HTML；后续如要做全文清洗，可另写 HTML parser。
- 招聘页 `https://www.kujiale.com/about/jobs` 返回 404，需要后续改用 Boss 直聘、猎聘、官网新路径或企业招聘公众号补。
- 尚未跑 YouTube / 播客；群核属于上市软件公司，第一优先级暂时应是招股书、财报、产品文档、创始人访谈和客户案例。
