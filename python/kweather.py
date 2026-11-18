"""케이웨더 날씨 API 를 부르는 작은 도우미 — 예제들이 함께 씁니다.

    from kweather import call
    body = call("kw-current", q="청운효자동")

- 키는 환경변수 KWEATHER_API_KEY 에서 읽습니다.
- 429(호출이 몰림) · 5xx 는 1 · 2 · 4초 쉬고 다시 부릅니다.
- 실패하면 KweatherError 를 냅니다. 409(같은 이름이 여러 곳)는 후보를 .candidates 로 줍니다.
"""
from __future__ import annotations

import os
import time

import requests

GW = "https://apigw.kweather.co.kr"


class KweatherError(RuntimeError):
    def __init__(self, status: int, code: str | None, message: str, candidates: list | None = None):
        super().__init__(f"{status} {code or ''} {message}".strip())
        self.status, self.code, self.candidates = status, code, candidates or []


def api_key() -> str:
    key = os.environ.get("KWEATHER_API_KEY", "").strip()   # 앞뒤 공백이 있으면 401 이 납니다
    if not key:
        raise SystemExit("환경변수 KWEATHER_API_KEY 에 API 키를 넣어 주세요.")
    return key


def call(path: str, timeout: float = 15, **params) -> dict:
    """상품 한 번 부르기. path 예: "kw-current", "kw-current/1111051500"."""
    for attempt in range(4):
        r = requests.get(f"{GW}/{path}", params=params or None,
                         headers={"Kweather-Api-Key": api_key()}, timeout=timeout)
        if r.status_code in (429, 500, 502, 503, 504) and attempt < 3:
            time.sleep(2 ** attempt)
            continue
        try:
            body = r.json()
        except ValueError:                      # 상품 주소가 틀린 404 는 JSON 이 아닙니다
            raise KweatherError(r.status_code, None, r.text[:120])
        if r.status_code == 409:
            raise KweatherError(409, body.get("error"), body.get("message", ""), body.get("data"))
        if r.status_code != 200 or body.get("error", "0") != "0":
            raise KweatherError(r.status_code, body.get("error"), str(body.get("message", "")))
        return body
    raise KweatherError(r.status_code, None, "다시 시도해도 실패했습니다")


def place(body: dict) -> tuple[str, dict]:
    """국내 상품 응답에서 (행정동 코드, 그곳의 data). 이름 · 좌표로 불렀으면 location 의 코드를 씁니다."""
    code = (body.get("location") or {}).get("hcode") or next(iter(body["data"]))
    return code, body["data"][code]["data"]
