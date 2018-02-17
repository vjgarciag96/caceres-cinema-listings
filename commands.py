import os
import urllib
from urllib.request import urlopen
from FilmsInfoHTMLParser import FilmsInfoHTMLParser

BASE_URL = os.environ.get('BASE_URL')

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello World!!")

def cinema_listings(bot, update):
    films_dict = dict()
    response = urllib.request.urlopen(BASE_URL).read()
    html_file = str(response, 'ISO-8859-1')

    info_parser = FilmsInfoHTMLParser(films_dict=films_dict)
    info_parser.feed(html_file)


    for film in films_dict.values():
        bot.send_message(chat_id=update.message.chat_id,
                         text=film.name)
        bot.send_photo(chat_id=update.message.chat_id,
                       photo=film.image)
