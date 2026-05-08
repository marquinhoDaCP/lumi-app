from ..config.config_api import async_session
from sqlalchemy.ext.asyncio import AsyncSession

MINUTE_IN_SECONDS = 60
HOURS_IN_SECONDS = 3600

async def get_session():
    async with async_session() as session:
        yield session