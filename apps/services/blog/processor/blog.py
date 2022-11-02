"""_summary_

Raises:
    HTTPException: _description_
    HTTPException: _description_
    HTTPException: _description_
    HTTPException: _description_

Returns:
    _type_: _description_
"""
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from apps.services.blog import models, schemas
from apps.services.blog.constants.messages import BLOG_ADDED


def get_all(db: Session):
    """_summary_

    Args:
        db (Session): _description_

    Returns:
        _type_: _description_
    """
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.BlogCreate, db: Session, user: schemas.TokenData):
    """_summary_

    Args:
        request (schemas.BlogCreate): _description_
        db (Session): _description_
        user (schemas.TokenData): _description_

    Returns:
        _type_: _description_
    """
    new_blog = models.Blog(title=request.title, body=request.blog_body, user_id=user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"details": BLOG_ADDED}


def get(blog_id: int, db: Session):
    """_summary_

    Args:
        id (int): _description_
        db (Session): _description_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    blog = db.query(models.Blog).get(blog_id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found"
        )
    return blog


def delete(blog_id: int, db: Session):
    """_summary_

    Args:
        id (int): _description_
        db (Session): _description_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found"
        )
    blog.delete(synchronize_session=False)

    db.commit()

    return {"details": "Blog deleted"}


def update(blog_id: int, request: schemas.Blog, db: Session):
    """_summary_

    Args:
        id (int): _description_
        request (schemas.Blog): _description_
        db (Session): _description_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found"
        )
    blog.update(request.dict(), synchronize_session=False)

    db.commit()

    return {"details": "Blog updated"}


def partial_update(blog_id: int, request: schemas.Blog, db: Session):
    """_summary_

    Args:
        id (int): _description_
        request (schemas.Blog): _description_
        db (Session): _description_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    updated_request = request.dict(exclude_unset=True)
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found"
        )
    blog.update(updated_request)
    db.commit()

    return {"details": "Blog updated"}
