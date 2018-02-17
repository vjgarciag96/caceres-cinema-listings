from html.parser import HTMLParser
from Film import Film
import re
import os

BASE_URL = os.environ.get('BASE_URL')

class FilmsInfoHTMLParser(HTMLParser):

    def __init__(self, films_dict):
        HTMLParser.__init__(self)
        self.films_dict = films_dict
        self.is_film = False
        self.index = 0
        self.divs_counter = 0
        self.film_object = Film()

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for attr in attrs:
                if attr[0] == 'class' and attr[1] == 'OLCT_movieTimesInfo':
                    self.is_film = True
        elif tag == 'img' and self.is_film:
            for attr in attrs:
                if attr[0] == 'src':
                    self.film_object.image = BASE_URL + attr[1]

    def handle_endtag(self, tag):
        if tag == 'div' and self.is_film == True:
            if self.divs_counter > 0:
                self.films_dict[self.film_object.name] = self.film_object
                self.is_film = False
                self.index = 0
                self.divs_counter = 0
                self.film_object = Film()
            else:
                self.divs_counter += 1


    def handle_data(self, data):
        data_cleaned = data.strip()
        if self.is_film == True and data_cleaned:
            if self.index == 0:
                self.film_object.name = data_cleaned
            elif self.index == 1:
                self.film_object.date = data_cleaned
            else:
                hhmm_regex = '^([0-9]{2}):([0-9]{2})'
                pattern = re.compile(hhmm_regex)
                if pattern.match(data_cleaned):
                    self.film_object.timetable.append(data_cleaned)
                else:
                    current_index = self.index - self.film_object.timetable.__len__()
                    if current_index == 2:
                        self.film_object.age_rating = data_cleaned
                    elif current_index == 3:
                        self.film_object.duration = data_cleaned
            self.index += 1
