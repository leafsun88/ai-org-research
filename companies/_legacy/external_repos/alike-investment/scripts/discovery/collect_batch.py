#!/usr/bin/env python3
"""
批量调用 Alike Investment 的单公司 collect 流程。

支持三种输入：
1. 直接传 ticker:          python3 collect_batch.py APP NVDA
2. ticker=公司名:         python3 collect_batch.py "APP=AppLovin" "RDDT=Reddit"
3. 从文件读取:            python3 collect_batch.py --file companies.txt

文件格式（每行一条，支持 # 注释）：
  APP
  NVDA|NVIDIA|英伟达
  RDDT=Reddit
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
INDEX_FILE = PROJECT_ROOT / "vault" / "_index.json"

sys.path.insert(0, str(SCRIPT_DIR))

from collect import COMPANY_ALIASES, ALL_MODULES, collect  # noqa: E402


@dataclass
class CompanySpec:
    ticker: str
    company_name: str | None = None
    company_name_cn: str | None = None


def load_index_names() -> dict[str, tuple[str | None, str | None]]:
    if not INDEX_FILE.exists():
        return {}

    data = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    companies = data.get("companies", {})
    ticker_map = data.get("ticker_map", {})

    names: dict[str, tuple[str | None, str | None]] = {}
    for ticker, slug in ticker_map.items():
        company = companies.get(slug, {})
        name = company.get("name_en") or company.get("name")
        name_cn = company.get("name") if company.get("name") != name else None
        names[ticker.upper()] = (name, name_cn)
    return names


def parse_company_spec(raw: str, index_names: dict[str, tuple[str | None, str | None]]) -> CompanySpec:
    text = raw.strip()
    if not text:
        raise ValueError("Empty company spec")

    if "|" in text:
        parts = [part.strip() for part in text.split("|")]
        ticker = parts[0].upper()
        company_name = parts[1] if len(parts) > 1 and parts[1] else None
        company_name_cn = parts[2] if len(parts) > 2 and parts[2] else None
        return CompanySpec(ticker=ticker, company_name=company_name, company_name_cn=company_name_cn)

    if "=" in text:
        ticker, company_name = [part.strip() for part in text.split("=", 1)]
        return CompanySpec(ticker=ticker.upper(), company_name=company_name or None)

    ticker = text.upper()
    alias = COMPANY_ALIASES.get(ticker)
    if alias:
        return CompanySpec(
            ticker=ticker,
            company_name=alias[0] or None,
            company_name_cn=alias[1] or None,
        )

    indexed = index_names.get(ticker)
    if indexed:
        return CompanySpec(
            ticker=ticker,
            company_name=indexed[0],
            company_name_cn=indexed[1],
        )

    return CompanySpec(ticker=ticker)


def load_specs(args_specs: list[str], file_path: str | None) -> list[str]:
    specs = list(args_specs)
    if file_path:
        path = Path(file_path)
        for line in path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            specs.append(stripped)
    return specs


def main() -> int:
    parser = argparse.ArgumentParser(description="Alike Investment 批量数据采集")
    parser.add_argument("companies", nargs="*", help="公司列表：APP / APP=AppLovin / NVDA|NVIDIA|英伟达")
    parser.add_argument("--file", help="从文件读取公司列表")
    parser.add_argument("--only", help=f"仅运行指定模块: {','.join(ALL_MODULES)}")
    parser.add_argument("--skip", help="跳过指定模块")
    parser.add_argument("--continue-on-error", action="store_true", help="单家公司失败后继续跑后续公司")
    parser.add_argument("--dry-run", action="store_true", help="只解析输入，不实际执行采集")

    args = parser.parse_args()

    raw_specs = load_specs(args.companies, args.file)
    if not raw_specs:
        parser.error("请至少提供一个公司 ticker，或通过 --file 提供名单")

    index_names = load_index_names()
    specs = [parse_company_spec(raw, index_names) for raw in raw_specs]
    only = args.only.split(",") if args.only else None
    skip = args.skip.split(",") if args.skip else None

    print(f"批量任务数: {len(specs)}")
    for idx, spec in enumerate(specs, start=1):
        display_name = spec.company_name or "(auto)"
        display_cn = f" / {spec.company_name_cn}" if spec.company_name_cn else ""
        print(f"{idx}. {spec.ticker} -> {display_name}{display_cn}")

    if args.dry_run:
        print("Dry run 完成，未执行采集。")
        return 0

    failures: list[tuple[CompanySpec, str]] = []
    for idx, spec in enumerate(specs, start=1):
        print(f"\n{'=' * 72}")
        print(f"[{idx}/{len(specs)}] 开始采集: {spec.ticker} {spec.company_name or ''}".strip())
        print(f"{'=' * 72}")
        try:
            collect(
                ticker=spec.ticker,
                company_name=spec.company_name,
                company_name_cn=spec.company_name_cn,
                only=only,
                skip=skip,
            )
        except Exception as exc:
            failures.append((spec, str(exc)))
            print(f"❌ 采集失败: {spec.ticker} - {exc}")
            if not args.continue_on_error:
                break

    print(f"\n{'=' * 72}")
    print("批量采集结束")
    print(f"总数: {len(specs)}")
    print(f"成功: {len(specs) - len(failures)}")
    print(f"失败: {len(failures)}")
    for spec, error in failures:
        print(f"- {spec.ticker}: {error}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
