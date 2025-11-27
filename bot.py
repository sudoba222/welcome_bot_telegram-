import os
from dotenv import load_dotenv
import telebot

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


if not TOKEN:

    raise ValueError("Token not found ")


botTime = telebot.TeleBot(TOKEN)


@botTime.message_handler(commands=['start', 'help'])
def handle_commands(message):
    if message.text == '/start':
        welcome_text = f"{message.from_user.first_name}, Hello! How are you?\nWelcome to the bot.\nUse /help to see commands"

        botTime.send_message(message.chat.id, welcome_text, parse_mode='html') #, reply_markup=markup)

    elif message.text == '/help':
        help_text =( "Welcome to the bot! Here are the available commands:\n"
    "/start - Display the welcome message and introduction\n"
    "/help - Show this list of commands and information"
)
        botTime.send_message(message.chat.id, help_text)

print("Bot is running ...")

botTime.infinity_polling()
