from .datastore import Datastore


class Customer:
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.rentals = []

    def statement(self):
        t = 0
        frequent_renter_points = 0
        result = "Rental record for {}\n".format(self.name)
        for rental in self.rentals:
            amt = 0

            # Regular movie
            if rental.movie_file.movie.price_code == 0:
                amt += 2
                if rental.days_rented > 2:
                    amt += (rental.days_rented - 2) * 1.5

            # New release
            elif rental.movie_file.movie.price_code == 1:
                amt += rental.days_rented * 3

            # Childrens
            elif rental.movie_file.movie.price_code == 2:
                amt += 1.5
                if rental.days_rented > 3:
                    amt += (rental.days_rented - 3) * 1.5

            t += amt

            frequent_renter_points += 1
            if (rental.movie_file.movie.price_code == 1) and rental.days_rented > 1:
                frequent_renter_points += 1

            result += "{}: {}".format(rental.movie_file.movie.name, amt)

        result += "Total due is {}\n".format(t)
        result += "You earned {} frequent renter points!".format(frequent_renter_points)

        return result

    def add_rental(self, rental):
        self.rentals.append(rental)

    def save(self):
        Datastore().add_movie(self)

    @staticmethod                                       
    def get(name):
        return Datastore().get_movie(name)