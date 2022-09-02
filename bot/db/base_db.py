import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from models.db_session import create_session


class BaseDBApi:
    """
    Этот класс базовый для взаимодействия с БД. Тут создается сессия, а при удалении объекта - закрывается
    """

    _sess: AsyncSession

    def __init__(self):
        self._sess = create_session()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args, **kwargs):
        await self.close()

    def __del__(self):
        asyncio.create_task(self.close())

    async def close(self):
        await self._sess.close()
