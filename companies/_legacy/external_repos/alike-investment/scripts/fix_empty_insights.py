#!/usr/bin/env python3
"""
修复 investment-memo.md 中 1.1 D1-D7 表格里的空一句话判断和空总结句。
从 alike-memo.md 重新提取。
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


def extract_insights_flexible(alike_text):
    """Extract one-line insight for each D, handling various heading formats."""
    insights = {}
    # Match: ## D1 or ### D1 with any separator (—, --, -, :, etc)
    parts = re.split(r'#{2,3}\s+(D\d)\s*[^\n]*\n', alike_text)
    # parts: [before, "D1", content1, "D2", content2, ...]
    for i in range(1, len(parts), 2):
        d_key = parts[i].lower()
        content = parts[i + 1] if i + 1 < len(parts) else ""
        # First bold text is the core insight
        bold_match = re.search(r'\*\*(.+?)\*\*', content)
        if bold_match:
            insight = bold_match.group(1).strip()
            if len(insight) > 80:
                insight = insight[:77] + "..."
            insights[d_key] = insight
    return insights


def extract_one_liner(alike_text):
    """Extract one-line conclusion from various formats."""
    # Try: ## 一句话结论\n\n**XXX**
    m = re.search(r'##\s*一句话结论\s*\n+\*\*(.+?)\*\*', alike_text, re.DOTALL)
    if m:
        s = m.group(1).strip().replace('\n', ' ')
        if len(s) > 120:
            s = s[:117] + "..."
        return s
    # Try first bold line after frontmatter that's not a heading
    # Skip frontmatter
    fm_end = alike_text.find('---', 4)
    if fm_end > 0:
        body = alike_text[fm_end+3:]
    else:
        body = alike_text
    # Find first standalone **XXX** paragraph (not inside a heading)
    for line in body.split('\n'):
        line = line.strip()
        if line.startswith('**') and line.endswith('**') and not line.startswith('#'):
            s = line.strip('*').strip()
            if len(s) > 20:  # skip short labels
                if len(s) > 120:
                    s = s[:117] + "..."
                return s
    return ""


def fix_memo(slug):
    memo_path = VAULT / slug / "scoring" / "investment-memo.md"
    alike_path = VAULT / slug / "scoring" / "alike-memo.md"

    if not memo_path.exists() or not alike_path.exists():
        return f"SKIP {slug}: missing files"

    memo = memo_path.read_text(encoding="utf-8")
    alike = alike_path.read_text(encoding="utf-8")

    if "### 1.1 D1-D7 组织评分总览" not in memo:
        return f"SKIP {slug}: no 1.1 section"

    changed = False

    # Fix empty one-liner: line with just ****
    if "\n****\n" in memo:
        one_liner = extract_one_liner(alike)
        if one_liner:
            memo = memo.replace("\n****\n", f"\n**{one_liner}**\n")
            changed = True

    # Fix empty insights in table rows
    insights = extract_insights_flexible(alike)
    for d_key, d_name in D_NAMES.items():
        # Match: | D1 CEO认知质量 | 4.0/5 |  |
        pattern = rf'(\| {re.escape(d_name)} \| [\d.⛔]+/5 \|)\s*\|'
        match = re.search(pattern, memo)
        if match:
            current_line = match.group(0)
            if current_line.rstrip().endswith("|  |") or current_line.rstrip().endswith("| |"):
                insight = insights.get(d_key, "")
                if insight:
                    new_line = f"{match.group(1)} {insight} |"
                    memo = memo.replace(current_line, new_line)
                    changed = True

    if changed:
        memo_path.write_text(memo, encoding="utf-8")
        return f"FIXED {slug}"
    return f"OK {slug}: nothing to fix"


def main():
    for d in sorted(VAULT.iterdir()):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        memo_path = d / "scoring" / "investment-memo.md"
        if memo_path.exists() and "### 1.1 D1-D7" in memo_path.read_text(encoding="utf-8"):
            print(fix_memo(d.name))


if __name__ == "__main__":
    main()
