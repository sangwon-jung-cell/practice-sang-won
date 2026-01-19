from fastapi import APIRouter, Depends
from backend.app.db import database
from backend.app.schemas import user_schemas;
from sqlalchemy.orm import Session

router = APIRouter

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

#@router.post("/", response_model=user_schemas.User)
#def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    