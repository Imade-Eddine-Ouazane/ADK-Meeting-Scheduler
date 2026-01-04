import re
from typing import Optional

def validate_contact(email: Optional[str] = None, phone: Optional[str] = None) -> dict:
    email_ok = bool(
        email and re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email)
    )
    phone_ok = bool(phone and re.fullmatch(r"\+?[0-9]{7,15}", phone))
    return {
        "email": email,
        "email_valid": email_ok,
        "phone": phone,
        "phone_valid": phone_ok,
        "status": "ok" if (email_ok or phone_ok) else "warn",
        "message": (
            "Valid coordinates" if (email_ok or phone_ok) else "Provide a valid email or phone."
        ),
    }
