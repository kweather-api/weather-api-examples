#!/usr/bin/env bash
# 케이웨더 날씨 API — curl 한 줄 예제.  KWEATHER_API_KEY 환경변수에 키를 넣고 필요한 줄만 골라 실행하세요.
# (한 줄이 1회 호출입니다. 상품마다 월 20회까지는 구독 없이 부를 수 있습니다.)
set -euo pipefail
GW="https://apigw.kweather.co.kr"
H="Kweather-Api-Key: ${KWEATHER_API_KEY:?KWEATHER_API_KEY 를 넣어 주세요}"

## 지역 고르기 — 세 가지
curl -sH "$H" "$GW/kw-current/1111051500"                                   # 1) 행정동 코드 (청운효자동)
curl -sG -H "$H" "$GW/kw-current" --data-urlencode "q=서울 구로구 구로3동"   # 2) 이름 (한글은 --data-urlencode 로)
curl -sH "$H" "$GW/kw-current?lat=37.49&lon=126.89"                         # 3) 좌표 (가장 가까운 행정구역)

## 상품
curl -sH "$H" "$GW/kw-10d/1111051500"            # 10일 예보 (시간별 · 3시간별 · 일별)
curl -sH "$H" "$GW/kw-dust-r1/1111051500"        # 미세먼지 실황
curl -sH "$H" "$GW/kw-warning1/1111051500"       # 기상특보 (걸린 특보가 없으면 206 · error "001")
curl -sH "$H" "$GW/kw-world-10d?q=Tokyo"         # 세계 도시 (한글 · 영문 이름, 또는 lat · lon)
curl -sH "$H" "$GW/kw-point-gfs?lat=37.57&lon=126.98"   # 수치 모델 좌표 예보 (gfs · ifs · g512 …)

## 행정동 코드표 (요금 없음 — 키는 필요합니다)
#   단위마다 상품이 다릅니다: 읍·면·동 kw-code-city2 · 시·군·구 kw-code-city · 광역 kw-code-state
curl -sH "$H" "$GW/kw-code-city2/1111051500"     # 코드 하나 (빼면 전체 목록)
