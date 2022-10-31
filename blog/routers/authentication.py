"""_summary_

Returns:
    _type_: _description_
"""
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from blog import schemas
from blog.database.database import get_db
from blog.response_schemas import RESPONSE_401
from blog.processor import authentication

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
