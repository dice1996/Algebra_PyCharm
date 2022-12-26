from datasource.dto.Movie import MovieDto
from service.MovieService import MovieService
from service.UserServices import UserServices
import sqlite3

DB_NAME = "videoteka.db"

class VideotekaService:
    def __init__(self):
        self.sqlConnection = sqlite3.connect(DB_NAME)
        MovieService(self.sqlConnection)
        UserServices(self.sqlConnection)

    def create_movie(self, name, year, director):
        movie = MovieDto()
        if name == "" or year == "" or director == "":
            return "Podaci nisu ispravno popunjeni. Pokušaj ponovno!"
        else:
            MovieService(self.sqlConnection).insert_movie(movie.create_movie(name, year, director))
            return "Film uspješno spremljen!"

    def show_available_movies(self):
        movies = MovieService(self.sqlConnection).show_available_movies()
        return movies