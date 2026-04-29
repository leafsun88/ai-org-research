#!/bin/bash
# build-index.sh — 重建 Research Vault 全局索引
# 用法: bash scripts/build-index.sh
# 当索引文件与实际文件不同步时使用

VAULT_DIR="$(cd "$(dirname "$0")/../vault" && pwd)"
INDEX_FILE="$VAULT_DIR/_index.json"
COMPANIES_DIR="$VAULT_DIR/companies"

echo "Scanning vault at: $VAULT_DIR"

# Count companies and notes
company_count=0
total_notes=0
all_tags=""

for company_dir in "$COMPANIES_DIR"/*/; do
  [ -d "$company_dir" ] || continue
  company_count=$((company_count + 1))

  slug=$(basename "$company_dir")
  meta_file="$company_dir/meta.json"

  if [ -f "$meta_file" ]; then
    echo "  Found: $slug ($(cat "$meta_file" | grep '"name"' | head -1 | sed 's/.*: "//;s/".*//'))"
  else
    echo "  Found: $slug (no meta.json)"
  fi

  # Count markdown files (excluding profile.md)
  notes=$(find "$company_dir" -name "*.md" ! -name "profile.md" | wc -l | tr -d ' ')
  total_notes=$((total_notes + notes))
  echo "    Notes: $notes"
done

echo ""
echo "=== Vault Summary ==="
echo "Companies: $company_count"
echo "Total Notes: $total_notes"
echo ""
echo "Note: To fully rebuild _index.json, use vault-status skill in Claude."
