from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    job: str
    date: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    is_active: bool

    class Config:
        orm_mode = True