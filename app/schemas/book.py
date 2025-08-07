from pydantic import BaseModel, PositiveInt, PositiveFloat


class BookBase(BaseModel):
    title: str
    author: str
    pages: PositiveInt
    rating: PositiveFloat
    price: PositiveFloat


class BookCreate(BookBase):
    id: PositiveInt
    # NOTE: This shouldn't be available as input value. I left it because of script tests,
    # otherwise we should not let user send ID


class BookUpdate(BaseModel):
    rating: PositiveFloat
    price: PositiveFloat


class BookRead(BookBase):
    id: int

    class Config:
        from_attributes = True  # required for model_validate to accept ORM models


class BookList(BaseModel):  # NOTE: This should be used instead of list[BookRead], we want to display items
    items: list[BookRead]
    limit: int
    offset: int
