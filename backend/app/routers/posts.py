from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, models, schemas, database
from fastapi import Query

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_posts(db, skip = skip, limit = limit)

@router.post("/")
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db, post)