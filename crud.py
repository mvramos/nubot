from sqlalchemy.orm import Session

from schemas import UserCreate, MessageCreate

from models import User, Message

def get_user(db: Session, user_id:int):
    return db.query(User).filter(User.telegram_id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    db_user = User(
                name = user.name, 
                telegram_id = user.telegram_id,
                chat_id = user.chat_id
              )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Message).offset(skip).limit(limit).all()

def create_message(db: Session, message: MessageCreate):
    db_message = Message(
                    keyword = message.keyword,
                    message = message.message
                )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message