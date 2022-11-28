import sqlite3
from utils.DBUtils import DBUtils as utl

DB_NAME = "Fakultet.db"

kreiraj_studij_query = '''
        CREATE TABLE IF NOT EXISTS "Studij" (
	    id INTEGER PRIMARY KEY,
	    naziv TEXT NOT NULL UNIQUE
);
'''

if __name__ == "__main__":
        sqlConnection = sqlite3.connect(DB_NAME)
        utl.izvrsi_i_zapisi(sqlConnection, kreiraj_studij_query)