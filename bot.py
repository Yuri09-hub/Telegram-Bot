from climate import get_description_climate, get_climate
import telebot
from dotenv import load_dotenv
import os
load_dotenv()
from datetime import datetime

API_KEY = os.getenv("CHAVE_API")

bot = telebot.TeleBot(str(API_KEY))


@bot.message_handler(commands=['option1'])
def option1(message):
    bot.reply_to(message,
    "my creator name is Yuri Rodrigues. He is trying to learn programming with the help of a guy named Jocelino. ")


@bot.message_handler(commands=['option2'])
def option2(message):
    bot.reply_to(message,
    f"""
    date: {datetime.today().strftime('%d/%m/%Y')}
    """)


@bot.message_handler(commands=['option3'])
def option3(message):
    bot.reply_to(message,
    f"""
    Location: Luanda 
    Temperature is {get_climate()}
    Description: {get_description_climate()}
    """)


def verify(message):
    return True

@bot.message_handlers(func=verify)
def response(res):
    text = """
        /option1 - who i am 
        /option2 - date 
        /option3 - temperature
        Replying with something else won't work.
        """
    bot.reply_to(res,text)


bot.polling()
