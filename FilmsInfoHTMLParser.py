from html.parser import HTMLParser
from .Film import Film


class FilmsInfoHTMLParser(HTMLParser):

    def __init__(self, films_dict):
        HTMLParser.__init__(self)
        self.films_dict = films_dict
        self.is_film = False
        self.index = 0
        self.film_object = Film()

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for attr in attrs:
                if attr[0] == 'class' and attr[1] == 'info-line':
                    self.is_film = True

    def handle_endtag(self, tag):
        if tag == 'div' and self.is_film == True:
            self.films_dict[self.film_object.name] = self.film_object
            self.is_film = False
            self.index = 0
            self.film_object = Film()


    def handle_data(self, data):
        if self.is_film == True and data != '\n':
            if self.index == 0:
                self.film_object.name = data.strip()
            elif self.index == 1:
                self.film_object.age_rating = data.strip()
            else:
                self.film_object.timetable.append(data)
            self.index += 1
