class Film():
    def __init__(self):
        self.name = ''
        self.age_rating = ''
        self.timetable = []
        self.image = ''

    def log_film(self):
        print('{}, {}'.format(self.name, self.age_rating))
        print("Horarios: ")
        for time in self.timetable:
            print(time)
        print(self.image)