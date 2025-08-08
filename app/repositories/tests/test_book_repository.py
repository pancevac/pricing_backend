import pytest
from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.book import BookRepository
from app.schemas.book import BookCreate, BookUpdate
from app.tests.factories import book_factory


@pytest.mark.asyncio
async def test_get_book_by_id(db_session: AsyncSession) -> None:
    # arrange
    book_repository = BookRepository(db_session)
    book = await book_factory(db_session)

    # act
    result_book = await book_repository.get_by_id(book.id)

    # assert
    assert result_book.id == book.id
    assert result_book.title == book.title
    assert result_book.author == book.author


@pytest.mark.asyncio
async def test_create_book(db_session: AsyncSession, faker: Faker) -> None:
    # arrange
    book_repository = BookRepository(db_session)
    book_in = BookCreate(
        id=faker.random_int(),
        title=faker.word(),
        author=faker.name(),
        price=faker.random_digit(),
        rating=faker.random_digit(),
        pages=faker.random_int()
    )

    # act
    book = await book_repository.create(book_in)

    # assert
    assert type(book.id) == int


@pytest.mark.asyncio
async def test_update_book(db_session: AsyncSession, faker: Faker) -> None:
    # arrange
    book_repository = BookRepository(db_session)
    book = await book_factory(db_session)
    book_update = BookUpdate(
        rating=faker.random_digit(),
        price=faker.random_digit()
    )

    # act
    updated_book = await book_repository.update(book_id=book.id, book=book_update)

    # assert
    assert updated_book.id == book.id
    assert updated_book.rating == book_update.rating
    assert updated_book.price == book_update.price
