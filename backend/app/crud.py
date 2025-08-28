from sqlalchemy.orm import Session
from app import models, schemas

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Post).order_by(models.Post.id.desc()).offset(skip).limit(limit).all()

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(title=post.title, content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post