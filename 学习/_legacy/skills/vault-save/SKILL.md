---
name: vault-save
description: |
  将投研成果保存到 Research Vault 知识库。当用户说"保存到知识库"、"存一下"、"save to vault"、"归档"、"存档"时触发。
  也应在用户完成一次投研Skill调用（如stock-fundamental-analyst、company-intelligence-tracker、org-x-ray、the-org、ceo-founder-ledger、red-team、exec-voice-intel、employee-sentiment等）后主动提示用户是否要保存。
  即使用户只说"存一下这个"或"把刚才的研究保存了"也应触发此skill。
model: sonnet
effort: medium
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash]
---

# Vault Save — 保存研究到知识库

你是 Research Vault 的存储引擎。你的任务是将当前对话中的投研成果，结构化地保存到知识库。

## 知识库路径

Vault 根目录：`/Users/wangguanjie/Desktop/Claude Data/共创产品/vault/`

## 执行流程

### Step 1：识别内容
从当前对话上下文中识别：
- **公司名称**（中文+英文）和 **ticker**
- **研究维度**：对应以下子目录之一：
  - `fundamental` — 基本面分析（来自 stock-fundamental-analyst）
  - `org` — 组织架构（来自 the-org）
  - `leadership` — CEO/创始人评估（来自 ceo-founder-ledger、org-x-ray）
  - `exec-voice` — 高管发言（来自 exec-voice-intel）
  - `employee` — 员工口碑（来自 employee-sentiment）
  - `red-team` — 红队/Bear Case（来自 red-team）
  - `intel` — 情报追踪（来自 company-intelligence-tracker）
  - `transcripts` — 访谈/视频纪要（来自 expert-transcript、video-transcript、meeting-notes-organizer）
  - `notes` — 自由笔记（用户手写或其他来源）
- **内容摘要**：提取核心发现的简要总结

如果无法自动识别，向用户确认公司和维度。

### Step 2：生成 slug
将公司名转为 kebab-case slug（如 `tencent`、`bytedance`、`google`、`pinduoduo`）。

### Step 3：创建/更新公司目录
检查 `vault/companies/{slug}/` 是否存在：

**如果是新公司**（目录不存在）：
1. 创建目录：`vault/companies/{slug}/`
2. 创建所有子目录：`fundamental/`、`org/`、`leadership/`、`exec-voice/`、`employee/`、`red-team/`、`intel/`、`transcripts/`、`notes/`
3. 创建 `meta.json`：
```json
{
  "name": "公司中文名",
  "name_en": "English Name",
  "slug": "slug",
  "tickers": ["TICKER"],
  "sector": "行业",
  "market": "US/HK/A",
  "tags": [],
  "watchlist": false,
  "created": "YYYY-MM-DD",
  "updated": "YYYY-MM-DD",
  "research_count": 0,
  "dimensions_covered": []
}
```
4. 创建初始 `profile.md`（参考模板 `vault/_templates/company-profile.md`，填入已知信息）

**如果公司已存在**：直接进入下一步。

### Step 4：保存研究笔记
将研究内容保存为 `vault/companies/{slug}/{dimension}/{YYYY-MM-DD}.md`

如果同一天同一维度已有文件，使用 `{YYYY-MM-DD}-v2.md`、`{YYYY-MM-DD}-v3.md` 等。

文件格式：
```markdown
# {公司名} — {维度中文名} 研究笔记

> 日期：{YYYY-MM-DD}
> 维度：{维度}
> 来源：{触发的Skill名称或"手动笔记"}

## 核心发现
{从对话中提取的核心内容}

## 关键数据
{如有定量数据}

## 值得追踪的信号
{值得持续关注的点}

---
*由 {skill名} 生成，存储于 Research Vault*
```

重要：保存的内容应是研究成果的**完整版本**，不要过度压缩。这是知识库的一手材料。

### Step 5：更新元数据
1. 更新 `meta.json`：
   - `updated` → 今天日期
   - `research_count` += 1
   - `dimensions_covered` 中添加新维度（如果之前没有）
   - 根据研究内容补充 `tags`

2. 更新 `profile.md` 的"最近研究"部分：
   - 在最近研究列表顶部添加一行：`- [{YYYY-MM-DD}] {维度中文名} → {dimension}/{filename}`

3. 更新 `vault/_index.json`：
   - 更新或添加该公司条目
   - 更新 `stats.total_companies` 和 `stats.total_notes`
   - 更新全局 `tags` 列表
   - 更新 `updated` 时间戳

### Step 6：确认
向用户报告：
- 保存路径
- 更新了哪些文件
- 该公司当前的研究覆盖度（哪些维度有了，哪些还缺）

## 注意事项
- 始终使用 UTF-8 编码
- 日期格式统一为 YYYY-MM-DD
- slug 统一用小写 kebab-case
- 保存时不要丢失研究内容的细节——知识库存的是完整研究，不是摘要
