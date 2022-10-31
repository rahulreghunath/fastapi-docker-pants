"""_summary_"""
# pylint: disable=unexpected-keyword-arg, no-value-for-parameter

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database.database import Base


class Blog(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """

    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates="blogs")


class User(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    phone = Column(String)

    blogs = relationship("Blog")
