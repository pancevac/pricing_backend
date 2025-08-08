import asyncio

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.database import DatabaseSessionManager


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Runs once before tests, create tables."""
    loop = asyncio.get_event_loop()
    mgr = DatabaseSessionManager(str(settings.DATABASE_URL), engine_kwargs={"echo": False})

    async def init():
        async with mgr.connect() as conn:
            await mgr.drop_all_tables(conn)
            await mgr.create_all_tables(conn)

    loop.run_until_complete(init())
    yield  # execute tests
    loop.run_until_complete(mgr.close())


@pytest.fixture
async def db_session() -> AsyncSession:
    mgr = DatabaseSessionManager(str(settings.DATABASE_URL), engine_kwargs={"echo": False})
    async with mgr.session() as session:
        yield session
        await session.rollback()
