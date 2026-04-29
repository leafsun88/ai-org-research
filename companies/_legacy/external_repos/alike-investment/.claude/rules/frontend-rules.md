---
paths:
  - "product-demo/**"
  - "dashboard/**"
---
# 前端开发规范

## 架构约束
- product-demo 是单文件SPA（index.html），所有代码在一个文件内
- 零外部依赖，不使用 npm/webpack/任何构建工具
- dashboard 使用 npx serve 静态服务 + Python API后端

## UI规范
- 按钮必须小巧，禁止大面积按钮
- 信息密度优先，避免留白浪费
- 深色主题为默认
- 中文UI，技术术语可保留英文

## Status vs Cowork
- Status面板：只读展示AI结论，不接受用户输入
- Cowork面板：交互式工作台，支持Chat/Signal/KQ三种模式
- Cowork中的任何数据变更必须双写：Timeline（展示层）+ COMPANY_STATUS/DELTA_PROPOSALS（数据层）

## 去重规则
- 新增KQ/Signal前按语义相似度比对现有数据
- 重复项合并而非新建，保留所有来源标记（AI/Human/Both）
