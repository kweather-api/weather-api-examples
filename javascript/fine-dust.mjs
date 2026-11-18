// 미세먼지 실황 — PM10 · PM2.5 와 등급.   node fine-dust.mjs 1111051500
import { call } from "./kweather.mjs";

const GRADE = { 1: "좋음", 2: "보통", 3: "나쁨", 4: "매우나쁨" };

const code = process.argv[2] ?? "1111051500";
const d = (await call(`kw-dust-r1/${code}`)).data[code].data;
const where = [d.state, d.city, d.city2].filter(Boolean).join(" ");
console.log(`${where} 미세먼지 ${d.pm10}㎍/㎥(${GRADE[d.pm10MeGrade] ?? "-"}) · 초미세먼지 ${d.pm25}㎍/㎥(${GRADE[d.pm25MeGrade] ?? "-"})`);
