"""_summary_

Raises:
    HTTPException: _description_

Returns:
    _type_: _description_
"""
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from blog import models, schemas
from blog.constants.messages import USER_ADDED
from shared.utils import Hash


def create(request: schemas.User, db: Session):
    """_summary_

    Args:
        request (schemas.User): _description_
        db (Session): _description_

    Returns:
        _type_: _description_
    """
    new_user = models.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"details": USER_ADDED}


def get(user_id: int, db: Session):
    """_summary_

    Args:
        user_id (int): _description_
        db (Session): _description_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    user = db.query(models.User).get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found"
        )
    return user
