# JavaScript 예제 (Node.js 18+)

설치할 것이 없습니다(내장 `fetch`).

```bash
export KWEATHER_API_KEY="내_API_키"      # PowerShell: $env:KWEATHER_API_KEY="내_API_키"

node first-call.mjs 청운효자동
node by-location.mjs                     # 코드 · 이름 · 좌표 · 같은 이름(409) 고르기
node fine-dust.mjs 1111051500
node world-weather.mjs Tokyo
```

[`kweather.mjs`](kweather.mjs) 가 키 읽기 · 재시도(429 · 5xx) · 오류를 맡습니다.

**브라우저에서 바로 부르지 마세요.** 키가 화면 소스에 그대로 드러납니다. 내 서버가 대신 부르고, 서버에서 몇 분씩 캐시해
화면에 넘기는 것이 안전하고 호출 수도 아낍니다 — [웹사이트 날씨 위젯 가이드](https://api.kweather.co.kr/guides/website-weather-widget).
