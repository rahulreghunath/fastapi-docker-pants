"""_summary_

Returns:
    _type_: _description_
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog import schemas
from blog.processor import user
from blog.response_schemas import RESPONSE_404, RESPONSE_OK
from blog.database.database import get_db
from blog.validations.user import check_if_exist

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "",
    tags=["users"],
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: RESPONSE_OK,
    },
)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    """_summary_

    Args:
        request (schemas.User): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        _type_: _description_
    """
    check_if_exist(request, db)
    return user.create(request, db)


@router.get(
    "/{id}",
    responses={
        status.HTTP_200_OK: {"model": schemas.ShowUser},
        status.HTTP_404_NOT_FOUND: RESPONSE_404,
    },
    response_model=schemas.ShowUser,
    tags=["users"],
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    # current_user: schemas.User = Depends(get_current_user),
):
    """_summary_

    Args:
        id (int): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).
        current_user (schemas.User, optional): _description_.
            Defaults to Depends(get_current_user).

    Returns:
        _type_: _description_
    """
    return user.get(user_id, db)
