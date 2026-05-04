from ..config.config_api import Base
from sqlalchemy import Column, Integer, String

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)