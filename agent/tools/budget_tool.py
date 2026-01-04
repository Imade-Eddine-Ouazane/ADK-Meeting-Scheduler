from __future__ import annotations
from typing import Optional


def estimate_budget(
    participants: int,
    catering_pp_eur: Optional[float] = None,
    room_cost_eur: Optional[float] = None,
    equipment_cost_eur: Optional[float] = None,
    other_costs_eur: Optional[float] = 0.0,
) -> dict:
    """
    Compute a rough meeting budget. Any missing component is treated as 0.
    Returns a breakdown and total.
    """
    if participants is None or participants <= 0:
        return {"status": "error", "message": "participants must be > 0"}

    catering_total = float(catering_pp_eur or 0.0) * participants
    room_total = float(room_cost_eur or 0.0)
    equipment_total = float(equipment_cost_eur or 0.0)
    other_total = float(other_costs_eur or 0.0)

    total = catering_total + room_total + equipment_total + other_total
    return {
        "status": "ok",
        "participants": participants,
        "breakdown": {
            "catering_total": round(catering_total, 2),
            "room_total": round(room_total, 2),
            "equipment_total": round(equipment_total, 2),
            "other_total": round(other_total, 2),
        },
        "total_eur": round(total, 2),
    }
