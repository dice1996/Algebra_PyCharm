

class MovieDto:
    def __init__(self):
        self.id = None
        self.name = None
        self.year = None
        self.director = None
        self.status = None

    def create_movie(self, name, year, director):
        self.name = name
        self.year = year
        self.director = director
        self.status = 0

        return self

    @staticmethod
    def map_to_movieDto(movie: tuple):
        movie_dto = MovieDto()
        movie_dto.id = movie[0]
        movie_dto.name = movie[1]
        movie_dto.year = movie[2]
        movie_dto.director = movie[3]
        movie_dto.status = movie[4]
        return movie_dto