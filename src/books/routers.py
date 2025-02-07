import smtplib
from datetime import datetime
from email.message import EmailMessage

from fastapi import APIRouter, HTTPException
from starlette import status

from database import db_dependency
from users.auth import user_dependency
from users.models import User
from books.schemas import BookCreateSchema, BookGetSchema
from books.models import Book, BookReadersModel
from utils import send_email


router = APIRouter(
    prefix="/books",
    tags=["books"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(
    user: user_dependency,
    db: db_dependency,
    create_book_request: BookCreateSchema
):
    """Создание книги. Требуется аутентификация"""

    create_book = Book(
        title=create_book_request.title,
        author=create_book_request.author
    )
    db.add(create_book)
    db.commit()
    return f'Book {create_book.title} created'


@router.get("/", response_model=list[BookGetSchema])
def get_books(db: db_dependency):
    """Получение всех книг"""

    return db.query(Book).all()


@router.get("/{book_id}", response_model=BookGetSchema)
def get_book_by_id(db: db_dependency, book_id: int):
    """Получение книги по id"""
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No books with thix id"
            )
    return book


@router.delete("/{book_id}")
def delete_book_by_id(user: user_dependency, db: db_dependency, book_id: int):
    """Удаление книги по id. Требуется аутентификация"""

    book_for_delete = db.query(Book).filter(Book.id == book_id).first()
    if not book_for_delete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No books with thix id"
            )
    db.delete(book_for_delete)
    db.commit()
    return f'Book {book_for_delete.title} deleted'


@router.post("/givebook/{book_id}/{user_id}")
def give_the_book_to_reader(
    user: user_dependency,
    db: db_dependency,
    book_id: int,
    user_id: int
):
    """Выдача книги. Требуется аутентификация"""

    create_relation = BookReadersModel(
        book_id=book_id,
        user_id=user_id,
        )
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No books with thix id"
            )
    book.date_of_granting = datetime.today()
    db.add(create_relation)
    db.commit()
    return "Книга успешно выдана"


@router.get("/sendmail/{book_id}/{user_id}")
def send_the_mail_to_the_reader(
    user: user_dependency,
    db: db_dependency,
    book_id: int,
    user_id: int
):
    """Отправить письмо читателю о возврате книги. Требуется аутентификация"""
    user = db.query(User).filter(User.id == user_id).first()
    book = db.query(Book).filter(Book.id == book_id).first()
    if not db.query(BookReadersModel).filter(
            BookReadersModel.book_id == book_id and BookReadersModel.user_id == user_id).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User doesn't have this book"
            )

    send_email(user.username, book.title, user.email)

    return "Email successfully sent"
