from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(String, index=True)
    telegram_id = Column(Integer, index=True)
    name = Column(String)
    is_student = Column(Boolean)

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String, index=True, unique=True)
    message = Column(String) 

