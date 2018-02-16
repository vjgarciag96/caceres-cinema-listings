from telegram.ext import CommandHandler, Updater
from commands import start

TOKEN = 'your_bot_token'

if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
