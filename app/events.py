from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.database import get_async_context_manager_db_session
from app.utils.dump_data import populate_dummy_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Run this event on app start to populate db with dummy data."""

    # before app start
    if settings.ENV == "local":
        async with get_async_context_manager_db_session() as session:
            await populate_dummy_data(session)

    yield
