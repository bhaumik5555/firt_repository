class Movie:
    def __init__(self, movie_name, launch_year):
        self.movie_name = movie_name
        self.launch_year = max(0,launch_year)

    @classmethod
    def cast(cls, lead_actor):
        cls.lead_actor = lead_actor
        return lead_actor

    def set_location(self, set_locations):
        self.set_locations = set_locations
        return set_locations


movie1 = Movie("Avengers", 2015)
movie2 = Movie("Ironman", 2011)

print(movie2.movie_name)
print(Movie.cast("Robert Downy Jr."))
print(movie1.set_location("New_York."))
# print(movie2.cast)
# print(movie1.set_location)
print(movie1.__dict__)

print(movie2.launch_year)

