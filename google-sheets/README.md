# 구글 시트 함수

1. 시트에서 **확장 프로그램 → Apps Script** 를 엽니다.
2. [`Code.gs`](Code.gs) 내용을 붙여 넣고 저장합니다.
3. 왼쪽 **프로젝트 설정(톱니) → 스크립트 속성 → 속성 추가**: 이름 `KWEATHER_API_KEY`, 값에 API 키.
4. 시트 칸에서 씁니다.

```
=KW_NOW("1111051500")                  지금 기온
=KW_NOW("1111051500", "weatherText")   지금 날씨 글자 (맑음 · 흐림 …)
=KW_DAILY("1111051500")                10일 최저 · 최고 표 (아래로 펼쳐짐)
```

- 행정동 코드는 [코드 찾기 가이드](https://api.kweather.co.kr/guides/call-weather-by-dong-code) 에서 찾습니다.
- 같은 호출은 10분 동안 캐시합니다. 시트를 다시 계산해도 그 사이에는 호출 수가 늘지 않습니다.
- 엑셀(파워 쿼리) 예제는 [시트 · 엑셀 가이드](https://api.kweather.co.kr/guides/weather-api-google-sheets-excel) 에 있습니다.
