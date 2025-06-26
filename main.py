from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo  # Importamos ZoneInfo correctamente

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, python fast api!"}

country_timezones = {
    "US": "America/New_York",
    "CA": "America/Toronto",
    "GB": "Europe/London",
    "FR": "Europe/Paris",
    "DE": "Europe/Berlin",
    "JP": "Asia/Tokyo",
    "BR": "America/Sao_Paulo",
    "MX": "America/Mexico_City",
    "CO": "America/Bogota",
    "AR": "America/Argentina/Buenos_Aires"
}

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso_code = iso_code.upper()
    timezone_str = country_timezones.get(iso_code, "UTC")
    tz = ZoneInfo(timezone_str)
    return {"time": datetime.now(tz)}
