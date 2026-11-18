# n8n — 아침 비 소식

매일 07:00 에 10일 예보를 받아 「오늘 몇 시부터 비 소식」 문장을 만듭니다. 뒤에 Slack · 텔레그램 · 메일 노드를 붙여 보내세요.

1. n8n 에서 **Workflows → Import from File** 로 [`morning-rain-alert.json`](morning-rain-alert.json) 을 가져옵니다.
2. **케이웨더 10일 예보** 노드 → Credential → **Create new (Header Auth)**
   - Name: `Kweather-Api-Key`
   - Value: API 키
3. 지역을 바꾸려면 HTTP 주소의 행정동 코드와 **비 소식 문장** 노드 첫 줄의 `code` 를 같이 바꿉니다.
4. **Execute workflow** 로 한 번 돌려 보고, 켜(Active) 둡니다.

키는 워크플로 파일이 아니라 n8n 자격 증명에 들어가므로, 워크플로를 내보내거나 공유해도 키가 따라가지 않습니다.

Make · Zapier 는 「HTTP 요청」 모듈에 같은 주소와 헤더를 넣으면 됩니다 — [노코드 자동화 가이드](https://api.kweather.co.kr/guides/weather-api-no-code-automation).
