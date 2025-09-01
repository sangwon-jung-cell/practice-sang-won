from fastapi import APIRouter, Depends, UploadFile, File
import shutil

router = APIRouter()

@router.post("/")
async def upload_image(file: UploadFile = File(...)):
    file_path = f"static/images/{file.filename}"
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"image_url": file_path}