from typing import Optional
from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str

class CreateUser(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str

class UpdateUser(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None