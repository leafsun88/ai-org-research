"""A-share public-company adapter scaffold with AKShare hooks."""

from __future__ import annotations

from .common import PublicCompanyTarget, record_extraction_gap, write_probe_report


def collect_cninfo_a(target: PublicCompanyTarget) -> dict:
    status = {
        "status": "not_run_for_pilot",
        "items": [],
        "gaps": [
            {
                "reason": "cninfo_adapter_requires_a_share_target",
                "next_step": "Use AKShare/CNInfo for annual, semiannual, quarterly reports, IPO prospectus, statements, holders, dividends, buybacks, and guidance.",
            }
        ],
    }
    record_extraction_gap(target, {"adapter": "cninfo_a", "reason": "not_run_for_pilot"})
    write_probe_report(target, "cninfo_a", status)
    return status

