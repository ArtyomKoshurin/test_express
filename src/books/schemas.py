from typing import Optional
from datetime import date

from pydantic import BaseModel

from users.schemas import UserGetSchema


class BookCreateSchema(BaseModel):
    title: str
    author: str


class BookGetSchema(BaseModel):
    title: str
    author: str
    readers: Optional[list[UserGetSchema]]
    date_of_granting: Optional[date]
    date_of_returning: Optional[date]
    status: str
