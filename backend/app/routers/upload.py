from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
import shutil
from backend.app.models import imagesmodel
from backend.app.db import database
from backend.app.schemas.images_schemas import ImageResponse

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    save_path = f"backend/static/images/{file.filename}"
    with open(save_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    image = imagesmodel.Post(
        file_name=file.filename,
        file_path=f"static/images/{file.filename}",
    )
    db.add(image)
    db.commit()
    db.refresh(image)

    return image

@router.get("/", response_model=list[ImageResponse])
def get_images(db: Session = Depends(get_db)):
    return db.query(imagesmodel.Post).all()