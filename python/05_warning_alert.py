"""기상특보 — 새로 발효된 특보만 골라 알리기. 5~10분마다 부르는 배치에 넣으세요.

    python 05_warning_alert.py
"""
from kweather import KweatherError, call

seen: set[tuple] = set()          # 이미 알린 특보 (지역, 이름, 발효 시각). 실제로는 DB 나 파일에 두세요.


def poll() -> list[str]:
    try:
        body = call("kw-warning1", timeout=30)
    except KweatherError as e:
        if e.code == "001":          # 걸린 특보가 하나도 없음
            return []
        raise
    new = []
    for code, row in body["data"].items():
        d = row["data"]
        where = " ".join(x for x in (d["state"], d["city"], d["city2"]) if x)
        for name, start, end in zip(d["warn"], d["startTime"], d["endTime"]):
            key = (code, name, start)
            if not end and key not in seen:
                seen.add(key)
                new.append(f"{where} {name} ({start[8:10]}:{start[10:12]} 발효)")
    return new


lines = poll()
print("\n".join(lines) if lines else "새로 발효된 특보 없음")   # 여기서 메신저 · 문자 발송으로 넘깁니다
