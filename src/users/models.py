from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


int_pk = Annotated[int, mapped_column(primary_key=True)]


class User(Base):
    __tablename__ = "users"

    id: Mapped[int_pk]
    username: Mapped[str]
    email: Mapped[str]
    hashed_password: Mapped[str]

    users_reading: Mapped[list["Book"]] = relationship(
        back_populates="readers",
        secondary="book_readers"
    )
