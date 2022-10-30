"""_summary_

Returns:
    _type_: _description_
"""
from typing import List
from fastapi import APIRouter, Depends, status
from fastapi import Security
from sqlalchemy.orm import Session


from blog import schemas
from blog.oauth2 import get_current_user
from blog.response_schemas import RESPONSE_404, RESPONSE_OK
from blog.processor import blog
from blog.database.database import get_db

router = APIRouter(prefix="/blogs", tags=["blogs"])


@router.get(
    "",
    responses={
        status.HTTP_200_OK: {
            "model": List[schemas.ShowBlog],
            "description": "List of Blogs",
        },
    },
    response_model=List[schemas.ShowBlog],
    tags=["blogs"],
)
def get_blogs(
    db: Session = Depends(get_db),
    # user: schemas.TokenData = Depends(get_current_user)
):
    """Launch
    the
    rocket. Go colonize space."""
    return blog.get_all(db)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: RESPONSE_OK,
    },
    tags=["blogs"],
)
def new_blog(
    request: schemas.BlogCreate,
    db: Session = Depends(get_db),
    user: schemas.TokenData = Security(get_current_user, scopes=["blogs"]),
):
    """_summary_

    Args:
        request (schemas.BlogCreate): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).
        user (schemas.TokenData, optional): _description_. Defaults to Security(get_current_user, scopes=["blogs"]).

    Returns:
        _type_: _description_
    """
    return blog.create(request, db, user)


@router.get(
    "/{id}",
    responses={
        status.HTTP_200_OK: {"model": schemas.ShowBlog},
        status.HTTP_404_NOT_FOUND: RESPONSE_404,
    },
    response_model=schemas.ShowBlog,
    tags=["blogs"],
)
def get_blog(
    blog_id: int,
    db: Session = Depends(get_db),
    # user: schemas.TokenData = Depends(get_current_user),
):
    """_summary_

    Args:
        blog_id (int): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        _type_: _description_
    """
    return blog.get(blog_id, db)


@router.delete(
    "/{id}",
    responses={
        status.HTTP_200_OK: RESPONSE_OK,
        status.HTTP_404_NOT_FOUND: RESPONSE_404,
    },
    status_code=status.HTTP_200_OK,
    tags=["blogs"],
)
def delete_blog(
    blog_id: int,
    db: Session = Depends(get_db),
    # user: schemas.TokenData = Depends(get_current_user),
):
    """_summary_

    Args:
        blog_id (int): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        _type_: _description_
    """
    return blog.delete(blog_id, db)


@router.put(
    "/{id}",
    responses={
        status.HTTP_202_ACCEPTED: RESPONSE_OK,
        status.HTTP_404_NOT_FOUND: RESPONSE_404,
    },
    status_code=status.HTTP_202_ACCEPTED,
    tags=["blogs"],
)
def update_blog(
    blog_id: int,
    request: schemas.Blog,
    db: Session = Depends(get_db),
    # user: schemas.TokenData = Depends(get_current_user),
):
    """_summary_

    Args:
        blog_id (int): _description_
        request (schemas.Blog): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        _type_: _description_
    """
    return blog.update(blog_id, request, db)


@router.patch(
    "/{id}",
    responses={
        status.HTTP_202_ACCEPTED: RESPONSE_OK,
        status.HTTP_404_NOT_FOUND: RESPONSE_404,
    },
    status_code=status.HTTP_202_ACCEPTED,
    tags=["blogs"],
)
def partial_update_blog(
    blog_id: int,
    request: schemas.BlogUpdate,
    db: Session = Depends(get_db),
    # user: schemas.TokenData = Depends(get_current_user),
):
    return blog.partial_update(blog_id, request, db)
