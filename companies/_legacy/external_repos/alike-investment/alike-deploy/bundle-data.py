#!/usr/bin/env python3
"""Bundle vault data into static JSON files for Vercel deployment."""

import json
import glob
import os

VAULT = "/Users/wangguanjie/Desktop/Claude Data/共创产品/vault/companies"
OUT = "/Users/wangguanjie/Desktop/Claude Data/共创产品/alike-deploy/data"
COMPANIES = ["Duolingo", "Spotify", "Bilibili", "PopMart"]

ARTIFACT_KEYS = [
    "alike-memo", "biz-inflection", "ceo-profile", "investment-memo",
    "kq-tracker", "org-inflection", "org-xray", "red-team"
]

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  wrote {path}  ({os.path.getsize(path):,} bytes)")

def bundle_scoring(slug):
    """Merge signal-engine + dim-analysis into one scoring file."""
    company_dir = os.path.join(VAULT, slug, "scoring")
    result = {"company": slug, "slug": slug, "signal_engine": None, "dim_analysis": None}

    # Find signal-engine (may have date suffix)
    se_files = sorted(glob.glob(os.path.join(company_dir, "signal-engine-*.json")))
    if se_files:
        result["signal_engine"] = load_json(se_files[-1])  # latest
        print(f"  signal-engine: {os.path.basename(se_files[-1])}")

    # Find dim-analysis
    da_path = os.path.join(company_dir, "dim-analysis.json")
    if os.path.exists(da_path):
        result["dim_analysis"] = load_json(da_path)
        print(f"  dim-analysis: found")
    else:
        print(f"  dim-analysis: not found")

    out_path = os.path.join(OUT, "scoring", f"{slug}.json")
    save_json(out_path, result)
    return result["signal_engine"] is not None

def bundle_artifacts(slug):
    """Merge all artifact files into one."""
    art_dir = os.path.join(VAULT, slug, "artifacts")
    if not os.path.isdir(art_dir):
        print(f"  artifacts: directory not found")
        return False

    artifacts = {}
    for key in ARTIFACT_KEYS:
        path = os.path.join(art_dir, f"{key}.json")
        if os.path.exists(path):
            artifacts[key] = load_json(path)

    if not artifacts:
        print(f"  artifacts: no files found")
        return False

    result = {"company": slug, "artifacts": artifacts}
    out_path = os.path.join(OUT, "artifacts", f"{slug}.json")
    save_json(out_path, result)
    print(f"  artifacts: {len(artifacts)} files merged")
    return True

def main():
    index = []

    for slug in COMPANIES:
        print(f"\n=== {slug} ===")
        has_scoring = bundle_scoring(slug)
        has_artifacts = bundle_artifacts(slug)
        index.append({
            "slug": slug,
            "name": slug,
            "has_scoring": has_scoring,
            "has_artifacts": has_artifacts
        })

    # Write companies index
    companies_path = os.path.join(OUT, "companies.json")
    save_json(companies_path, {"companies": index})

    print(f"\nDone. {len(index)} companies bundled.")

if __name__ == "__main__":
    main()
