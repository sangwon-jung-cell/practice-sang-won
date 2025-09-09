# Python 3.12이 설치된 가벼운 리눅스 이미지에서 시작
FROM python:3.12-slim

# 컨테이너 안 작업 디렉토리 생성
WORKDIR /app

# requirements.txt 복사 후 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 전체 복사
COPY . .

# FastAPI 앱 실행
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
