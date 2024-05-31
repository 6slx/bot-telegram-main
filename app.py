from flask import Flask, request
from threading import Thread
import telebot

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token obtained from BotFather
bot = telebot.TeleBot('7464547351:AAEGOElP71f1nrYXBaEUvVDzZvwv54gaHFQ')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your Telegram bot.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Function to start the bot polling loop in a separate thread
def start_bot():
    bot.polling()

# Start the bot polling loop in a separate thread
bot_thread = Thread(target=start_bot)
bot_thread.start()

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, this is a Telegram bot!'

if __name__ == '__main__':
    app.run()
