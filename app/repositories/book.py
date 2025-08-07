from sqlalchemy import select, update

from app.models.book import Book
from app.repositories.base import BaseRepository
from app.schemas.book import BookCreate
from app.schemas.book import BookUpdate


class BookRepository(BaseRepository):

    async def get_all(
        self,
        limit: int = 10,
        offset: int = 0,
        title: str | None = None,
        min_pages: int | None = None
    ) -> list[Book]:
        query = select(Book)

        if title:
            query = query.where(Book.title == title)

        if min_pages is not None:
            query = query.where(Book.pages >= min_pages)

        query = query.offset(offset)
        query = query.limit(limit)
        query = query.order_by(Book.id.desc())

        result = await self._session.execute(query)
        return result.scalars().all()

    async def get_by_id(self, book_id: int) -> Book | None:
        query = select(Book).where(Book.id == book_id)
        result = await self._session.execute(query)
        return result.scalar_one()

    async def create(self, book: BookCreate) -> Book:
        book = Book(
            id=book.id,
            title=book.title,
            author=book.author,
            pages=book.pages,
            rating=book.rating,
            price=book.price
        )
        self._session.add(book)
        await self._session.commit()
        await self._session.refresh(book)
        return book

    async def update(self, book_id: int, book: BookUpdate) -> Book:
        query = (
            update(Book)
            .where(Book.id == book_id)
            .values(**book.model_dump())
        )
        await self._session.execute(query)
        await self._session.commit()
        return await self.get_by_id(book_id)
