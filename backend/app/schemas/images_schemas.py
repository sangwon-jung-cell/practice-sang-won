# schemas/image.py
from pydantic import BaseModel
from datetime import datetime

class ImageResponse(BaseModel):
    id: int
    file_name: str
    file_path: str
    created_at: datetime

    class Config:
        from_attributes = True 