

class Datastore:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Datastore, cls).__new__(cls)
            cls.instance.movies = []
            cls.instance.customers = []
        return cls.instance

    def add_movie(self, movie):
        self.movies.append(movie)
        # TODO: Persist movies

    def get_movie(self, name):
        for movie in self.movies:
            if movie.name == name:
                return movie

        return None

    def add_customer(self, customer):
        self.customers.append(customer)
        # TODO: Persist customers

    def get_customer(self, name):
        for movie in self.movies:
            if movie.name == name:
                return movie

        return None