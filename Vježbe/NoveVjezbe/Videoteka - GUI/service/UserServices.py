from utils.DBUtils import DBUtils
from datasource.dto.User import UserDto


class UserServices:
    def __init__(self, sqlConnection):
        self.sqlConnection = sqlConnection
        self.create_table()

    def create_table(self):
        query = f'''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            email TEXT NOT NULL,
            oib integer not null,
            movie_id integer,
            FOREIGN KEY(movie_id) REFERENCES movie(id));        
        '''
        DBUtils.db_execute(self.sqlConnection, query)
