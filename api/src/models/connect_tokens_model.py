from sqlalchemy import (
    Column, Integer, ForeignKey,
    String, DateTime
)
from sqlalchemy.sql import func
from ..config.config_api import Base

class ConnectTokensModel(Base):
    __tablename__ = 'connect_tokens'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    id_user = Column(Integer, ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    token = Column(String(150), nullable=False)
    last_update = Column(
        DateTime(timezone=True), server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(), nullable=False
    )