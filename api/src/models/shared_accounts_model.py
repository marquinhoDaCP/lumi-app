from ..config.config_api import Base
from sqlalchemy import Column, Integer, SmallInteger, ForeignKey

class SharedAccountsModel(Base):
    __tablename__ = 'shared_accounts'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    id_owner_account = Column(Integer, ForeignKey('user_accounts.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    id_member = Column(Integer, ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    can_view_balance = Column(SmallInteger(), default=0, nullable=False)
    can_view_transaction = Column(SmallInteger(), default=0, nullable=False)