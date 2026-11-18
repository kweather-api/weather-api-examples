# curl 예제

[`examples.sh`](examples.sh) 에 상품별 한 줄 호출이 있습니다. 필요한 줄만 골라 실행하세요.

```bash
export KWEATHER_API_KEY="내_API_키"
curl -sG -H "Kweather-Api-Key: $KWEATHER_API_KEY" "https://apigw.kweather.co.kr/kw-current" --data-urlencode "q=청운효자동"
```

- 한글 이름은 `-G --data-urlencode "q=…"` 로 보내세요. **Windows 의 한글 명령창에서 주소에 한글을 그대로 넣으면**
  CP949 로 전송돼 `404 · error "005"`(찾지 못함)가 납니다.
- 응답을 보기 좋게: `| python -m json.tool` 또는 `| jq`.
