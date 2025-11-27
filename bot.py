import telebot
import config
botTime = telebot.TeleBot(config.token)
from telebot import types
@botTime.message_handler(commands=['start'])
def startbot(message):
    welcome = f"{message.from_user.first_name}, Hello! How are you ?\n Welcome to the bot.\nUse /help to see commands"
    markup = types.InlineKeyboardMarkup()
    botTime.send_message(message.chat.id, welcome, parse_mode='html', reply_markup=markup)

botTime.infinity_polling()