
import telebot
from dotenv import load_dotenv
import os
load_dotenv()
from datetime import datetime
API_KEY = os.getenv("CHAVE_API")



bot = telebot.TeleBot(str(API_KEY))

def help_response():
    text = """
    /time - what time is it
    / 
    """

@bot.message_handlers(commands=['start'])
def response(res):
    bot.reply_to(res," Hi, I'm Yuri Bot")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message," Hi, I'm Yuri Bot")


bot.polling()
