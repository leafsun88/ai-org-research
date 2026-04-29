---
paths:
  - "skills/**"
---
# Skill开发规范

## SKILL.md 结构
- frontmatter必须包含：name, description, allowed-tools
- description控制在250字符内，说清楚"什么时候用"和"什么���候不用"
- 有副作用的skill（写文件、发请求）必须设 `disable-model-invocation: true`

## 知识库模式（参考 winner-pattern-org）
- 复杂skill应拆分为 SKILL.md（框架+流程）+ references/（知识库+案例）
- SKILL.md保持框架精练，详细案例和标准放 references/ 子目录
- SKILL.md中用 `view references/xxx.md` 引用知识库
- 知识库文件可独立于skill被其他agent/skill引用

## Skill同步
- skills/ 目录是source of truth
- 修改skill后必须同步到 `~/.claude/skills/{skill-name}/SKILL.md`
- 同步命令：`cp skills/{name}/SKILL.md ~/.claude/skills/{name}/SKILL.md`

## 输出规范
- 研究类skill输出必须包含：信源列表 + S1-S5标注 + 核心发现
- 输出格式统一为Markdown，结构化数据用JSON code block
- 所有skill完成后提示用户 /vault-save
