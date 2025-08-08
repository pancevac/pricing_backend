import pytest
from pytest_mock import MockerFixture
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.book import BookService
from app.repositories.book import BookRepository
from app.tests.factories import book_factory
from app.exceptions import NotFoundException


@pytest.mark.asyncio
async def test_get_book_by_id(db_session: AsyncSession, mocker: MockerFixture) -> None:
    # arrange
    book_service = BookService(db_session)
    book = await book_factory(db_session)

    mock_book_repository_get = mocker.patch.object(BookRepository, 'get_by_id', return_value=book)

    # act
    result_book = await book_service.get_by_id(book.id)

    # assert
    assert result_book.id == book.id
    assert result_book.title == book.title
    assert result_book.author == book.author
    mock_book_repository_get.assert_called_once_with(book.id)


@pytest.mark.asyncio
async def test_get_book_by_id_when_not_exist(db_session: AsyncSession, mocker: MockerFixture) -> None:
    # arrange
    book_service = BookService(db_session)
    mock_book_repository_get = mocker.patch.object(BookRepository, 'get_by_id', side_effect=NoResultFound)

    # act
    with pytest.raises(NotFoundException):
        await book_service.get_by_id(999)

    # assert
    mock_book_repository_get.assert_called_once_with(999)
