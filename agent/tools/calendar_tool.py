from __future__ import annotations
from datetime import datetime, timedelta
from typing import Optional

def find_common_slots(
    window_start: str,
    window_end: str,
    duration_minutes: int,
    daily_start: str = "09:00",
    daily_end: str = "17:00",
    max_results: int = 3,
) -> dict:
    try:
        start_dt = datetime.fromisoformat(window_start)
        end_dt = datetime.fromisoformat(window_end)
        start_date = start_dt.date()
        end_date = end_dt.date()
    except Exception as err:
        try:
            start_date = datetime.fromisoformat(window_start).date()
            end_date = datetime.fromisoformat(window_end).date()
        except Exception as err2:
            return {"status": "invalid_window", "detail": str(err2)}
    if end_date < start_date or duration_minutes <= 0:
        return {"status": "invalid_window"}
    slots = []
    cur = start_date
    while cur <= end_date and len(slots) < max_results:
        day_start = datetime.fromisoformat(f"{cur.isoformat()}T{daily_start}:00")
        day_end = datetime.fromisoformat(f"{cur.isoformat()}T{daily_end}:00")
        t = day_start
        while t + timedelta(minutes=duration_minutes) <= day_end and len(slots) < max_results:
            slot_end = t + timedelta(minutes=duration_minutes)
            slots.append({"start": t.isoformat(), "end": slot_end.isoformat()})
            t += timedelta(minutes=90)
        cur += timedelta(days=1)
    if not slots:
        return {"status": "no_slots"}
    return {"status": "ok", "slots": slots}
