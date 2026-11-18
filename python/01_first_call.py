"""첫 호출 — 동 이름으로 지금 날씨.

    pip install -r requirements.txt
    python 01_first_call.py 청운효자동
"""
import sys

from kweather import call, place

name = sys.argv[1] if len(sys.argv) > 1 else "청운효자동"
body = call("kw-current", q=name)
code, d = place(body)
v = d["values"]
print(f"{body['location']['name']}({code}) {v['temperature']}℃ {v['weatherText']} · 습도 {v['humidity']}% · 바람 {v['windSpeed']}m/s")
