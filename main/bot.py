import os
import telebot
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TELEGRAM_BOT_TOKEN")








bot = telebot.TeleBot(token)







bot.infinity_polling()