#!/bin/bash
# Alike Investment — 新同事环境配置脚本
# 用法: git clone → cd 共创产品 → bash scripts/setup.sh
set -e

echo "=== Alike Investment 环境配置 ==="

# 1. 同步skills到~/.claude/skills/
echo "[1/4] 同步Skills到Claude Code..."
SKILLS_DIR="$HOME/.claude/skills"
mkdir -p "$SKILLS_DIR"

for skill_dir in skills/*/; do
  skill_name=$(basename "$skill_dir")
  target="$SKILLS_DIR/$skill_name"
  mkdir -p "$target"

  # 复制SKILL.md和references/
  if [ -f "$skill_dir/SKILL.md" ]; then
    cp "$skill_dir/SKILL.md" "$target/SKILL.md"
    # 复制references子目录（如果有）
    if [ -d "$skill_dir/references" ]; then
      mkdir -p "$target/references"
      cp -r "$skill_dir/references/"* "$target/references/" 2>/dev/null
    fi
    echo "  ✅ $skill_name"
  fi
done

# 2. 创建个人settings.local.json（如果不存在）
echo "[2/4] 检查个人配置..."
LOCAL_SETTINGS=".claude/settings.local.json"
if [ ! -f "$LOCAL_SETTINGS" ]; then
  cat > "$LOCAL_SETTINGS" << 'EOF'
{
  "permissions": {
    "allow": [
      "WebSearch",
      "Bash(python3 scripts/discovery/*.py *)",
      "Bash(bash skills/collect/generate-summary.sh *)"
    ]
  }
}
EOF
  echo "  ✅ 创建 $LOCAL_SETTINGS（请根据需要添加权限）"
else
  echo "  ⏭️ $LOCAL_SETTINGS 已存在，跳过"
fi

# 3. 安装Python依赖
echo "[3/4] 安装Python依赖..."
pip3 install yfinance requests dashscope 2>/dev/null && echo "  ✅ Python依赖安装完成" || echo "  ⚠️ pip3安装失败，请手动运行: pip3 install yfinance requests dashscope"

# 4. 验证
echo "[4/4] 验证环境..."
COMPANIES=$(find vault/companies -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')
SKILLS_COUNT=$(ls -d skills/*/SKILL.md 2>/dev/null | wc -l | tr -d ' ')
echo "  📊 Vault: $COMPANIES 家公司"
echo "  🔧 Skills: $SKILLS_COUNT 个"
echo ""
echo "=== 配置完成！==="
echo "可用命令："
echo "  npx serve product-demo -l 3456    # 启动前端"
echo "  /collect TICKER CompanyName        # 一键采集公司数据"
echo "  /pipeline CompanyName              # 一键研究流程"
echo "  /vault-status                      # 查看知识库状态"
