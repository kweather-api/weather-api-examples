# 케이웨더 날씨 MCP 서버 / KWeather Weather MCP Server

AI 도구(Claude · Cursor · VS Code …)가 한국 읍·면·동 날씨와 세계 도시 날씨를 직접 찾아 부르게 하는 원격 MCP 서버입니다.
Remote MCP server that lets AI tools look up Korean neighborhood-level weather, fine dust, warnings, world city weather and numerical-model point forecasts.

- 주소 / URL: `https://apigw.kweather.co.kr/kw-mcp` (Streamable HTTP)
- 인증 / Auth: 헤더 `Kweather-Api-Key: <API 키>` (또는 `Authorization: Bearer <API 키>`)
- 키 / Key: [api.kweather.co.kr](https://api.kweather.co.kr) 가입 즉시 발급 — 상품마다 월 20회 무료 체험 / issued on sign-up, 20 free calls per product per month

## 도구 / Tools

| 도구 | 하는 일 | What it does | 호출 수 / Counted |
|---|---|---|---|
| `search_region` | 국내 지역 이름 → 행정 코드 | Korean place name → region code | 아니요 / no |
| `search_city` | 세계 도시 이름 → 도시 코드 | World city name → city code | 아니요 / no |
| `list_products` | 부를 수 있는 상품 | Available products | 아니요 / no |
| `describe_product` | 입력 · 응답 필드 뜻 · 단위 | Fields and units | 아니요 / no |
| `get_data` | 상품 API 한 번 (실황 · 예보 · 미세먼지 · 특보 …) | Call one product | 예 (성공만) / yes, on success |
| `get_point_forecast` | 좌표 한 점 수치 모델 예보 | Point forecast from a model | 예 (성공만) / yes, on success |

데이터 조회는 내 API 키의 구독 · 체험 한도 안에서 사이트에서 부르는 것과 똑같이 셉니다.
Data calls are metered against your key exactly like direct API calls.

## 연결 / Setup

### Claude Code

```bash
claude mcp add --transport http kweather https://apigw.kweather.co.kr/kw-mcp \
  --header "Kweather-Api-Key: 내_API_키"
```

### Cursor (`~/.cursor/mcp.json`)

```json
{
  "mcpServers": {
    "kweather": {
      "url": "https://apigw.kweather.co.kr/kw-mcp",
      "headers": { "Kweather-Api-Key": "내_API_키" }
    }
  }
}
```

### VS Code (`.vscode/mcp.json`) — 키를 파일에 적지 않고 처음 한 번 물어봅니다 / prompts for the key once

```json
{
  "inputs": [
    { "type": "promptString", "id": "kweather-key", "description": "KWeather API key", "password": true }
  ],
  "servers": {
    "kweather": {
      "type": "http",
      "url": "https://apigw.kweather.co.kr/kw-mcp",
      "headers": { "Kweather-Api-Key": "${input:kweather-key}" }
    }
  }
}
```

### Claude Desktop (`claude_desktop_config.json`, [mcp-remote](https://www.npmjs.com/package/mcp-remote) 사용 / via mcp-remote)

```json
{
  "mcpServers": {
    "kweather": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://apigw.kweather.co.kr/kw-mcp",
               "--header", "Kweather-Api-Key:${KWEATHER_API_KEY}"],
      "env": { "KWEATHER_API_KEY": "내_API_키" }
    }
  }
}
```

## 이렇게 물어보세요 / Try asking

- 「서울 구로3동 지금 날씨랑 미세먼지 알려줘」
- 「이번 주말 부산 해운대에 비 와?」
- 「도쿄 10일 예보를 표로 정리해줘」
- "What's the fine dust level in Jongno-gu, Seoul right now?"
- "Compare tomorrow's max temperature in Seoul from GFS, ECMWF IFS and KIM."

자세한 안내 / Guide: [날씨 MCP 가이드](https://api.kweather.co.kr/guides/weather-mcp)
