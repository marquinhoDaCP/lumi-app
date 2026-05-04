from os import environ
from dotenv import load_dotenv

load_dotenv()

# API Config
API_HOST = environ.get('API_HOST') or 'localhost'
API_PORT = int(environ.get('API_PORT') or 8000)
API_SECRET_KEY = environ.get('API_SECRET_KEY') or 'secret-key'
API_EMAIL = environ.get('API_EMAIL')
API_EMAIL_APP_PASSWORD = environ.get('API_EMAIL_APP_PASSWORD')

# Pluggy Config
PLUGGY_CLIENT_ID = environ.get('PLUGGY_CLIENT_ID')
PLUGGY_CLIENT_SECRET = environ.get('PLUGGY_CLIENT_SECRET')

# Database Config
DB_HOST = environ.get('DB_HOST') or 'localhost'
DB_PORT = environ.get('DB_PORT') or 3306
DB_USER = environ.get('DB_USER') or 'root'
DB_PASSWORD = environ.get('DB_PASSWORD') or '123456'
DATABASE = environ.get('DATABASE') or 'lumi'
DB_DRIVER = environ.get('DB_DRIVER') or 'pymysql'
DB_DRIVER_ASYNC = environ.get('DB_DRIVER_ASYNC') or 'aiomysql'

CONNECTION_STR_SYNC = f'mysql+{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/lumi'
CONNECTION_STR_ASYNC = f'mysql+{DB_DRIVER_ASYNC}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/lumi'