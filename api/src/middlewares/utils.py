from ..config.config_api import async_session
from sqlalchemy.ext.asyncio import AsyncSession

async def get_session():
    async with async_session() as session:
        yield session