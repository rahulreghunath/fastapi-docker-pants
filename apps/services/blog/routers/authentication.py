"""_summary_

Returns:
    _type_: _description_
"""
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from apps.services.blog import schemas
from apps.services.blog.database.database import get_db
from apps.services.blog.processor import authentication
from apps.services.blog.response_schemas import RESPONSE_401

router = APIRouter(tags=["authentication"])


@router.post(
    "/login",
    responses={
        status.HTTP_200_OK: {"model": schemas.Token, "description": "User"},
        status.HTTP_401_UNAUTHORIZED: RESPONSE_401,
    },
    response_model=schemas.Token,
)
def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    """_summary_

    Args:
        request (OAuth2PasswordRequestForm, optional): _description_.
            Defaults to Depends().
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        _type_: _description_
    """
    print("sdf")

    return authentication.authenfication(request, db)
