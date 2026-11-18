// 케이웨더 날씨 API 를 부르는 작은 도우미 — 예제들이 함께 씁니다. Node.js 18+ (내장 fetch).
//
//   import { call, place } from "./kweather.mjs";
//   const body = await call("kw-current", { q: "청운효자동" });
//
// - 키는 환경변수 KWEATHER_API_KEY 에서 읽습니다.
// - 429(호출이 몰림) · 5xx 는 1 · 2 · 4초 쉬고 다시 부릅니다.
// - 실패하면 KweatherError. 409(같은 이름이 여러 곳)는 후보를 .candidates 로 줍니다.

export const GW = "https://apigw.kweather.co.kr";

export class KweatherError extends Error {
  constructor(status, code, message, candidates = []) {
    super(`${status} ${code ?? ""} ${message}`.replace(/\s+/g, " ").trim());
    this.status = status;
    this.code = code;
    this.candidates = candidates;
  }
}

function apiKey() {
  const key = (process.env.KWEATHER_API_KEY ?? "").trim(); // 앞뒤 공백이 있으면 401 이 납니다
  if (!key) throw new Error("환경변수 KWEATHER_API_KEY 에 API 키를 넣어 주세요.");
  return key;
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

/** 상품 한 번 부르기. path 예: "kw-current", "kw-current/1111051500". */
export async function call(path, params = {}) {
  const url = new URL(`${GW}/${path}`);
  for (const [k, v] of Object.entries(params)) url.searchParams.set(k, String(v));
  let res;
  for (let attempt = 0; attempt < 4; attempt++) {
    res = await fetch(url, { headers: { "Kweather-Api-Key": apiKey() } });
    if ([429, 500, 502, 503, 504].includes(res.status) && attempt < 3) {
      await sleep(1000 * 2 ** attempt);
      continue;
    }
    break;
  }
  const text = await res.text();
  let body;
  try {
    body = JSON.parse(text);
  } catch {
    throw new KweatherError(res.status, null, text.slice(0, 120)); // 상품 주소가 틀린 404 는 JSON 이 아닙니다
  }
  if (res.status === 409) throw new KweatherError(409, body.error, body.message ?? "", body.data ?? []);
  if (res.status !== 200 || (body.error ?? "0") !== "0") {
    throw new KweatherError(res.status, body.error, String(body.message ?? ""));
  }
  return body;
}

/** 국내 상품 응답에서 [행정동 코드, 그곳의 data]. 이름 · 좌표로 불렀으면 location 의 코드를 씁니다. */
export function place(body) {
  const code = body.location?.hcode ?? Object.keys(body.data)[0];
  return [code, body.data[code].data];
}
