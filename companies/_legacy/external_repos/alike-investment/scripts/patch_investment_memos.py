#!/usr/bin/env python3
"""
批量为 investment-memo.md 插入 D1-D7 评分总览表（1.1节）。
- 从 alike-memo.md 提取分数和各维度一句话判断
- 插入到 "## 一、组织穿透" 之后、原 "### 1.1" 之前
- 原 1.1→1.2, 1.2→1.3, 1.3→1.4, 1.4→1.5 顺位递增
- 删除所有 "（篇幅比例xx%）" 标注
- 跳过 Duolingo（将单独重写）
"""

import re, os, json
from pathlib import Path

VAULT = Path("/Users/wangguanjie/Desktop/Claude Data/共创产品/vault/companies")

# D维度中文名
D_NAMES = {
    "d1": "D1 CEO认知质量",
    "d2": "D2 Key Leader深度",
    "d3": "D3 考核激励机制",
    "d4": "D4 信息架构",
    "d5": "D5 组织熵减能力",
    "d6": "D6 Talent Density",
    "d7": "D7 Key Bet质量",
}


def parse_frontmatter(text):
    """Extract frontmatter without PyYAML. Handles inline dicts like {d1: 4.0}."""
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if not m:
        return {}
    raw = m.group(1)
    result = {}
    for line in raw.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        km = re.match(r'^(\w+)\s*:\s*(.+)$', line)
        if not km:
            continue
        key, val = km.group(1), km.group(2).strip()
        # Parse inline dict {d1: 4.0, d2: 3.5, ...}
        if val.startswith('{') and val.endswith('}'):
            inner = val[1:-1]
            d = {}
            for pair in inner.split(','):
                pair = pair.strip()
                pm = re.match(r'(\w+)\s*:\s*(.+)', pair)
                if pm:
                    try:
                        d[pm.group(1).strip()] = float(pm.group(2).strip())
                    except ValueError:
                        d[pm.group(1).strip()] = pm.group(2).strip()
            result[key] = d
        else:
            # Try numeric
            try:
                result[key] = float(val) if '.' in val else int(val)
            except ValueError:
                result[key] = val.strip('"').strip("'")
    return result


def extract_d_insights(alike_text):
    """Extract one-line insight for each D dimension from alike-memo."""
    insights = {}
    # Pattern: ### D1 — ... or ### D1 — CEO认知质量：X/5
    # Then look for the first bold line as the insight
    sections = re.split(r'### (D\d)\s*[—–-]', alike_text)
    for i in range(1, len(sections), 2):
        d_key = sections[i].lower()
        content = sections[i + 1] if i + 1 < len(sections) else ""
        # First bold text is the core insight
        bold_match = re.search(r'\*\*(.+?)\*\*', content)
        if bold_match:
            insight = bold_match.group(1).strip()
            # Truncate to reasonable length
            if len(insight) > 80:
                insight = insight[:77] + "..."
            insights[d_key] = insight
        else:
            insights[d_key] = ""
    return insights


def build_table(fm, insights):
    """Build the D1-D7 overview table markdown."""
    d_scores = fm.get("d_scores", {})
    alike_score = fm.get("alike_score", "?")
    fit_score = fm.get("fit_score", "?")

    lines = []
    lines.append("| 维度 | 得分 | 一句话判断 |")
    lines.append("|------|------|-----------|")
    for key in ["d1", "d2", "d3", "d4", "d5", "d6", "d7"]:
        score = d_scores.get(key, "?")
        name = D_NAMES.get(key, key.upper())
        insight = insights.get(key, "")
        lines.append(f"| {name} | {score}/5 | {insight} |")
    lines.append(f"| **Alike Score** | **{alike_score}/100** | Fit: {fit_score}/5 |")
    return "\n".join(lines)


def patch_memo(slug):
    """Patch a single company's investment-memo.md."""
    memo_path = VAULT / slug / "scoring" / "investment-memo.md"
    alike_path = VAULT / slug / "scoring" / "alike-memo.md"

    if not memo_path.exists():
        return f"SKIP {slug}: no investment-memo.md"
    if not alike_path.exists():
        return f"SKIP {slug}: no alike-memo.md"

    memo_text = memo_path.read_text(encoding="utf-8")
    alike_text = alike_path.read_text(encoding="utf-8")

    # Already patched?
    if "### 1.1 D1-D7 组织评分总览" in memo_text:
        return f"SKIP {slug}: already has 1.1 D1-D7 table"

    # Parse alike-memo frontmatter for scores
    fm = parse_frontmatter(alike_text)
    if not fm.get("d_scores"):
        return f"SKIP {slug}: alike-memo has no d_scores"

    # Extract per-dimension insights
    insights = extract_d_insights(alike_text)

    # Build the 1.1 section
    # Get company one-line conclusion from alike-memo
    one_liner_match = re.search(r'## 一句话结论\s*\n\s*\*\*(.+?)\*\*', alike_text)
    if not one_liner_match:
        one_liner_match = re.search(r'\*\*一句话.*?[:：]\s*(.+?)\*\*', alike_text)
    one_liner = one_liner_match.group(1).strip() if one_liner_match else ""
    if len(one_liner) > 120:
        one_liner = one_liner[:117] + "..."

    table = build_table(fm, insights)

    new_section = f"""### 1.1 D1-D7 组织评分总览

**{one_liner}**

{table}

"""

    # Step 1: Delete "（篇幅比例xx%）" or "(篇幅比例xx%)"
    memo_text = re.sub(r'[（(]篇幅比例\d+%\+?[）)]', '', memo_text)

    # Step 2: Insert 1.1 and renumber existing 1.x sections
    # Find "## 一、组织穿透" line
    org_match = re.search(r'^(## 一、组织穿透.*)\n', memo_text, re.MULTILINE)
    if not org_match:
        return f"SKIP {slug}: no '## 一、组织穿透' heading found"

    # Find the first ### 1.x after 组织穿透
    first_sub = re.search(r'^### 1\.\d', memo_text[org_match.end():], re.MULTILINE)
    if not first_sub:
        return f"SKIP {slug}: no subsections found under 组织穿透"

    insert_pos = org_match.end() + first_sub.start()

    # Renumber: 1.1→1.2, 1.2→1.3, etc. (go from high to low to avoid double-rename)
    # Find max section number first
    section_nums = [int(m.group(1)) for m in re.finditer(r'^### 1\.(\d)', memo_text[org_match.end():], re.MULTILINE)]
    if section_nums:
        max_num = max(section_nums)
        for n in range(max_num, 0, -1):
            memo_text = memo_text.replace(f"### 1.{n} ", f"### 1.{n+1} ")

    # Re-find insert position after renumber
    org_match = re.search(r'^(## 一、组织穿透.*)\n', memo_text, re.MULTILINE)
    first_sub = re.search(r'^### 1\.\d', memo_text[org_match.end():], re.MULTILINE)
    insert_pos = org_match.end() + first_sub.start()

    # Insert new 1.1
    memo_text = memo_text[:insert_pos] + new_section + memo_text[insert_pos:]

    memo_path.write_text(memo_text, encoding="utf-8")
    return f"OK {slug}: inserted 1.1 D1-D7 table, renumbered sections"


def main():
    # Get all companies with investment-memo.md
    results = []
    for company_dir in sorted(VAULT.iterdir()):
        if not company_dir.is_dir():
            continue
        slug = company_dir.name
        if slug.startswith("_") or slug.startswith("."):
            continue
        # Skip Duolingo (will be rewritten separately)
        if slug == "duolingo":
            results.append(f"SKIP {slug}: will be rewritten separately")
            continue
        memo_path = company_dir / "scoring" / "investment-memo.md"
        if memo_path.exists():
            result = patch_memo(slug)
            results.append(result)

    for r in results:
        print(r)


if __name__ == "__main__":
    main()
