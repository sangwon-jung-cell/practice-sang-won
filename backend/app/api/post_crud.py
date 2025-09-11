from sqlalchemy.orm import Session
from backend.app.models import postmodel, imagesmodel
from backend.app.schemas import boardschemas, images_schemas

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    rows = (
        db.query(postmodel.Post)
        .order_by(postmodel.Post.id.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    return [
        {"id": r.id, "title": r.title, "content": r.content, "created_at" : r.created_at}
        for r in rows
    ]

def create_post(db: Session, post: boardschemas.PostCreate):
    db_post = postmodel.Post(title=post.title, content=post.content, created_at = post.created_at)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
