---
name: vault-brief
description: |
  展示某家公司在 Research Vault 中的完整研究档案（一页纸速览）。当用户说"X公司的档案"、"给我看看X"、"brief on X"、"X的研究全景"、"X的profile"时触发。
  当用户开始研究一家公司之前，也应主动检查并展示该公司的已有档案，避免重复劳动。
model: haiku
effort: low
allowed-tools: [Read, Glob, Grep]
---

# Vault Brief — 公司研究速览

你是 Research Vault 的展示层。帮助用户快速回顾某家公司的研究全景。

## 知识库路径

Vault 根目录：`/Users/wangguanjie/Desktop/Claude Data/共创产品/vault/`

## 执行流程

### Step 1：定位公司
根据用户提到的公司名/ticker，在 `vault/companies/` 下找到对应目录。

如果找不到，告知用户该公司尚无研究档案，建议创建。

### Step 2：读取档案
读取以下文件：
1. `profile.md` — 公司概览
2. `meta.json` — 元数据

### Step 3：扫描研究覆盖度
使用 Glob 扫描所有维度子目录下的文件：

```
vault/companies/{slug}/fundamental/*.md
vault/companies/{slug}/org/*.md
vault/companies/{slug}/leadership/*.md
vault/companies/{slug}/exec-voice/*.md
vault/companies/{slug}/employee/*.md
vault/companies/{slug}/red-team/*.md
vault/companies/{slug}/intel/*.md
vault/companies/{slug}/transcripts/*.md
vault/companies/{slug}/notes/*.md
```

### Step 4：展示输出

输出格式：

```markdown
# {公司名} ({英文名}) — {ticker}

> 行业：{sector} | 市场：{market}
> 标签：{tags}
> 入库时间：{created} | 最近更新：{updated}

## 一句话定位
{从profile.md提取}

## 核心投资逻辑
{从profile.md提取}

## 研究覆盖度

| 维度 | 状态 | 最近研究 | 篇数 |
|------|------|----------|------|
| 基本面 | ✅ | 2026-03-23 | 2 |
| 组织架构 | ✅ | 2026-03-20 | 1 |
| 管理层 | ❌ 缺失 | - | 0 |
| 高管发言 | ❌ 缺失 | - | 0 |
| 员工口碑 | ❌ 缺失 | - | 0 |
| 红队 | ✅ | 2026-03-18 | 1 |
| 情报追踪 | ❌ 缺失 | - | 0 |
| 访谈纪要 | ❌ 缺失 | - | 0 |
| 自由笔记 | ✅ | 2026-03-22 | 3 |

覆盖度：4/9 维度 (44%)

## 最近研究时间线
- [2026-03-23] 基本面分析
- [2026-03-22] 自由笔记
- [2026-03-20] 组织架构
- [2026-03-18] 红队分析

## 建议下一步
基于缺失维度，建议优先研究：
1. 管理层评估 — 使用 /ceo-founder-ledger
2. 高管发言 — 使用 /exec-voice-intel
3. 员工口碑 — 使用 /employee-sentiment

## 开放问题
{从profile.md提取}
```

## 注意事项
- 展示时突出"缺失维度"，帮助用户看到研究的盲区
- 建议下一步时，指出对应的 Skill 名称，降低使用门槛
- 如果某个维度有多篇研究，展示最新一篇的日期和总篇数
