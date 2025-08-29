from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    image_url = Column(String(300), nullable=True)  # 이미지 경로/URL