"""세계 도시 날씨 — 도시 이름(한글 · 영문)이나 좌표로 지금과 10일.

    python 06_world_weather.py Tokyo
"""
import sys

from kweather import call

city = sys.argv[1] if len(sys.argv) > 1 else "Tokyo"
body = call("kw-world-10d", q=city)
loc, d = body["location"], body["data"]["data"]
now = d.get("current")
print(f"{loc['name']}({loc['country']}) 지금", f"{now['values']['temperature']}℃ {now['values']['weatherText']}" if now else "실황 없음")
for day in d["timelines"]["daily"]:
    v = day["values"]
    print(f"  {day['date']} {v['temperatureMin']}~{v['temperatureMax']}℃ 비 {v['precipitationProbabilityMax']}%")
