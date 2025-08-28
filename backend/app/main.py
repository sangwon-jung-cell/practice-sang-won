from fastapi import FastAPI
from app.routers import posts
from app.database import Base, engine
from app.routers import posts
from fastapi.middleware.cors import CORSMiddleware

# DB 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 프론트엔드 도메인 허용 (개발용)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

app.include_router(posts.router, prefix="/posts", tags=["posts"])

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}