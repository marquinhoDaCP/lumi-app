from typing import List
from ..schemas import users_schema
from ..middlewares.utils import get_session
from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession
from ..controllers.users_controller import UsersController

usersController = UsersController()
router = APIRouter(prefix='/users', tags=['users'])

@router.post('', response_model=users_schema.UserResponse)
async def get_all_users(
    user: users_schema.CreateUser,
    db: AsyncSession = Depends(get_session)
):
    return await usersController.create_user(user, db)

@router.get('', response_model=list[users_schema.UserResponse])
async def get_all_users(db: AsyncSession = Depends(get_session)):
    return await usersController.get_all_users(db)

@router.get('/{id}', response_model=users_schema.UserResponse)
async def get_user_by_id(
    db: AsyncSession = Depends(get_session),
    id: int = Path(description="ID to retrieve data")
):
    return await usersController.get_user_by_id(id, db)

@router.patch('/{id}', response_model=users_schema.UserResponse)
async def update_user_by_id(
    user: users_schema.UpdateUser,
    db: AsyncSession = Depends(get_session),
    id: int = Path(description="ID to update data")
):
    return await usersController.update_user_by_id(id, user, db)

@router.delete('/{id}')
async def delete_user_by_id(
    db: AsyncSession = Depends(get_session),
    id: int = Path(description="ID to delete data")
):
    return await usersController.delete_user_by_id(id, db)