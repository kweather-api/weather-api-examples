# KWeather Weather API — Examples

Ready-to-run examples for the [KWeather Weather API](https://api.kweather.co.kr): Korean weather at the
**neighborhood (eup·myeon·dong) level** — current conditions, forecasts, fine dust and weather warnings —
plus world city weather and point forecasts from numerical models (GFS, ECMWF IFS, KIM).

[한국어](README.md)

- **Query by name or coordinates** — no KMA grid (nx, ny) conversion. Call with `q=청운효자동` or `lat=37.57&lon=126.98`.
- **Everything now, in one response** — temperature, wind, precipitation, fine dust, warnings and the change since yesterday.
- **Use it from AI tools** — an MCP server lets Claude, Cursor and other AI tools find and call the weather data ([mcp/](mcp/)).

## Getting started

1. Sign up at [api.kweather.co.kr](https://api.kweather.co.kr) — your API key is issued immediately.
   Every product on sale can be called **up to 20 times a month without a subscription**.
2. Put the key in an environment variable. Do not hard-code it.

   ```bash
   export KWEATHER_API_KEY="your_api_key"     # Windows PowerShell: $env:KWEATHER_API_KEY="your_api_key"
   ```

3. First call

   ```bash
   curl -H "Kweather-Api-Key: $KWEATHER_API_KEY" "https://apigw.kweather.co.kr/kw-current?lat=37.57&lon=126.98"
   curl -H "Kweather-Api-Key: $KWEATHER_API_KEY" "https://apigw.kweather.co.kr/kw-world-10d?q=Tokyo"
   ```

## Examples

| Folder | What's inside |
|---|---|
| [curl/](curl/) | One-line calls per product, three ways to pick a location |
| [python/](python/) | First call, name/coordinates, fine dust, 10-day forecast, warning alerts, world weather, model forecasts, error handling |
| [javascript/](javascript/) | Node.js 18+ (`fetch`, no dependencies) |
| [google-sheets/](google-sheets/) | Sheet functions `=KW_NOW()` and `=KW_DAILY()` (Apps Script) |
| [n8n/](n8n/) | A morning rain-alert workflow |
| [mcp/](mcp/) | Connect the weather MCP server to Claude Code, Claude Desktop and Cursor |

## Basics

- Base URL: `https://apigw.kweather.co.kr/<product>`
- Auth header: `Kweather-Api-Key: <your key>`
- Picking a location (Korean products)
  - Administrative dong code in the path: `/kw-current/1111051500`
  - Name: `?q=청운효자동` (Korean). If several places share the name you get `409` with a list of candidates.
  - Coordinates: `?lat=37.57&lon=126.98` (nearest administrative area)
- `error: "0"` means success. When you call by name or coordinates, `location` tells you which place was matched.

## Popular products

| Product | Description |
|---|---|
| `kw-current` | Korea, current conditions — temperature, wind, precipitation, fine dust, warnings, vs. yesterday |
| `kw-10d` | Korea, 10-day forecast — hourly, 3-hourly, daily |
| `kw-dust-r1` | Fine dust now (PM10, PM2.5, grades) |
| `kw-warning1` | Weather warnings |
| `kw-world-10d` | World cities — now and 10 days (`?q=Tokyo`) |
| `kw-point-gfs` · `kw-point-ifs` · `kw-point-g512` | Point forecast from GFS · ECMWF IFS · KIM |

All products and response fields: [API reference](https://api.kweather.co.kr/data) (Korean).

## Errors

| Status | Meaning |
|---|---|
| 401 | Missing or wrong key, or no subscription/trial for that product |
| 404 | Wrong product path (plain-text body), or no place matches the name/coordinates (`error: "005"`) |
| 409 | Ambiguous name — call again with one candidate's `hcode` |
| 429 | Trial calls used up, or too many calls in a short time |

## License

The example code in this repository is [MIT](LICENSE). Use of the weather data is subject to the [terms of service](https://api.kweather.co.kr/terms).
