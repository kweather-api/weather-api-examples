"""지역을 고르는 세 가지 방법 — 행정동 코드 · 이름 · 좌표. 같은 이름이 여러 곳이면(409) 후보에서 고릅니다.

    python 02_by_location.py
"""
from kweather import KweatherError, call, place


def show(label: str, body: dict) -> None:
    code, d = place(body)
    loc = body.get("location") or {}
    how = (loc.get("resolved") or {}).get("by", "hcode")
    print(f"{label:<12} → {loc.get('name', code)}({code}, {how}) {d['values']['temperature']}℃")


show("코드", call("kw-current/1153054000"))                    # 구로제3동
show("이름", call("kw-current", q="서울 구로구 구로3동"))
show("좌표", call("kw-current", lat=37.49, lon=126.89))         # 가장 가까운 행정구역

# 같은 이름이 여러 곳 — 409 와 후보 목록이 옵니다. 화면에서는 사용자에게 고르게 하세요.
try:
    call("kw-current", q="신사동")
except KweatherError as e:
    if e.status != 409:
        raise
    print("신사동 후보:", ", ".join(c["name"] for c in e.candidates))
    show("후보 첫 번째", call("kw-current", hcode=e.candidates[0]["hcode"]))
