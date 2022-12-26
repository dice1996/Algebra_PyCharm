from datasource.dto.Movie import MovieDto
from utils.DBUtils import DBUtils

class MovieService:
    def __init__(self, sqlConnection):
        self.sqlConnection = sqlConnection
        self.create_table()

    def create_table(self):
        query = f'''
        CREATE TABLE IF NOT EXISTS movie (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            year INTEGER NOT NULL,
            director TEXT NOT NULL,
            status INTEGER NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id)
            );
        '''
        DBUtils.db_execute(self.sqlConnection, query)

    def insert_movie(self, movie: MovieDto):
        query = f'''
            INSERT INTO movie (
                name,
                year,
                director,
                status)
            VALUES ("{movie.name}", {movie.year}, "{movie.director}", {movie.status});'''
        DBUtils.db_execute(self.sqlConnection, query)

    def show_available_movies(self):
        query = f'''
        SELECT * FROM movie WHERE status = 0;
        '''
        result = DBUtils.db_fetch(self.sqlConnection, query)
        movies = []
        for movie in result:
            movie_item = MovieDto.map_to_movieDto(movie)
            movie_item.status = "AVAILABLE"
            movies.append(movie_item)
        return movies