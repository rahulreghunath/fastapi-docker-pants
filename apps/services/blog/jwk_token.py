"""_summary_

Raises:
    credentials_exception: _description_
    HTTPException: _description_
    credentials_exception: _description_

Returns:
    _type_: _description_
"""
from datetime import datetime, timedelta

from fastapi import HTTPException, status
from fastapi.security import SecurityScopes
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from apps.services.blog import models
from apps.services.blog.constants.messages import UNAUTHORIZED_REQUEST
from apps.services.blog.schemas import TokenData

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 150


def create_access_token(data: dict):
    """_summary_

    Args:
        data (dict): _description_

    Returns:
        _type_: _description_
    """
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_token(
    token: str, security_scopes: SecurityScopes, credentials_exception, db: Session
):
    """_summary_

    Args:
        token (str): _description_
        security_scopes (SecurityScopes): _description_
        credentials_exception (_type_): _description_
        db (Session): _description_

    Raises:
        credentials_exception: _description_
        HTTPException: _description_
        credentials_exception: _description_

    Returns:
        _type_: _description_
    """
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("user")
        token_scopes = payload.get("scopes", [])
        user = db.query(models.User).filter(models.User.email == username).first()

        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=UNAUTHORIZED_REQUEST,
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return TokenData(id=user.id, scopes=token_scopes)
    except JWTError as e:
        raise credentials_exception from e
