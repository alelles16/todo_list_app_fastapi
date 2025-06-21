from pydantic import BaseModel, EmailStr
from typing import Optional


# Data model for creating a new user
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# User data
class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
