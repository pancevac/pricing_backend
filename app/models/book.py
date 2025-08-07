from typing import Optional

from pydantic import PositiveFloat
from sqlalchemy import UniqueConstraint
from sqlmodel import SQLModel, Field


class Book(SQLModel, table=True):
    __tablename__ = "books"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(nullable=False, index=True)
    author: str = Field(nullable=False)
    pages: int = Field(nullable=False, index=True)
    rating: PositiveFloat = Field(nullable=False)
    price: PositiveFloat = Field(nullable=False)

    # Composite unique constraint
    __table_args__ = (
        UniqueConstraint("title", "author", name="uq_title_author"),
    )