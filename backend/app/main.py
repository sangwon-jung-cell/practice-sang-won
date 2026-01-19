from fastapi import FastAPI
from backend.app.db.database import Base, engine
from backend.app.routers import posts, upload, weather, login
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.app.models import users, imagesmodel, postmodel

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
app.include_router(upload.router, prefix="/upload", tags=["upload"])
app.include_router(weather.router, prefix="/weather", tags=["weather"])
app.include_router(login.router, prefix="/login", tags=["login"])

app.mount("/static", StaticFiles(directory="backend/static"), name="static")

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}