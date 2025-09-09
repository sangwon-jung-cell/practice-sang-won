from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from backend.app.api import post_crud
from backend.app.models import postmodel
from backend.app.schemas import boardschemas
from backend.app.db import database
from fastapi import Query
import shutil

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return post_crud.get_posts(db, skip = skip, limit = limit)

@router.post("/")
def create_post(post: boardschemas.PostCreate, db: Session = Depends(get_db)):
    return post_crud.create_post(db, post)

