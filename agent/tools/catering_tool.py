from __future__ import annotations
from typing import Optional, List
from agent.memory.catering_catalog import CATERING, CateringOption


def find_catering(
    city: Optional[str] = None,
    diet: Optional[str] = None,
    max_per_person_eur: Optional[int] = None,
) -> dict:
    matches: List[CateringOption] = []
    for c in CATERING:
        if city and c.city.lower() != city.lower():
            continue
        if diet and c.diet.lower() != diet.lower():
            continue
        if max_per_person_eur is not None and c.per_person_eur > max_per_person_eur:
            continue
        matches.append(c)
    return {
        "count": len(matches),
        "results": [
            {
                "city": c.city,
                "name": c.name,
                "per_person_eur": c.per_person_eur,
                "diet": c.diet,
                "notes": c.notes,
            }
            for c in matches
        ],
        "hint": "Adjust city, diet, or max_per_person_eur to refine results.",
    }
