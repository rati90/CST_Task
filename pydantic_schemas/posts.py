from pydantic import BaseModel


class PostBase(BaseModel):
    description: str
    user_id: int


class PostCreate(PostBase):
    ...



class Post(PostBase):
    id: int

    class Config:
        orm_mode = True

