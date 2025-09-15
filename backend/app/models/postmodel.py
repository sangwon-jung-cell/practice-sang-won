from sqlalchemy import Column, DateTime, Integer, String, func
from backend.app.db.database import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    created_at = Column(DateTime(), server_default=func.now())