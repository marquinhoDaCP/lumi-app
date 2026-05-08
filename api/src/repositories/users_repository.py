from ..schemas import users_schema
from ..models.users_model import UserModel
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

class UsersRepostitory:
    def __init__(self):
        self.__userModel = UserModel

    async def create_user(self, user: users_schema.CreateUser, db: AsyncSession):
        try:
            user_dict = user.__dict__
            db_user = self.__userModel(**user_dict)

            db.add(db_user)
        
            await db.commit()
            await db.refresh(db_user)
        
            return db_user
        
        except:
            await db.rollback()
            raise

    async def get_all_users(self, db: AsyncSession):
        response = await db.execute(select(self.__userModel))
        return response.scalars().all()

    async def get_user_by_id(self, id: int, db: AsyncSession):
        response = await db.execute(select(self.__userModel).where(self.__userModel.id == id))
        return response.scalars().first()

    async def update_user_by_id(self, id: int, user: users_schema.UpdateUser, db: AsyncSession):
        user_dict = { key:value for key, value in user.__dict__.items() if value is not None }
        
        try:
            await db.execute(update(self.__userModel).where(self.__userModel.id == id).values(user_dict))
            await db.commit()

            return await self.get_user_by_id(id, db)
        
        except:
            await db.rollback()
            raise

    async def delete_user_by_id(self, id: int, db: AsyncSession):
        response = await db.execute(delete(self.__userModel).where(self.__userModel.id == id))
        await db.commit()
        return response