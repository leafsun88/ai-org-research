---
name: org-scan
description: 组织架构穿透 — 多Agent并行搜索公司C-Suite到VP级别高管的职业经历
argument-hint: TICKER "CompanyName"
---

## 路径约定（Alike Investment集成）

本skill的输出路径已适配Alike Investment的vault结构：
- 输出根目录：`vault/companies/{slug}/discovery/`（不再是 `discovery_database/{TICKER}/`）
- slug = kebab-case公司名（如 applovin, duolingo, pop-mart）
- TICKER→slug映射：查询 `vault/_index.json` 的 `tickerMap` 字段
- 如果_index.json中没有该TICKER，创建新目录并更新_index.json

所有输出路径中的 `discovery_database/{TICKER}/` 或 `{TICKER}/` 替换为 `vault/companies/{slug}/discovery/`。
例如：`APP/sources/youtube/` → `vault/companies/applovin/discovery/sources/youtube/`

所有采集数据的YAML frontmatter必须包含 `credibility: S?` 和 `evidence: E?` 字段。

# /org-scan — 组织架构穿透

对指定公司进行组织穿透，覆盖C-level到VP级别。Orchestrator获取名单→并行Agent逐人穿透。

## 参数
$ARGUMENTS: `TICKER "CompanyName"`

## 信源置信度标签

| 来源 | S标签 | E标签 |
|------|-------|-------|
| SEC DEF 14A | S5 | E4 |
| 公司IR页面 | S4 | E3 |
| LinkedIn (WebSearch) | S4 | E2 |
| Crunchbase | S4 | E2 |
| 新闻报道 | S2 | E2 |

## Phase 1: Orchestrator — 获取高管名单

1. SEC EDGAR获取最新DEF 14A → 解析高管名单+简历
2. WebSearch `site:{company_website}/leadership` → 补充VP级别
3. 输出 `vault/companies/{slug}/discovery/organization/overview/org_structure.md` [S5·E4]

名单包含: C-Suite + SVP/VP + 董事会 + 近2年离职关键高管

## Phase 2: 并行Agent穿透

每人启动一个Agent（每批最多5个并行）。每个Agent执行4步搜索:

**Step 1: 身份+职业轨迹** [S4·E2]
- `"{name}" "{company}" biography career`
- `"{name}" site:linkedin.com`
- 提取: 教育、完整履历、LinkedIn URL

**Step 2: 当前公司角色** [S3-S5·E2-E4]
- `"{name}" "{company}" role responsibility`
- 提取: 负责什么、关键项目

**Step 3: 人脉网络** [S4·E2]
- `"{name}" board advisor investor`
- 提取: 过往共事关系、外部董事席位

**Step 4: 争议/负面** [S2-S5·E2-E4]
- `"{name}" lawsuit SEC controversy`
- 提取: 诉讼、负面报道

### 输出

每人一个文件，按级别分文件夹:
```
vault/companies/{slug}/discovery/organization/
├── c_suite/{name}.md
├── vp_level/{name}.md
├── board/{name}.md
└── departed/{name}.md
```

YAML frontmatter含 `credibility` 和 `evidence` 字段。保留原始搜索结果原文。

## Phase 3: 汇总

生成 `vault/companies/{slug}/discovery/organization/_org_scan_report.md`:
- 组织架构结构讲述（文字描述汇报关系）
- 关键发现（团队稳定性、人才来源、异常信号）
