"""_summary_

Raises:
    RequestValidationError: _description_
"""
from sqlalchemy.orm import Session
from fastapi.exceptions import RequestValidationError
from pydantic.error_wrappers import ErrorWrapper
from blog import models, schemas
from blog.constants.messages import EMAIL_EXIST


def check_if_exist(request: schemas.User, db_session: Session):
    """_summary_

    Args:
        request (schemas.User): _description_
        db (Session): _description_

    Raises:
        RequestValidationError: _description_
    """
    user = db_session.query(models.User).filter(models.User.email == request.email).first()
    if user:
        raise RequestValidationError(
            [ErrorWrapper(ValueError(EMAIL_EXIST), ("body", "email"))]
        )
