from typing import Annotated

from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_db_session


class BaseService:

    _session: AsyncSession

    def __init__(self, session: Annotated[AsyncSession, Depends(get_db_session)]):
        self._session = session
