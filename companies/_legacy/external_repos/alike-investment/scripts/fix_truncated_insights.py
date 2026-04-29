#!/usr/bin/env python3
"""
修复 investment-memo.md 中 1.1 D1-D7 表格里被截断的一句话判断。
从 alike-memo.md 提取完整文本，替换带省略号的版本。
"""

import re
from pathlib import Path

VAULT = Path("/Users/wangguanjie/Desktop/Claude Data/共创产品/vault/companies")

D_NAMES = {
    "d1": "D1 CEO认知质量",
    "d2": "D2 Key Leader深度",
    "d3": "D3 考核激励机制",
    "d4": "D4 信息架构",
    "d5": "D5 组织熵减能力",
    "d6": "D6 Talent Density",
    "d7": "D7 Key Bet质量",
}


def extract_insights_full(alike_text):
    """Extract full one-line insight for each D dimension."""
    insights = {}
    parts = re.split(r'#{2,3}\s+(D\d)\s*[^\n]*\n', alike_text)
    for i in range(1, len(parts), 2):
        d_key = parts[i].lower()
        content = parts[i + 1] if i + 1 < len(parts) else ""
        bold_match = re.search(r'\*\*(.+?)\*\*', content)
        if bold_match:
            insight = bold_match.group(1).strip()
            insights[d_key] = insight
    return insights


def fix_memo(slug):
    memo_path = VAULT / slug / "scoring" / "investment-memo.md"
    alike_path = VAULT / slug / "scoring" / "alike-memo.md"

    if not memo_path.exists() or not alike_path.exists():
        return f"SKIP {slug}: missing files"

    memo = memo_path.read_text(encoding="utf-8")
    alike = alike_path.read_text(encoding="utf-8")

    if "### 1.1 D1-D7 组织评分总览" not in memo:
        return f"SKIP {slug}: no 1.1 section"

    insights = extract_insights_full(alike)
    if not insights:
        return f"SKIP {slug}: no insights extracted"

    changed = False
    for d_key, d_name in D_NAMES.items():
        full_insight = insights.get(d_key, "")
        if not full_insight:
            continue
        # Match table row: | D1 CEO认知质量 | 4.0/5 | <current text> |
        pattern = rf'(\| {re.escape(d_name)} \| [\d.⛔]+/5 \|) (.+?) \|'
        match = re.search(pattern, memo)
        if match:
            current = match.group(2).strip()
            # Replace if truncated (has ...) or different from full
            if '...' in current or current != full_insight:
                old_line = match.group(0)
                new_line = f"{match.group(1)} {full_insight} |"
                memo = memo.replace(old_line, new_line)
                changed = True

    if changed:
        memo_path.write_text(memo, encoding="utf-8")
        return f"FIXED {slug}"
    return f"OK {slug}: already complete"


def main():
    for d in sorted(VAULT.iterdir()):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        memo_path = d / "scoring" / "investment-memo.md"
        if memo_path.exists() and "### 1.1 D1-D7" in memo_path.read_text(encoding="utf-8"):
            print(fix_memo(d.name))


if __name__ == "__main__":
    main()
