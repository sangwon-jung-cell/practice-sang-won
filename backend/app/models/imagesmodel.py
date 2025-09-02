from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from app.db.database import Base

class Post(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())