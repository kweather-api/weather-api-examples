# 파이썬 예제

```bash
pip install -r requirements.txt
export KWEATHER_API_KEY="내_API_키"      # PowerShell: $env:KWEATHER_API_KEY="내_API_키"

python 01_first_call.py 청운효자동
python 02_by_location.py                 # 코드 · 이름 · 좌표 · 같은 이름(409) 고르기
python 03_fine_dust.py 1111051500
python 04_10day_forecast.py 1111051500
python 05_warning_alert.py
python 06_world_weather.py Tokyo
python 07_model_point_forecast.py 37.57 126.98
```

[`kweather.py`](kweather.py) 가 키 읽기 · 재시도(429 · 5xx) · 오류를 맡습니다. 내 코드에 그대로 가져가 써도 됩니다.

상품마다 월 20회까지는 구독 없이 부를 수 있습니다. `02_by_location.py` 는 한 번에 5번 부릅니다.
