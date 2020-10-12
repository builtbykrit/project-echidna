from .datastore import Datastore


class Movie:
    
    def __init__(self, id, name, price_code):
        self.id = id
        self.name = name
        self.price_code = price_code

    def save(self):
        Datastore().add_movie(self)

    @staticmethod
    def get(name):
        return Datastore().get_movie(name)


class MovieFile:

    def __init__(self, id, movie, url):
        self.id = id
        self.movie = movie
        self.url = url


class Rental:

    def __init__(self, id, movie_file, days_rented):
        self.id = id
        self.movie_file = movie_file
        self.days_rented = days_rented