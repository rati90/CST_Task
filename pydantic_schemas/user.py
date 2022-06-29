from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str
    role: int = 1
    is_public: bool = True
    is_active: bool = True


class UserInDB(UserBase):
    hashed_password: str


class User(UserBase):
    id: int
    is_public: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
