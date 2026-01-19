FROM python:3.12-slim
# 최상위 루트를 작업 디렉토리로 잡습니다
WORKDIR /

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. [중요] 현재 폴더의 모든 소스 코드를 컨테이너의 /backend 폴더로 복사
COPY . /backend

# [수정] 최상위 경로(/)를 PYTHONPATH에 추가하여 파이썬이 'backend' 패키지를 찾을 수 있게 합니다.
ENV PYTHONPATH=/


CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]