"""_summary_"""

from typing import List, Union
from pydantic import BaseModel, Field, constr


class HTTPError(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    detail: str

    class Config:
        """_summary_"""

        schema_extra = {
            "example": {"detail": "HTTPException raised."},
        }


class HTTPSuccess(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    detail: str

    class Config:
        """_summary_"""

        schema_extra = {
            "example": {"detail": "Response message"},
        }


class BlogBase(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    title: Union[str, None] = None
    body: Union[str, None] = None


class Blog(BlogBase):
    """_summary_

    Args:
        BlogBase (_type_): _description_
    """

    title: Union[str, None] = None
    body: Union[str, None] = None

    class Config:
        """_summary_"""

        orm_mode = True


class BlogCreate(Blog):
    """_summary_

    Args:
        Blog (_type_): _description_
    """

    title: constr(min_length=10, max_length=100) = Field(
        title="Blog title",
        description="Title should more that 10 and less than 100 charactors",
    )
    blog_body: constr(min_length=100, max_length=1000) = Field(
        title="Blog Body",
        description="Body should more that 100 and less than 1000 charactors",
    )


class BlogUpdate(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    title: Union[str, None] = None
    body: Union[str, None] = None


class BaseUser(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    name: str
    email: str


class ResponseUser(BaseUser):
    """_summary_

    Args:
        BaseUser (_type_): _description_
    """

    class Config:
        """_summary_"""

        orm_mode = True


class User(BaseUser):
    """_summary_

    Args:
        BaseUser (_type_): _description_
    """

    password: str


class ShowUser(BaseUser):
    """_summary_

    Args:
        BaseUser (_type_): _description_
    """

    blogs: List[Blog]

    class Config:
        """_summary_"""

        orm_mode = True


class ShowBlog(Blog):
    """_summary_

    Args:
        Blog (_type_): _description_
    """

    creator: ResponseUser = {}

    class Config:
        """_summary_"""

        orm_mode = True


class Login(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    username: str
    password: str


class Token(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: int = None
    scopes: List[str] = []
