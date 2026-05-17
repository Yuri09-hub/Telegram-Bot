import telebot
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("CHAVE_API")

bot = telebot.TeleBot(str(API_KEY))


bot.polling()
