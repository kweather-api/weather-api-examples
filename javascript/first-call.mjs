// 첫 호출 — 동 이름으로 지금 날씨.   node first-call.mjs 청운효자동
import { call, place } from "./kweather.mjs";

const name = process.argv[2] ?? "청운효자동";
const body = await call("kw-current", { q: name });
const [code, d] = place(body);
const v = d.values;
console.log(`${body.location.name}(${code}) ${v.temperature}℃ ${v.weatherText} · 습도 ${v.humidity}% · 바람 ${v.windSpeed}m/s`);
