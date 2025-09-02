from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
import shutil
from app.models import imagesmodel
from app.db import database
from app.schemas.images_schemas import ImageResponse

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = f"static/images/{file.filename}"
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    image = imagesmodel.Post(
        file_name=file.filename,
        file_path=file_path,
    )
    db.add(image)
    db.commit()
    db.refresh(image)

    return image

@router.get("/", response_model=list[ImageResponse])
def get_images(db: Session = Depends(get_db)):
    return db.query(imagesmodel.Post).all()