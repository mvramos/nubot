from typing import List, Optional
from pydantic import BaseModel


class MessageBase(BaseModel):
    keyword: str
    message: str

class MessageCreate(MessageBase):
    pass

#when reading
class Message(MessageBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    telegram_id: int
    chat_id: int
    is_student: Optional[bool] = True

class UserCreate(UserBase):
    pass

# when reading
class User(UserBase):
    id: int

    class Config:
        orm_mode = True