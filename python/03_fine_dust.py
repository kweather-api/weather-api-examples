"""미세먼지 실황 — PM10 · PM2.5 와 등급.

    python 03_fine_dust.py 1111051500
"""
import sys

from kweather import call

GRADE = {1: "좋음", 2: "보통", 3: "나쁨", 4: "매우나쁨"}

code = sys.argv[1] if len(sys.argv) > 1 else "1111051500"
d = call(f"kw-dust-r1/{code}")["data"][code]["data"]
where = " ".join(x for x in (d["state"], d["city"], d["city2"]) if x)
print(f"{where} 미세먼지 {d['pm10']}㎍/㎥({GRADE.get(d['pm10MeGrade'], '-')}) · "
      f"초미세먼지 {d['pm25']}㎍/㎥({GRADE.get(d['pm25MeGrade'], '-')})")
