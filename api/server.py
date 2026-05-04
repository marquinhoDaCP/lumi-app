import uvicorn
from src.config.config_api import API_HOST, API_PORT

if __name__ == '__main__':
    uvicorn.run(
        app='src.api:app',
        host=API_HOST,
        port=API_PORT,
        reload=True
    )