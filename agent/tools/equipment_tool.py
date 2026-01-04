from __future__ import annotations
from typing import Optional, List, Dict


def get_equipment_recommendations(
    participants: int,
    remote_attendees: bool = False,
    has_room_video: Optional[bool] = None,
) -> Dict:
    """
    Returns a simple recommended equipment package based on audience size and remote needs.
    This is heuristic and offline (no external API).
    """
    if participants <= 0:
        return {"status": "error", "message": "participants must be > 0"}

    recs: List[Dict] = []

    # Audio basics by size
    if participants <= 8:
        recs.append({"item": "table microphone", "qty": 1, "notes": "For small rooms"})
    elif participants <= 16:
        recs.append({"item": "2x boundary microphones", "qty": 2, "notes": "Wider pickup"})
    else:
        recs.append({"item": "PA speaker", "qty": 2, "notes": "Ensure coverage"})
        recs.append({"item": "wireless handheld mic", "qty": 2, "notes": "Q&A"})

    # Video needs
    if remote_attendees:
        if has_room_video is True:
            recs.append({"item": "use in-room VC system", "qty": 1, "notes": "Room provides video"})
        else:
            recs.append({
                "item": "USB conferencing camera",
                "qty": 1,
                "notes": "Place at front, 1080p"
            })
            recs.append({
                "item": "speakerphone",
                "qty": 1,
                "notes": "Echo-cancelling device"
            })

    # Display
    if participants > 10:
        recs.append({"item": "projector or large display", "qty": 1, "notes": ">= 100'' equiv"})
    else:
        recs.append({"item": "TV/monitor", "qty": 1, "notes": "HDMI/USB-C adapters"})

    return {"status": "ok", "items": recs}
