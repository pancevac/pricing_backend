from typing import Annotated

from fastapi import APIRouter, Depends, Query, status

from app.schemas.book import BookRead, BookUpdate
from app.services.book import BookService
from app.schemas.book import BookCreate
from app.models import Book

router = APIRouter(prefix="/books", tags=["books"])
BookServiceDep = Annotated[BookService, Depends(BookService)]

@router.get("/", response_model=list[BookRead])
async def get_books(
    service: BookServiceDep,
    limit: Annotated[int, Query(ge=0, description="Maximum number of book's pages per request")] = 30,
    offset: Annotated[int, Query(ge=0, description="Offset from start of book's pages")] = 0,
    title: Annotated[str | None, Query(description="Title of a book")] = None,
    min_pages: Annotated[int | None, Query(description="Minimum number of book's pages")] = None,
) -> list[Book]:
    """Get all books, optionally by title or min_pages, with pagination."""

    return await service.get_all(limit=limit, offset=offset, title=title, min_pages=min_pages)


@router.get("/{book_id}", response_model=BookRead)
async def get_book_by_id(service: BookServiceDep, book_id: int) -> Book:
    """Get book by its ID."""

    return await service.get_by_id(book_id)


@router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
async def create_book(service: BookServiceDep, body: BookCreate) -> Book:
    """Add new book record."""

    return await service.create(book=body)


@router.put("/{book_id}", response_model=BookRead) # note: this should be patch method, but test will fail.
async def update_book(service: BookServiceDep, book_id: int, body: BookUpdate) -> Book:
    """Update book price and rating."""

    return await service.update(book_id=book_id, book=body)
