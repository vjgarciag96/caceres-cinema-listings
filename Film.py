class Film():
    def __init__(self):
        self.name = ''
        self.date = ''
        self.age_rating = ''
        self.timetable = []
        self.image = ''
        self.duration = ''

    def log_film(self):
        print('{}, {}, {}'.format(self.name, self.age_rating, self.duration))
        print(self.date)
        print("Horarios: ")
        for time in self.timetable:
            print(time)
        print(self.image)