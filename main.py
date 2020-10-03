from typing import Optional, List
from fastapi import FastAPI, Depends, HTTPException
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
import logging

from sqlalchemy.orm import Session

from crud import create_message, get_messages
from models import Base
from schemas import Message, MessageCreate

from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

#DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


TOKEN = '940763980:AAHF3BjmtoC9wJJLk9qpuB0Amp74mxvXQ1Q'

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Start bot handling text messages. Commands are ignored for now.
def startBot(update, context):
    """
        TODOs:
            0) Checa se o aluno é novo e manda msg de boas vindas
            1) Clean message (Lower, strip special characters split and get first word) e.g. Sim = sim = Sim! = SiM, por favor = Sim <3 etc
            2) Busca msg no banco e retorna o texto 
            3) Se não achou retorna uma mensagem que não entendeu. 
            4) Subir para Máquina Virtual
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text='Olá eu sou o Ronaldinho seu amiguinho.')

start_handler = MessageHandler(Filters.text & (~Filters.command), startBot)
dispatcher.add_handler(start_handler)

def commandBot(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Vai toma no cu mermão')

command_handler = CommandHandler('cuzao', commandBot)
dispatcher.add_handler(command_handler)

#Start bot
updater.start_polling()


@app.get('/')
def root():
    return 'Servidor está no ar!'

@app.get('/start')
def start():
    updater.start_polling()
    return "TÁ ONLINE MULEKE!"

@app.get('/stop')
def stop_bot():
    updater.stop()
    return 'BOT DESLIGOU'

@app.post('/messages/', response_model = Message)
def add_message_to_db(message: MessageCreate, db: Session = Depends(get_db)):
    return create_message(db=db, message=message)

@app.get('/messages/', response_model=List[Message])
def read_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    messages = get_messages(db, skip=skip, limit=limit)
    return messages
