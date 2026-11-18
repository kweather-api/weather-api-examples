"""수치 모델 좌표 예보 — 같은 지점의 내일 최고기온을 모델끼리 비교.

    python 07_model_point_forecast.py 37.57 126.98
"""
import sys
from datetime import date, timedelta

from kweather import KweatherError, call

lat, lon = (float(sys.argv[1]), float(sys.argv[2])) if len(sys.argv) > 2 else (37.57, 126.98)
tomorrow = (date.today() + timedelta(days=1)).isoformat()

for model in ("gfs", "g512", "ifs"):           # GFS · KIM · ECMWF IFS
    try:
        d = call(f"kw-point-{model}", lat=lat, lon=lon, timeout=30)["data"]
    except KweatherError as e:
        print(f"{model:<5} — {e}")
        continue
    steps = [s for tl in d["timelines"].values() for s in tl]
    temps = [s["values"]["temperature"] for s in steps if s["time"].startswith(tomorrow)]
    best = f"{max(temps):.1f}℃" if temps else "자료 없음"
    print(f"{d['modelName']:<20} 내일 최고 {best}  (사이클 {d['issuedAt'][:13]})")
