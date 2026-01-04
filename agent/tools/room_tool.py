from __future__ import annotations
from typing import Optional, List
from agent.memory.room_catalog import ROOMS, Room

def find_rooms(
    city: Optional[str] = None,
    min_capacity: Optional[int] = None,
    video: Optional[bool] = None,
) -> dict:
    matches: List[Room] = []
    for r in ROOMS:
        if city and r.city.lower() != city.lower():
            continue
        if min_capacity and r.capacity < min_capacity:
            continue
        if video is not None and r.video != video:
            continue
        matches.append(r)
    return {
        "count": len(matches),
        "results": [
            {
                "city": r.city,
                "name": r.name,
                "capacity": r.capacity,
                "video": r.video,
                "notes": r.notes,
            }
            for r in matches
        ],
        "hint": "Adjust city or min_capacity or video to refine results.",
    }
