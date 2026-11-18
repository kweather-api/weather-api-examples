# 케이웨더 날씨 API 예제

[케이웨더 날씨 API](https://api.kweather.co.kr) 를 바로 불러 볼 수 있는 예제 모음입니다.
한국 **읍·면·동 단위** 실황 · 예보 · 미세먼지 · 기상특보와 세계 도시 날씨, 좌표 한 점 수치 모델 예보를 다룹니다.

[English](README.en.md)

- **동 이름 · 좌표로 바로 조회** — 기상청 격자(nx, ny) 변환 없이 `q=청운효자동` 이나 `lat=37.57&lon=126.98` 로 부릅니다.
- **실황 한 번에** — 기온 · 바람 · 강수 · 미세먼지 · 특보 · 어제와 비교가 한 응답에 옵니다.
- **AI 도구에서 바로** — MCP 서버로 Claude · Cursor 같은 AI 도구가 날씨를 직접 찾아 부릅니다([mcp/](mcp/)).

## 시작하기

1. [api.kweather.co.kr](https://api.kweather.co.kr) 에서 가입하면 그 자리에서 API 키가 나옵니다.
   판매 중인 상품은 상품마다 **월 20회까지 구독 없이** 불러 볼 수 있습니다.
2. 키를 환경변수에 넣습니다. 코드에 직접 적지 마세요.

   ```bash
   export KWEATHER_API_KEY="내_API_키"        # Windows PowerShell: $env:KWEATHER_API_KEY="내_API_키"
   ```

3. 첫 호출

   ```bash
   curl -G -H "Kweather-Api-Key: $KWEATHER_API_KEY" \
     "https://apigw.kweather.co.kr/kw-current" --data-urlencode "q=청운효자동"
   ```

## 예제

| 폴더 | 내용 |
|---|---|
| [curl/](curl/) | 상품별 한 줄 호출 · 지역을 고르는 세 가지 방법 |
| [python/](python/) | 첫 호출 · 동 이름/좌표 · 미세먼지 · 10일 예보 · 특보 알림 · 세계 날씨 · 수치 모델 · 오류 처리 |
| [javascript/](javascript/) | Node.js 18+ (`fetch`, 의존성 없음) — 첫 호출 · 미세먼지 · 세계 날씨 · 오류 처리 |
| [google-sheets/](google-sheets/) | 구글 시트 함수 `=KW_NOW()` · `=KW_DAILY()` (Apps Script) |
| [n8n/](n8n/) | 매일 아침 비 소식 만들기 워크플로 |
| [mcp/](mcp/) | Claude Code · Claude Desktop · Cursor 에 날씨 MCP 연결 |

## 기본 규칙

- 주소: `https://apigw.kweather.co.kr/<상품 코드>`
- 인증: 헤더 `Kweather-Api-Key: <API 키>`
- 지역 고르기 (국내 상품)
  - 행정동 코드를 경로에: `/kw-current/1111051500`
  - 이름: `?q=청운효자동` · `?q=서울 구로구 구로3동` (같은 이름이 여러 곳이면 `409` 와 후보 목록)
  - 좌표: `?lat=37.57&lon=126.98` (가장 가까운 행정구역)
- 응답: `error` 가 `"0"` 이면 성공입니다. 이름 · 좌표로 부르면 `location` 에 찾은 곳이 함께 옵니다.

  ```json
  {
    "error": "0",
    "location": { "hcode": "1111051500", "name": "청운효자동", "resolved": { "by": "name", "query": "청운효자동" } },
    "data": { "1111051500": { "data": { "values": { "temperature": 6.1, "weatherText": "맑음" } } } }
  }
  ```

## 자주 쓰는 상품

| 상품 코드 | 내용 |
|---|---|
| `kw-current` | 국내 실황 — 기온 · 바람 · 강수 · 미세먼지 · 특보 · 어제와 비교 |
| `kw-10d` | 국내 10일 예보 — 시간별 · 3시간별 · 일별 |
| `kw-dust-r1` | 미세먼지 실황(PM10 · PM2.5, 등급) |
| `kw-warning1` | 기상특보 |
| `kw-world-10d` | 세계 도시 실황 · 10일 예보 (`?q=Tokyo`, 한글 · 영문) |
| `kw-point-gfs` · `kw-point-ifs` · `kw-point-g512` | 좌표 한 점 수치 모델 예보 (GFS · ECMWF IFS · KIM) |

전체 상품과 응답 필드는 [API 문서](https://api.kweather.co.kr/data) 에 있습니다.

## 오류

| 상태 | 뜻 |
|---|---|
| 401 | 키가 없거나 틀림, 또는 구독도 체험도 없는 상품 |
| 404 | 상품 주소가 틀림(JSON 이 아닌 글자), 또는 이름 · 좌표에 맞는 곳이 없음(`error: "005"`) |
| 409 | 같은 이름이 여러 곳 — `data` 의 후보 중 하나의 `hcode` 로 다시 부릅니다 |
| 429 | 체험 20회를 다 썼거나, 짧은 시간에 너무 몰아 부름 |

자세한 대처는 [오류 해결 가이드](https://api.kweather.co.kr/guides/weather-api-errors) 를 보세요.

## 더 보기

- [날씨 API 연동 가이드](https://api.kweather.co.kr/guides) — 따라 하면 붙는 글 20편
- [기상청 날씨 API 를 더 쉽게](https://api.kweather.co.kr/guides/kma-weather-api-alternative)
- [요금](https://api.kweather.co.kr/pricing) · [문의](https://api.kweather.co.kr/contact)

## 라이선스

이 저장소의 예제 코드는 [MIT](LICENSE) 입니다. 날씨 데이터 이용은 [이용약관](https://api.kweather.co.kr/terms) 을 따릅니다.
