#!/bin/bash
# ============================================================
# import-discovery-db.sh
# Discovery Database → Alike Vault 导入脚本
#
# 用法: ./scripts/import-discovery-db.sh /path/to/discovery_database
#
# 将同事的discovery_database数据导入到vault/companies/目录
# 不覆盖已有的Alike特有文件（scoring/artifacts/historical）
# ============================================================

set -euo pipefail

DISCOVERY_DB="${1:?用法: $0 /path/to/discovery_database}"
VAULT_DIR="$(cd "$(dirname "$0")/.." && pwd)/vault/companies"
INDEX_FILE="$(cd "$(dirname "$0")/.." && pwd)/vault/_index.json"

# Ticker → Company name mapping
declare -A TICKER_MAP=(
  ["APP"]="AppLovin"
  ["DUOL"]="Duolingo"
  ["SPOT"]="Spotify"
  ["BILI"]="Bilibili"
  ["POP"]="PopMart"
  ["NVDA"]="Nvidia"
  ["TEM"]="TempusAI"
)

echo "📦 Discovery Database 导入工具"
echo "  Source: $DISCOVERY_DB"
echo "  Target: $VAULT_DIR"
echo ""

# Check source exists
if [ ! -d "$DISCOVERY_DB" ]; then
  echo "❌ 找不到 $DISCOVERY_DB"
  exit 1
fi

# List available tickers
echo "📋 发现以下公司:"
for ticker_dir in "$DISCOVERY_DB"/*/; do
  ticker=$(basename "$ticker_dir")
  [ "$ticker" = "scripts" ] && continue
  company="${TICKER_MAP[$ticker]:-$ticker}"
  file_count=$(find "$ticker_dir" -type f | wc -l | tr -d ' ')
  size=$(du -sh "$ticker_dir" 2>/dev/null | cut -f1)
  echo "  $ticker → $company ($file_count files, $size)"
done
echo ""

# Process each ticker
for ticker_dir in "$DISCOVERY_DB"/*/; do
  ticker=$(basename "$ticker_dir")
  [ "$ticker" = "scripts" ] && continue

  company="${TICKER_MAP[$ticker]:-$ticker}"
  target="$VAULT_DIR/$company"

  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "🔄 导入 $ticker → $company"

  # Create target dirs
  mkdir -p "$target"/{financials,organization/people,sources/{earnings,transcripts,social,news,research}}

  # --- 1. Financials ---
  imported=0
  for f in financials.md financials_detailed.md data_full_xbrl.md data_full_statements.md data_price_history.md data_holders.md; do
    if [ -f "$ticker_dir/$f" ]; then
      cp "$ticker_dir/$f" "$target/financials/$f"
      imported=$((imported + 1))
    fi
  done
  echo "  📊 Financials: $imported files"

  # --- 2. Organization ---
  imported=0
  if [ -d "$ticker_dir/organization" ]; then
    # Scan report
    if [ -f "$ticker_dir/organization/_org_scan_report.md" ]; then
      cp "$ticker_dir/organization/_org_scan_report.md" "$target/organization/_scan-report.md"
      imported=$((imported + 1))
    fi
    # C-Suite
    for person_file in "$ticker_dir"/organization/c_suite/*.md; do
      [ -f "$person_file" ] || continue
      cp "$person_file" "$target/organization/people/$(basename "$person_file")"
      imported=$((imported + 1))
    done
    # Board
    for person_file in "$ticker_dir"/organization/board/*.md; do
      [ -f "$person_file" ] || continue
      cp "$person_file" "$target/organization/people/board_$(basename "$person_file")"
      imported=$((imported + 1))
    done
    # VP level
    for person_file in "$ticker_dir"/organization/vp_level/*.md; do
      [ -f "$person_file" ] || continue
      cp "$person_file" "$target/organization/people/vp_$(basename "$person_file")"
      imported=$((imported + 1))
    done
    # Departed
    for person_file in "$ticker_dir"/organization/departed/*.md; do
      [ -f "$person_file" ] || continue
      cp "$person_file" "$target/organization/people/departed_$(basename "$person_file")"
      imported=$((imported + 1))
    done
    # Overview
    if [ -d "$ticker_dir/organization/overview" ]; then
      cp "$ticker_dir"/organization/overview/*.md "$target/organization/" 2>/dev/null || true
      imported=$((imported + 1))
    fi
  fi
  echo "  👥 Organization: $imported files"

  # --- 3. Sources ---
  imported=0
  # SEC filings
  if [ -d "$ticker_dir/sources/earnings" ]; then
    cp "$ticker_dir"/sources/earnings/*.md "$target/sources/earnings/" 2>/dev/null && \
      imported=$((imported + $(ls "$ticker_dir"/sources/earnings/*.md 2>/dev/null | wc -l | tr -d ' '))) || true
  fi
  # YouTube transcripts
  if [ -d "$ticker_dir/sources/youtube" ]; then
    cp "$ticker_dir"/sources/youtube/*.md "$target/sources/transcripts/" 2>/dev/null && \
      imported=$((imported + $(ls "$ticker_dir"/sources/youtube/*.md 2>/dev/null | wc -l | tr -d ' '))) || true
  fi
  # Podcast transcripts
  if [ -d "$ticker_dir/sources/podcasts_transcripts" ]; then
    cp "$ticker_dir"/sources/podcasts_transcripts/*.md "$target/sources/transcripts/" 2>/dev/null && \
      imported=$((imported + $(ls "$ticker_dir"/sources/podcasts_transcripts/*.md 2>/dev/null | wc -l | tr -d ' '))) || true
  fi
  # Social media
  if [ -d "$ticker_dir/sources/social" ]; then
    cp "$ticker_dir"/sources/social/*.md "$target/sources/social/" 2>/dev/null && \
      imported=$((imported + $(ls "$ticker_dir"/sources/social/*.md 2>/dev/null | wc -l | tr -d ' '))) || true
  fi
  # Substack
  if [ -d "$ticker_dir/sources/substack_analysis" ]; then
    cp "$ticker_dir"/sources/substack_analysis/*.md "$target/sources/news/" 2>/dev/null && \
      imported=$((imported + $(ls "$ticker_dir"/sources/substack_analysis/*.md 2>/dev/null | wc -l | tr -d ' '))) || true
  fi
  # News
  if [ -d "$ticker_dir/sources/news_investigations" ]; then
    cp "$ticker_dir"/sources/news_investigations/*.md "$target/sources/news/" 2>/dev/null && \
      imported=$((imported + $(ls "$ticker_dir"/sources/news_investigations/*.md 2>/dev/null | wc -l | tr -d ' '))) || true
  fi
  # Perplexity research
  if [ -d "$ticker_dir/sources/perplexity" ]; then
    cp "$ticker_dir"/sources/perplexity/*.md "$target/sources/research/" 2>/dev/null && \
      imported=$((imported + $(ls "$ticker_dir"/sources/perplexity/*.md 2>/dev/null | wc -l | tr -d ' '))) || true
  fi
  echo "  📎 Sources: $imported files"

  # --- 4. Profile (merge, don't overwrite) ---
  if [ -f "$ticker_dir/profile.md" ] && [ ! -f "$target/profile_discovery.md" ]; then
    cp "$ticker_dir/profile.md" "$target/profile_discovery.md"
    echo "  📝 Profile: copied as profile_discovery.md (won't overwrite profile.json)"
  fi

  # --- 5. Signals ---
  if [ -d "$ticker_dir/signals" ]; then
    mkdir -p "$target/signals_imported"
    cp "$ticker_dir"/signals/*.md "$target/signals_imported/" 2>/dev/null || true
    sig_count=$(ls "$target"/signals_imported/*.md 2>/dev/null | wc -l | tr -d ' ')
    echo "  📡 Signals: $sig_count files (imported to signals_imported/, needs merge)"
  fi

  echo "  ✅ $ticker → $company 完成"
  echo ""
done

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ 导入完成！"
echo ""
echo "⚠️  注意事项："
echo "  1. profile_discovery.md 需要手动合并到 profile.json"
echo "  2. signals_imported/ 需要和 daily/ 去重合并"
echo "  3. financials/ 目前是原始Markdown，如需JSON格式需额外转换"
echo "  4. 已有的 scoring/artifacts/historical 目录未被修改"
