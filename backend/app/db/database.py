from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pathlib import Path
import os

# Docker 환경인지 확인 (Docker는 보통 루트에 .dockerenv 파일이 있음)
IS_DOCKER = os.path.exists('/.dockerenv')

if IS_DOCKER:
    # Docker 컨테이너 내부 경로
    DB_PATH = Path("/backend/db_data/test.db")
else:
    # 로컬 개발 환경 (현재 폴더의 local_db_data 사용)
    # 현재 파일(database.py) 위치를 기준으로 프로젝트 루트의 폴더를 가리킴
    BASE_DIR = Path(__file__).resolve().parents[3] # bp/ 폴더 위치
    DB_PATH = BASE_DIR / "backend" / "local_db_data" / "test.db"

# 폴더 생성 시도
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()