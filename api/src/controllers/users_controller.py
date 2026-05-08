import bcrypt 
from ..schemas import users_schema
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..repositories.users_repository import UsersRepostitory

class UsersController:
    def __init__(self):
        self.__usersRepository = UsersRepostitory()
        self.__notFoundException = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    async def create_user(self, user: users_schema.CreateUser, db: AsyncSession) -> users_schema.UserResponse:
        # Encrypt users password before saves in database
        user.password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())

        response = await self.__usersRepository.create_user(user, db)
        return response
    
    async def get_all_users(self, db: AsyncSession) -> list[users_schema.UserResponse]:
        response = await self.__usersRepository.get_all_users(db)
        return response
    
    async def get_user_by_id(self, id: int, db: AsyncSession) -> users_schema.UserResponse:
        response = await self.__usersRepository.get_user_by_id(id, db)

        if not response:
            raise self.__notFoundException

        return response
    
    async def update_user_by_id(
        self,
        id: int,
        user: users_schema.UpdateUser,
        db: AsyncSession
    ) -> users_schema.UserResponse:
        user_db = await self.__usersRepository.get_user_by_id(id, db)

        if not user_db:
            raise self.__notFoundException
        
        response = await self.__usersRepository.update_user_by_id(id, user, db)
        return response
    
    async def delete_user_by_id(self, id: int, db: AsyncSession):
        user = await self.__usersRepository.get_user_by_id(id, db)

        if not user:
            raise self.__notFoundException
        
        await self.__usersRepository.delete_user_by_id(id, db)
        return {
            "message": "User removed successfully"
        }