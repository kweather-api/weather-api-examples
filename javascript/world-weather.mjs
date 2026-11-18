// 세계 도시 날씨 — 도시 이름(한글 · 영문)으로 지금과 10일.   node world-weather.mjs Tokyo
import { call } from "./kweather.mjs";

const city = process.argv[2] ?? "Tokyo";
const body = await call("kw-world-10d", { q: city });
const { current, timelines } = body.data.data;
const now = current ? `${current.values.temperature}℃ ${current.values.weatherText}` : "실황 없음";
console.log(`${body.location.name}(${body.location.country}) 지금 ${now}`);
for (const d of timelines.daily) {
  console.log(`  ${d.date} ${d.values.temperatureMin}~${d.values.temperatureMax}℃ 비 ${d.values.precipitationProbabilityMax}%`);
}
