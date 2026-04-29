#!/bin/bash
# team-init.sh — 一键初始化投研团队协作
# 用法: cd 共创产品 && bash scripts/team-init.sh

set -e

echo "=== 投研团队协作初始化 ==="

# 1. Git init
if [ -d .git ]; then
  echo "[跳过] 已是 Git 仓库"
else
  git init
  echo "[完成] Git 仓库初始化"
fi

# 2. .gitignore
if [ ! -f .gitignore ]; then
  cat > .gitignore << 'EOF'
# 个人配置不入库
.claude/
*.local
.DS_Store
node_modules/

# 编辑器
.vscode/
.idea/
*.swp
*.swo

# 系统
Thumbs.db
.Spotlight-V100
.Trashes
EOF
  echo "[完成] .gitignore 创建"
else
  echo "[跳过] .gitignore 已存在"
fi

# 3. .team/ 目录
if [ ! -d .team ]; then
  mkdir -p .team/reviews
  echo "[完成] .team/ 目录创建"
else
  echo "[跳过] .team/ 已存在"
fi

# 4. 首次 commit
git add vault/ dashboard/ .team/ skills/ scripts/ .gitignore 2>/dev/null || true
git commit -m "init: 投研知识库团队协作初始化

- vault/: 研究知识库 (3家公司, 47+篇笔记)
- dashboard/: 可视化仪表盘
- .team/: 团队协作配置
- skills/: 投研技能定义
- scripts/: 工具脚本" 2>/dev/null || echo "[跳过] 无新文件需要提交"

echo ""
echo "=== 初始化完成 ==="
echo ""
echo "下一步："
echo "  1. 编辑 .team/config.json 添加团队成员"
echo "  2. 连接远程仓库: git remote add origin <url>"
echo "  3. 推送: git push -u origin main"
echo "  4. 团队成员克隆: git clone <url>"
echo ""
echo "使用 /team status 查看团队状态"
