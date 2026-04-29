#!/usr/bin/env python3
"""
Fix D1-D7 overview table rows that show "校准参照" (label) instead of actual insight.

Root cause: previous extractor grabbed the FIRST bold text after each D heading,
but alike-memos start D sections with "**校准参照**：..." as a sub-label.
Fix: skip known label bolds and short bolds, grab first meaningful bold text.
"""

import re
from pathlib import Path

VAULT = Path("/Users/wangguanjie/Desktop/Claude Data/共创产品/vault/companies")

# Bolds that are sub-labels, not insights — skip them
SKIP_LABEL_PREFIXES = (
    "校准参照", "校准参考", "校准锚点", "校准",
    "关键证据", "核心判断", "核心观点",
    "信息充分度", "对标", "锚点",
    "关键引用", "关键数据",
)

# Companies to fix (those with polluted tables)
TARGETS = [
    "veeva-systems", "stripe", "palantir", "datadog",
    "cursor", "crowdstrike", "amd", "axon",
]

D_NAMES = {
    "d1": "D1 CEO认知质量",
    "d2": "D2 Key Leader深度",
    "d3": "D3 考核激励机制",
    "d4": "D4 信息架构",
    "d5": "D5 组织熵减能力",
    "d6": "D6 Talent Density",
    "d7": "D7 Key Bet质量",
}


def is_label_bold(text: str) -> bool:
    """Check if a bold text is a label (not an insight)."""
    t = text.strip()
    if len(t) < 15:
        return True
    for prefix in SKIP_LABEL_PREFIXES:
        if t.startswith(prefix):
            return True
    # Bullet list markers like "[S3] 第一性原理..." are OK if long enough
    return False


def clean_insight(text: str) -> str:
    """Clean up an insight text for table display."""
    # Strip leading [S\d] markers since table is narrow
    text = re.sub(r'^\[S\d\]\s*', '', text)
    # Remove trailing punctuation for table cleanliness
    text = text.rstrip("。.")
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_d_insights(alike_text: str) -> dict:
    """Extract a meaningful one-line insight for each D dimension."""
    insights = {}
    # Split on D headings (## or ### level, any separator after D\d)
    sections = re.split(r'#{2,3}\s+(D\d)[^\n]*\n', alike_text)
    # sections = [preamble, 'D1', content1, 'D2', content2, ...]
    for i in range(1, len(sections), 2):
        d_key = sections[i].lower()
        if i + 1 >= len(sections):
            break
        content = sections[i + 1]
        # Stop at next section-level heading to avoid leaking into D2
        content = re.split(r'\n#{2,3}\s+', content)[0]

        insight = extract_one_insight(content)
        insights[d_key] = insight
    return insights


def extract_one_insight(content: str) -> str:
    """Extract one insight from a D section's content."""
    # Strategy 1: Find first non-label bold in the content
    # Iterate through bold matches to find the first meaningful one
    for m in re.finditer(r'\*\*(.+?)\*\*', content, re.DOTALL):
        bold_text = m.group(1)
        if is_label_bold(bold_text):
            continue

        clean = clean_insight(bold_text)
        # A bold is a "full sentence" only if it's long AND ends with sentence punctuation
        # (avoids misclassifying label-like noun phrases as sentences)
        ends_like_sentence = bool(re.search(r'[。.！!？?]$', clean))
        if len(clean) > 40 and ends_like_sentence:
            return clean

        # Bold is short or label-like — grab the following sentence
        # up to next bold or newline
        tail_start = m.end()
        tail = content[tail_start:tail_start + 500]
        # Tail usually begins with "：" or ":" then sentence
        tail = re.sub(r'^[:：]\s*', '', tail)
        # Stop at next bold, italic quote, or paragraph break
        tail = re.split(r'\*\*|\n\n|(?<=[。.！!？?])\s*\n|> \*', tail)[0]
        # Strip italic, links, citations
        tail = re.sub(r'\*([^*]+)\*', r'\1', tail)
        tail = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', tail)
        tail = re.sub(r'—\s*[^—]*$', '', tail)  # strip trailing — source
        tail_clean = clean_insight(tail)

        # Combine label + first sentence of tail
        first_sent = re.split(r'(?<=[。.])', tail_clean)[0] if tail_clean else ""
        if first_sent and len(first_sent) > 20:
            combined = f"{clean}：{first_sent}" if clean else first_sent
            return clean_insight(combined)
        if clean:
            return clean

    # Strategy 2: fallback — first non-meta paragraph
    paras = [p.strip() for p in content.split('\n\n') if p.strip()]
    for p in paras:
        if p.startswith('>') or p.startswith('|') or p.startswith('#') or p.startswith('-'):
            continue
        if p.startswith('**') and is_label_bold(p.strip('*')):
            continue
        clean = re.sub(r'\*\*|\*|`', '', p)
        clean = re.sub(r'\[S\d\]', '', clean)
        return clean_insight(clean)
    return ""


def rewrite_table(memo_text: str, insights: dict) -> tuple:
    """Rewrite D1-D7 table rows with new insights. Returns (new_text, changed_count)."""
    changed = 0

    def replace_row(match):
        nonlocal changed
        name = match.group(1)
        score = match.group(2)
        old_insight = match.group(3).strip()

        # Determine d_key from name
        d_key = None
        for k, v in D_NAMES.items():
            if v == name:
                d_key = k
                break
        if d_key is None or d_key not in insights:
            return match.group(0)

        new_insight = insights[d_key]
        if not new_insight:
            return match.group(0)
        if new_insight == old_insight:
            return match.group(0)

        changed += 1
        return f"| {name} | {score} | {new_insight} |"

    # Match table row: | D1 CEO认知质量 | 4.5/5 | ... |
    pattern = re.compile(
        r'\|\s*(D\d [^|]+?)\s*\|\s*([\d.]+/5)\s*\|\s*([^|]*?)\s*\|'
    )
    new_text = pattern.sub(replace_row, memo_text)
    return new_text, changed


def fix_company(slug: str) -> str:
    memo_path = VAULT / slug / "scoring" / "investment-memo.md"
    alike_path = VAULT / slug / "scoring" / "alike-memo.md"

    if not memo_path.exists():
        return f"SKIP {slug}: no investment-memo.md"
    if not alike_path.exists():
        return f"SKIP {slug}: no alike-memo.md"

    alike_text = alike_path.read_text(encoding="utf-8")
    memo_text = memo_path.read_text(encoding="utf-8")

    insights = extract_d_insights(alike_text)
    if not insights:
        return f"SKIP {slug}: no D sections found"

    # Show what we extracted
    preview = " | ".join(
        f"{k}={v[:30]}..." if len(v) > 30 else f"{k}={v}"
        for k, v in sorted(insights.items())
    )

    new_text, changed = rewrite_table(memo_text, insights)
    if changed == 0:
        return f"NOCHANGE {slug}: 0 rows updated\n  extracted: {preview}"

    memo_path.write_text(new_text, encoding="utf-8")
    return f"OK {slug}: {changed} rows updated\n  extracted: {preview}"


def main():
    for slug in TARGETS:
        print(fix_company(slug))
        print()


if __name__ == "__main__":
    main()
