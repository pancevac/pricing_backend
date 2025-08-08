from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Book


async def book_factory(db_session: AsyncSession) -> Book:
    """Fixture for creating a book. Act like a factory"""
    faker = Faker()
    book = Book(
        id=faker.random_int(),
        title=faker.text(),
        author=faker.name(),
        pages=faker.random_int(),
        rating=faker.random_digit(),
        price=faker.random_digit()
    )
    db_session.add(book)
    await db_session.flush()
    await db_session.refresh(book)
    return book
