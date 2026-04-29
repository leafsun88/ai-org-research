#!/bin/bash
# 为指定公司的discovery/目录生成_summary.json
# 用法: ./generate-summary.sh <company-dir>
# 示例: ./generate-summary.sh vault/companies/Duolingo

CO_DIR="$1"
DISC="$CO_DIR/discovery"
OUT="$DISC/_summary.json"

if [ ! -d "$DISC" ]; then
  echo "No discovery/ directory at $DISC"
  exit 1
fi

# 基础统计
TOTAL_FILES=$(find "$DISC" -type f ! -name '.DS_Store' ! -name '_summary.json' | wc -l | tr -d ' ')
TOTAL_SIZE_KB=$(du -sk "$DISC" 2>/dev/null | cut -f1)
LATEST_FILE=$(find "$DISC" -type f ! -name '.DS_Store' ! -name '_summary.json' -printf '%T@ %p\n' 2>/dev/null | sort -rn | head -1 | cut -d' ' -f2-)
LATEST_DATE=$(stat -f '%Sm' -t '%Y-%m-%d' "$LATEST_FILE" 2>/dev/null || date -r "$LATEST_FILE" '+%Y-%m-%d' 2>/dev/null)

# Sources统计
sources_json="{"
for src in earnings youtube podcasts_transcripts substack_analysis social news_investigations perplexity; do
  dir="$DISC/sources/$src"
  if [ -d "$dir" ]; then
    count=$(find "$dir" -type f ! -name '.DS_Store' | wc -l | tr -d ' ')
    latest=$(ls -t "$dir/" 2>/dev/null | head -1)
    sources_json="$sources_json\"$src\":{\"count\":$count,\"latest\":\"$latest\"},"
  fi
done
sources_json="${sources_json%,}}"

# Organization统计
org_json="{"
org_total=0
for sub in c_suite board vp_level departed overview; do
  dir="$DISC/organization/$sub"
  if [ -d "$dir" ]; then
    count=$(find "$dir" -type f ! -name '.DS_Store' | wc -l | tr -d ' ')
    org_total=$((org_total + count))
    org_json="$org_json\"$sub\":$count,"
  fi
done
org_json="${org_json%,}}"

# Top 10 largest files
top_files="["
while IFS= read -r line; do
  size=$(echo "$line" | awk '{print $1}')
  path=$(echo "$line" | awk '{$1=""; print substr($0,2)}' | sed "s|$DISC/||")
  top_files="$top_files{\"path\":\"$path\",\"size_kb\":$((size/1024))},"
done < <(find "$DISC" -type f ! -name '.DS_Store' ! -name '_summary.json' -printf '%s %p\n' | sort -rn | head -10)
top_files="${top_files%,}]"

# Key files existence
has_org_report=$([ -f "$DISC/organization/_org_scan_report.md" ] && echo "true" || echo "false")
has_profile=$([ -f "$DISC/profile.md" ] && echo "true" || echo "false")
has_financials=$([ -f "$DISC/financials.md" ] && echo "true" || echo "false")

cat > "$OUT" << ENDJSON
{
  "generated": "$(date +%Y-%m-%d)",
  "file_count": $TOTAL_FILES,
  "total_size_kb": $TOTAL_SIZE_KB,
  "last_updated": "$LATEST_DATE",
  "sources": $sources_json,
  "organization": {
    "people_count": $org_total,
    "breakdown": $org_json
  },
  "key_files": {
    "org_scan_report": $has_org_report,
    "profile": $has_profile,
    "financials": $has_financials
  },
  "top_files_by_size": $top_files,
  "recommended_read_order": [
    "profile.md",
    "financials.md",
    "organization/_org_scan_report.md",
    "sources/earnings/ (latest 10-K)",
    "sources/youtube/ (CEO interviews)",
    "sources/social/ (sentiment)"
  ]
}
ENDJSON

echo "Generated $OUT ($TOTAL_FILES files, ${TOTAL_SIZE_KB}KB)"
