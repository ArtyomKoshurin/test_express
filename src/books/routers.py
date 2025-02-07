from fastapi import APIRouter, HTTPException
from starlette import status

from database import db_dependency
from users.auth import user_dependency
from books.schemas import BookCreateSchema, BookGetSchema
from books.models import Book


router = APIRouter(
    prefix="/books",
    tags=["books"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(user: user_dependency, db: db_dependency, create_book_request: BookCreateSchema):
    """Создание книги. Требуется аутентификация"""
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required"
        )
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
    return db.query(Book).filter(Book.id == book_id).first()


@router.delete("/{book_id}")
def delete_book_by_id(user: user_dependency, db: db_dependency, book_id: int):
    """Удаление книги по id. Требуется аутентификация"""
    book_for_delete = db.query(Book).filter(Book.id == book_id).first()
    db.delete(book_for_delete)
    db.commit()
    return f'Book {book_for_delete.title} deleted'
