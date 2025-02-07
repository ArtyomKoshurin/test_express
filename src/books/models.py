from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    readers: Mapped[list["User"]] = relationship(
        back_populates="users_reading",
        secondary="book_readers"
    )
    date_of_granting: Mapped[date] = mapped_column(nullable=True)
    date_of_returning: Mapped[date] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(default="in_stock")


class BookReadersModel(Base):
    __tablename__ = "book_readers"

    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id"),
        primary_key=True,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        primary_key=True,
    )
