import httpx
from ..middlewares.utils import HOURS_IN_SECONDS

class PluggyService:
    def __init__(self):
        self.__apiKey: str = None # Stores API Key in cache
        self.__expiresAtInSeconds: int = 2 * HOURS_IN_SECONDS

    async def get_api_key(self) -> str:

        is_token_expired =

pluggy_service = PluggyService()