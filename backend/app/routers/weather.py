from fastapi import APIRouter, HTTPException
import httpx # 외부 API 호출을 위한 라이브러리

router = APIRouter()

# 실제로는 환경 변수에 저장하는 것이 좋습니다.
API_KEY = "5d88d6a2b12722c05e25f135c492cb0b"

router.get("/weather")
async def get_weather(city: str):
    # 외부 날씨 API 호출
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="날씨 정보를 가져오는 데 실패했습니다.")