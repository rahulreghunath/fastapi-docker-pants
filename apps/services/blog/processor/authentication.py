"""_summary_

Raises:
    HTTPException: _description_
    HTTPException: _description_

Returns:
    _type_: _description_
"""
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from apps.services.blog import models
from apps.services.blog.jwk_token import create_access_token
from apps.shared.utils import Hash


def authenfication(request: OAuth2PasswordRequestForm, db: Session):
    """_summary_

    Args:
        request (OAuth2PasswordRequestForm): _description_
        db (Session): _description_

    Raises:
        HTTPException: _description_
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials"
        )
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password"
        )

    access_token = create_access_token(data={"user": user.email, "scopes": ["blogs"]})

    return {"access_token": access_token, "token_type": "bearer"}
