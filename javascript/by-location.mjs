// 지역을 고르는 세 가지 방법 — 코드 · 이름 · 좌표. 같은 이름이 여러 곳이면(409) 후보에서 고릅니다.
//   node by-location.mjs
import { KweatherError, call, place } from "./kweather.mjs";

function show(label, body) {
  const [code, d] = place(body);
  const loc = body.location ?? {};
  console.log(`${label.padEnd(10)} → ${loc.name ?? code}(${code}, ${loc.resolved?.by ?? "hcode"}) ${d.values.temperature}℃`);
}

show("코드", await call("kw-current/1153054000")); // 구로제3동
show("이름", await call("kw-current", { q: "서울 구로구 구로3동" }));
show("좌표", await call("kw-current", { lat: 37.49, lon: 126.89 }));

try {
  await call("kw-current", { q: "신사동" });
} catch (e) {
  if (!(e instanceof KweatherError) || e.status !== 409) throw e;
  console.log("신사동 후보:", e.candidates.map((c) => c.name).join(", "));
  show("후보 첫 번째", await call("kw-current", { hcode: e.candidates[0].hcode }));
}
