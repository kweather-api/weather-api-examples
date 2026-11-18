// 구글 시트에서 케이웨더 날씨 API 를 함수로 — =KW_NOW("1111051500") · =KW_DAILY("1111051500")
// 설정: 확장 프로그램 → Apps Script → 이 파일 붙여넣기 → 프로젝트 설정 → 스크립트 속성에 KWEATHER_API_KEY 추가.
// 같은 호출은 10분 동안 캐시해 호출 수를 아낍니다.

const GW = "https://apigw.kweather.co.kr";

function kw_(path) {
  const cache = CacheService.getScriptCache();
  const hit = cache.get(path);
  if (hit) return JSON.parse(hit);
  const key = PropertiesService.getScriptProperties().getProperty("KWEATHER_API_KEY");
  if (!key) throw new Error("스크립트 속성에 KWEATHER_API_KEY 를 넣어 주세요.");
  let res;
  for (let i = 0; i < 4; i++) {                 // 초당 한도(429)면 잠깐 쉬고 다시
    res = UrlFetchApp.fetch(GW + "/" + path, {
      headers: { "Kweather-Api-Key": key.trim() },
      muteHttpExceptions: true,
    });
    if (res.getResponseCode() !== 429) break;
    Utilities.sleep(1100);
  }
  const body = JSON.parse(res.getContentText());
  if (body.error !== "0") throw new Error(res.getResponseCode() + " " + body.message);
  cache.put(path, JSON.stringify(body), 600);
  return body;
}

/**
 * 지금 날씨 한 칸.
 * @param {string} code 행정동 코드 (예: "1111051500")
 * @param {string} field temperature · humidity · windSpeed · weatherText … (기본 temperature)
 * @customfunction
 */
function KW_NOW(code, field) {
  const body = kw_("kw-current/" + code);
  return body.data[code].data.values[field || "temperature"];
}

/**
 * 10일 최저 · 최고 표.
 * @param {string} code 행정동 코드
 * @customfunction
 */
function KW_DAILY(code) {
  const body = kw_("kw-10d/" + code);
  const rows = body.data[code].data.daily.map((d) =>
    [d.date, d.values.temperatureMin, d.values.temperatureMax]);
  return [["날짜", "최저", "최고"], ...rows];
}
