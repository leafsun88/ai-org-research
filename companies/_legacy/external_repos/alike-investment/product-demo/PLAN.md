# Cowork 重构计划

## 核心理念
Cowork = 一条连续的人机对话时间线（per research），自动识别三种模式，所有 Status 中的点击都导航到 Cowork 并展示对应上下文。

## 数据模型

### 统一时间线 `coworkTimeline[researchId]`
替换 `coworkHistory` + `coworkSessions`，合并为一条流：
```js
coworkTimeline[researchId] = [
  { id, ts, type: 'chat'|'signal'|'kq', role: 'user'|'ai'|'agent', ... },
  ...
]
```

每条消息的类型：
- `{ type:'chat', role:'user', text }` — 用户自由对话
- `{ type:'chat', role:'ai', text, sources:[] }` — AI回答（含出处）
- `{ type:'signal', role:'ai', signalId, summary }` — AI提出的signal小卡片
- `{ type:'signal-expand', signalId }` — 用户点击展开的signal大卡片（内含agents debate、evidence等）
- `{ type:'kq', role:'ai', kqId, summary }` — Key Question小卡片
- `{ type:'kq-expand', kqId }` — 用户点击展开的KQ大卡片

### 展开的"大卡片"
大卡片不离开Cowork，而是在timeline中inline展开为一个大区域，包含：
- Signal：信号描述 + 维度影响 + confidence + agents debate + evidence列表 + 可继续追问
- KQ：问题 + evolving answer + sources + 可继续追问

## 渲染逻辑

### `renderCoworkTab()`
1. 渲染完整 timeline（最新N条，老的折叠为"Load earlier"）
2. 如果有 `expandedItem`（signal/kq），渲染大卡片
3. 底部输入框永远可用
4. 无 mode bar（自动检测模式）

### 模式自动检测 `detectCoworkMode(text)`
- `/signal` 或 关键信号词 → signal mode → 走 human-proposal 流程
- `/kq` 或 关键问题词 → kq mode → 走 human-question 流程
- 其他 → chat mode → 基于私域/公开信息回答

### Status → Cowork 导航
- 点击 Signal 卡片 → `expandSignalInCowork(signalId)` → 切到Cowork，滚动到该signal，展开大卡片
- 点击 KQ 卡片 → `expandKQInCowork(kqId)` → 切到Cowork，滚动到该KQ，展开大卡片
- 点击 "+" → `startHumanProposal/startHumanQuestion` → 切到Cowork，AI提问话术

## 实施步骤

### Step 1: 替换数据模型
- 删除 `coworkSessions`, `activeCoworkSession`, `coworkContext`
- 新增 `coworkTimeline = {}`
- 新增 `expandedCoworkItem = null` // { type: 'signal'|'kq', id }

### Step 2: 重写 renderCoworkTab
- 渲染 timeline，每条消息根据 type 不同UI
- signal/kq 作为小卡片渲染，点击展开
- 展开后为大卡片（全部agent debate + evidence + confidence）
- 删除 mode bar（Chat/Divergent/Convergent）

### Step 3: 重写 handleCoworkSend
- 自动检测模式
- chat → 生成AI回答（含sources）
- signal相关 → 走signal pipeline
- kq相关 → 走KQ pipeline

### Step 4: Status → Cowork 连接
- 所有 Status 中的点击事件导航到 Cowork + 展开对应item
- "+" 按钮导航到 Cowork + AI话术

### Step 5: 历史折叠
- 只显示最近N条
- 老消息折叠为"Load earlier"
- 大卡片可以收起回小卡片
