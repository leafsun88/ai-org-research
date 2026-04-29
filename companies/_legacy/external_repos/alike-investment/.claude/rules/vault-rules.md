---
paths:
  - "vault/**"
---
# Vault 数据规范

## 写入规则
- 每次写入vault文件后，必须同步更新 `vault/_index.json`
- 研究笔记文件名：`{YYYY-MM-DD}.md`，同一天同维度追加而非覆盖
- meta.json 必须包含：name, tickers, sector, tags, dimensions（数组）
- profile.md 是公司的"一句话定位 + 研究历史"，每次新增维度研究后更新

## S1-S5 标注
- 每条数据入库时必须标注信源置信度（S1-S5）
- 标注位置：研究笔记的 YAML frontmatter 或正文开头的 metadata block
- 缺失S标签的数据视为不完整，提醒用户补充

## 目录结构
- 9个维度目录必须按需创建，不要预创建空目录
- scoring/ 目录存放 signal-engine 输出（JSON格式）
- historical/ 存放 D1-D7 历史评分和事件时间线
- daily/ 存放每日自动crawl（`{YYYY-MM-DD}.json`）

## D1-D7 评分规范
- D1-D7评分标准的权威来源：`skills/winner-pattern-org/references/org_patterns.md`
- 评分必须先完成 Step 0（业务本质画像），从业务倒推理想组织形态
- Fit Score（组织-业务适配度）是独立评分，不纳入D1-D7加权
- 信息不足的维度必须标注 ⛔ 拒绝打分，不允许硬打分
- scoring/ 中的 JSON 数据应包含：D1-D7分数、Fit Score、A类核心机制、信息缺口

## 大文件分层读取（节省context）

vault中存在多种大文件，禁止直接Read全文。按以下策略分层读取：

| 文件类型 | 典型大小 | 读取策略 |
|---------|---------|---------|
| 10-K/10-Q filing | 100-150KB | 用Grep定位"MD&A"或"Risk Factors"段落，只Read命中区间（offset+limit） |
| _xbrl_facts.json | 500-950KB | 永远不全量加载。用Grep搜具体指标名（Revenue, NetIncome, EPS） |
| data_full_xbrl.md | 100-150KB | 同上，Grep搜指标 |
| data_price_history.md | 100KB+ | 只读最近1年：Read with offset跳过历史数据 |
| organization/ (68个人物文件) | 每个2-5KB | 先读_org_scan_report.md（汇总），只在需要穿透具体人时读individual文件 |
| discovery/_summary.json | 1KB | 优先读取——这是discovery/的路由缓存 |

**读取顺序原则**：summary → Grep定位 → Read(offset, limit) → 永远不Read全文

## 索引一致性
- `_index.json` 的 totalNotes 必须与实际文件数一致
- dimensions 数组必须反映实际存在的维度目录（有文件的才算）
- ticker 映射必须唯一，不允许重复
