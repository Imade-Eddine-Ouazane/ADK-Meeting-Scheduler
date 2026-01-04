from __future__ import annotations
from datetime import datetime
from typing import List, Optional
import uuid


def create_ics_event(
    summary: str,
    start_iso: str,
    end_iso: str,
    location: str = "",
    description: str = "",
    organizer: Optional[str] = None,
    attendees: Optional[List[str]] = None,
    uid: Optional[str] = None,
) -> dict:
    """
    Build a minimal ICS calendar event. Times are taken as-is from provided ISO strings.
    Returns an object with an 'ics' field containing the text.
    """
    try:
        dt_start = datetime.fromisoformat(start_iso)
        dt_end = datetime.fromisoformat(end_iso)
    except Exception as err:
        return {"status": "error", "message": f"Invalid datetime: {err}"}
    if dt_end <= dt_start:
        return {"status": "error", "message": "end must be after start"}

    def fmt(dt: datetime) -> str:
        return dt.strftime("%Y%m%dT%H%M%S")

    event_uid = uid or str(uuid.uuid4())
    now = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//ADK Meeting Scheduler//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "BEGIN:VEVENT",
        f"UID:{event_uid}",
        f"DTSTAMP:{now}",
        f"DTSTART:{fmt(dt_start)}",
        f"DTEND:{fmt(dt_end)}",
        f"SUMMARY:{summary}",
    ]
    if location:
        lines.append(f"LOCATION:{location}")
    if description:
        # rudimentary escaping
        safe_desc = description.replace("\n", "\\n").replace(",", "\\,")
        lines.append(f"DESCRIPTION:{safe_desc}")
    if organizer:
        lines.append(f"ORGANIZER:MAILTO:{organizer}")
    if attendees:
        for a in attendees:
            lines.append(f"ATTENDEE:MAILTO:{a}")
    lines += [
        "END:VEVENT",
        "END:VCALENDAR",
        "",
    ]
    ics_text = "\r\n".join(lines)
    return {
        "status": "ok",
        "summary": summary,
        "start": start_iso,
        "end": end_iso,
        "ics": ics_text,
        "uid": event_uid,
    }
