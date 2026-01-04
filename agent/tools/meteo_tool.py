import requests

def get_weather_tool(city: str, date: str) -> dict:
    try:
        geo = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city, "count": 1, "language": "fr", "format": "json"},
            timeout=15,
        ).json()
    except Exception as err:
        return {"status": "error", "message": f"Erreur géocoding: {err}"}

    if not geo.get("results"):
        return {"status": "error", "message": f"Ville introuvable: {city}"}

    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]

    try:
        meteo = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
                "timezone": "Africa/Casablanca",
            },
            timeout=15,
        ).json()
    except Exception as err:
        return {"status": "error", "message": f"Erreur forecast: {err}"}

    days = meteo.get("daily", {}).get("time", [])
    if date not in days:
        return {"status": "error", "message": f"Date non dispo dans la prévision: {date}"}

    i = days.index(date)
    daily = meteo["daily"]
    return {
        "status": "ok",
        "city": city,
        "date": date,
        "tmax": daily["temperature_2m_max"][i],
        "tmin": daily["temperature_2m_min"][i],
        "precip_mm": daily["precipitation_sum"][i],
    }
