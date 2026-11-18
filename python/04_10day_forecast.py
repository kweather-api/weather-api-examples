"""10일 예보 — 일별 최저 · 최고와 다음 비 소식.

    python 04_10day_forecast.py 1111051500

- daily 는 오후가 되면 오늘 칸이 빠지고 내일부터 올 수 있습니다. 오늘 값이 필요하면 hourly 에서 구하세요.
- 예보가 아직 채워지지 않은 날은 값이 null(None)로 올 수 있습니다.
"""
import sys

from kweather import call

code = sys.argv[1] if len(sys.argv) > 1 else "1111051500"
d = call(f"kw-10d/{code}")["data"][code]["data"]

for day in d["daily"]:
    v = day["values"]
    lo, hi = v.get("temperatureMin"), v.get("temperatureMax")
    print(day["date"], f"{lo} ~ {hi} ℃" if lo is not None and hi is not None else "자료 없음")

steps = d["timelines"]["hourly"] + d["timelines"]["threeHourly"]
rain = next((s for s in steps if (s["values"]["precipitation"] or 0) > 0), None)
print("다음 비:", rain["time"] if rain else "10일 안에 없음")
