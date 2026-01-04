from __future__ import annotations
from typing import Optional


def check_budget_policy(
    participants: int,
    total_eur: float,
    max_pp_eur: Optional[float] = None,
    max_total_eur: Optional[float] = None,
) -> dict:
    """
    Simple policy check for meeting budgets.
    - max_pp_eur: maximum allowed spend per participant
    - max_total_eur: absolute maximum total budget
    Returns pass/fail with reasons.
    """
    issues = []
    if participants is None or participants <= 0:
        return {"status": "error", "message": "participants must be > 0"}
    if total_eur is None or total_eur < 0:
        return {"status": "error", "message": "total_eur must be >= 0"}

    if max_pp_eur is not None:
        pp = total_eur / participants
        if pp > float(max_pp_eur):
            issues.append({
                "type": "per_person_limit",
                "per_person": round(pp, 2),
                "limit": float(max_pp_eur),
            })
    if max_total_eur is not None:
        if total_eur > float(max_total_eur):
            issues.append({
                "type": "total_limit",
                "total": round(total_eur, 2),
                "limit": float(max_total_eur),
            })

    return {
        "status": "pass" if not issues else "fail",
        "participants": participants,
        "total_eur": round(total_eur, 2),
        "issues": issues,
    }
