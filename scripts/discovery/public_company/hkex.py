"""HKEX public-company adapter scaffold."""

from __future__ import annotations

from .common import PublicCompanyTarget, record_extraction_gap, write_probe_report


def collect_hkex(target: PublicCompanyTarget) -> dict:
    status = {
        "status": "not_run_for_pilot",
        "items": [],
        "gaps": [
            {
                "reason": "hkex_adapter_requires_live_target",
                "next_step": "Use HKEXnews annual/interim/prospectus/circular search, then yfinance .HK market data.",
            }
        ],
    }
    record_extraction_gap(target, {"adapter": "hkex", "reason": "not_run_for_pilot"})
    write_probe_report(target, "hkex", status)
    return status

