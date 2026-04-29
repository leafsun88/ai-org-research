---
paths:
  - "scripts/discovery/**"
  - "vault/*/discovery/**"
---
# 数据采集规范

## 输出路径
- 所有采集数据写入 `vault/companies/{slug}/discovery/`
- slug = kebab-case公司名（从 `vault/_index.json` 的 `ticker_map` 查询）
- 新公司必须先在 `_index.json` 注册后再采集

## YAML Frontmatter（强制）
- 每个采集输出的 .md 文件必须包含 YAML frontmatter
- 必选字段：`ticker`, `type`, `credibility`, `evidence`
- 常见字段：`date`, `last_updated`, `data_source`, `url`, `title`
- type枚举参见 `vault/_schema/DATA_SCHEMA.md`

## 自动标签规则
- SEC filing → S5·E4
- XBRL数据 → S5·E4
- Earnings call transcript → S3·E3
- CEO Twitter/podcast → S3·E2
- 新闻报道（CNBC等） → S2·E2
- Reddit讨论 → S1·E1
- Perplexity AI研究 → S1-S2·E1-E2（需交叉验证）

## 禁止事项
- ❌ 禁止创建"仅URL+摘要"的文件——必须获取全文才保存
- ❌ 禁止缺少S/E标签的数据入库
- ❌ 禁止在discovery/目录外直接写入采集原始数据
