import sys
import os
import telebot
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from handlers.handlers_sign_up import handlers_sign_up

load_dotenv()
token = os.getenv("TELEGRAM_BOT_TOKEN")








bot = telebot.TeleBot(token)
handlers_sign_up(bot)






bot.infinity_polling()