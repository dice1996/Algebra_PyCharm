import sqlite3


class DBUtils:
    @staticmethod
    def execute_query(sqlConnection, query):
        try:
            cursor: sqlite3 = sqlConnection.cursor()
            cursor.execute(query)
            row_id = cursor.lastrowid
            sqlConnection.commit()
            cursor.close()
            return row_id
            #print("Akcija uspješno izvršena")
        except sqlite3.Error as sqlError:
            print(sqlError)
        except Exception as e:
            print(e)

    @staticmethod
    def fetch_data(sqlConnection, upit, one = False):
        try:
            cursor: sqlite3.Cursor = sqlConnection.cursor()
            cursor.execute(upit)
            rezultat = None
            if one:
                rezultat = cursor.fetchone()
            else:
                rezultat = cursor.fetchall()
            cursor.close()
            #print("Akcija 'DOHVATI' uspješno izvršena!")
            return rezultat
        except sqlite3.Error as sqlError:
            print(sqlError)
        except Exception as e:
            print(e)

