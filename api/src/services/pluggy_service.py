import httpx
from ..config.config_api import (
    PLUGGY_API_URL,
    PLUGGY_CLIENT_ID,
    PLUGGY_CLIENT_SECRET
)
from ..middlewares.utils import HOURS_IN_SECONDS

class PluggyService:
    def __init__(self):
        self.__apiKey: str = None # Stores API Key in cache
        self.__expiresAt: int = 2 * HOURS_IN_SECONDS # Expires in seconds (2h)

    async def get_api_key(self) -> str:
        if not self.__apiKey:
            async with httpx.AsyncClient() as http:
                response = await http.post(
                    PLUGGY_API_URL + '/auth',
                    json={
                        "clientId": PLUGGY_CLIENT_ID,
                        "clientSecret": PLUGGY_CLIENT_SECRET
                    }
                )
            
            response.raise_for_status() 

pluggy_service = PluggyService()