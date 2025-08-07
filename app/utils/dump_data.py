import json

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Book


async def populate_dummy_data(session: AsyncSession) -> None:
    """Populate dummy books."""
    result = await session.execute(select(Book))

    # if existing, terminate insertion
    if result.first():
        return

    with open("books.json") as f:
        books = json.load(f)

    for book in books:
        book = Book(
            id=book["id"],
            title=book["title"],
            author=book["author"],
            pages=book["pages"],
            price=book["price"],
            rating=book["rating"],
        )
        session.add(book)
    await session.flush()
    await session.commit()

    print('Dummy data inserted!')
