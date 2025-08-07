from sqlalchemy.exc import IntegrityError, NoResultFound

from app.repositories.book import BookRepository
from app.models.book import Book
from app.services.base import BaseService
from app.schemas.book import BookCreate, BookUpdate
from app.exceptions import NotFoundException
from app.exceptions import IntegrityException


class BookService(BaseService):

    async def get_all(self,
        limit: int,
        offset: int,
        title: str | None = None,
        min_pages: int | None = None
    ) -> list[Book]:
        book_repository = BookRepository(self._session)
        return await book_repository.get_all(limit=limit, offset=offset, title=title, min_pages=min_pages)

    async def get_by_id(self, book_id: int) -> Book:
        book_repository = BookRepository(self._session)
        try:
            return await book_repository.get_by_id(book_id)
        except NoResultFound:
            raise NotFoundException("Book not found")

    async def create(self, book: BookCreate) -> Book:
        book_repository = BookRepository(self._session)
        try:
            return await book_repository.create(book)
        except IntegrityError:
            raise IntegrityException("Book with given name and author already exists")

    async def update(self, book_id: int, book: BookUpdate) -> Book:
        book_repository = BookRepository(self._session)
        try:
            return await book_repository.update(book_id=book_id, book=book)
        except NoResultFound:
            raise NotFoundException("Book not found")
