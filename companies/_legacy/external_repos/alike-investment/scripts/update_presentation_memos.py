#!/usr/bin/env python3
"""
更新 presentation/index.html 中 inline DATA 里的 full_memo 和 exec_summary 字段。
从 vault/companies/{slug}/scoring/investment-memo.md 读取最新内容。
"""

import re, json
from pathlib import Path

ROOT = Path("/Users/wangguanjie/Desktop/Claude Data/共创产品")
HTML_PATH = ROOT / "presentation" / "index.html"
VAULT = ROOT / "vault" / "companies"


def extract_exec_summary(memo_text: str) -> str:
    """Extract Executive Summary section from memo."""
    # Find ## Executive Summary
    m = re.search(r'^## Executive Summary\s*\n', memo_text, re.MULTILINE)
    if not m:
        return ""
    start = m.end()
    # Find next ## heading
    next_h2 = re.search(r'^## ', memo_text[start:], re.MULTILINE)
    if next_h2:
        end = start + next_h2.start()
    else:
        end = len(memo_text)
    return "## Executive Summary\n" + memo_text[start:end].strip()


def main():
    html = HTML_PATH.read_text(encoding="utf-8")

    # Extract the DATA JSON array
    data_match = re.search(r'const DATA = (\[.*?\]);\s*\n', html, re.DOTALL)
    if not data_match:
        print("ERROR: Could not find const DATA in index.html")
        return

    data = json.loads(data_match.group(1))
    updated = 0

    # slug alias map (presentation slug -> vault directory name)
    SLUG_ALIAS = {"veeva": "veeva-systems"}

    for company in data:
        slug = company.get("slug", "")
        vault_slug = SLUG_ALIAS.get(slug, slug)
        memo_path = VAULT / vault_slug / "scoring" / "investment-memo.md"
        if not memo_path.exists():
            continue

        memo_text = memo_path.read_text(encoding="utf-8")
        exec_summary = extract_exec_summary(memo_text)

        # Update fields
        if memo_text != company.get("full_memo", ""):
            company["full_memo"] = memo_text
            company["has_memos"] = True
            if exec_summary:
                company["exec_summary"] = exec_summary
            updated += 1
            print(f"  UPDATED: {slug}")

    # Write back
    new_json = json.dumps(data, ensure_ascii=False)
    new_html = html[:data_match.start(1)] + new_json + html[data_match.end(1):]
    HTML_PATH.write_text(new_html, encoding="utf-8")
    print(f"\nDone. Updated {updated} companies in presentation DATA.")


if __name__ == "__main__":
    main()
