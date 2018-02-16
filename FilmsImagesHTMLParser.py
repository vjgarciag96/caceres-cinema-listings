from html.parser import HTMLParser

class FilmsImagesHTMLParser(HTMLParser):

    def __init__(self, films_dict):
        HTMLParser.__init__(self)
        self.films_dict = films_dict
        self.is_image_film = False
        self.film = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'alt':
                    try:
                        self.film = self.films_dict[attr[1]]
                        self.is_image_film = True
                    except:
                        pass
                elif attr[0] == 'src' and self.is_image_film == True:
                    self.film.image = attr[1]

    def handle_endtag(self, tag):
        if tag == 'img' and self.is_image_film == True:
            self.is_image_film = False
