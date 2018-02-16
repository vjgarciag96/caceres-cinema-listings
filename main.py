from telegram.ext import CommandHandler, Updater
from commands import start, cinema_listings
import os

TOKEN = os.environ.get('TOKEN')
PORT = int(os.environ.get('PORT', '8443'))
WEBHOOK_URL = os.environ.get('WEBHOOK_URL')
BASE_URL = os.environ.get('BASE_URL')

if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    cinema_listing_handler = CommandHandler('cartelera', cinema_listings)
    dispatcher.add_handler(cinema_listing_handler)

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.set_webhook(WEBHOOK_URL + TOKEN)
    updater.idle()

