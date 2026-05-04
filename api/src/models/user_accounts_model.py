from ..config.config_api import Base
from sqlalchemy import Column, Integer, ForeignKey

class UserAccountsModel(Base):
    __tablename__ = 'user_accounts'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    id_item = Column(Integer, nullable=False)
    id_user = Column(Integer, ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'))