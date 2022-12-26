import sqlite3


class DBUtils:
    @staticmethod
    def db_execute(sqlConnection, query):
        try:
            cursor: sqlite3 = sqlConnection.cursor()
            cursor.execute(query)
            row_id = cursor.lastrowid
            sqlConnection.commit()
            cursor.close()
            return row_id
            # print("Akcija uspješno izvršena")
        except sqlite3.Error as sqlError:
            print(sqlError)
        except Exception as e:
            print(e)

    @staticmethod
    def db_fetch(sqlConnection, upit, one=False):
        try:
            cursor: sqlite3.Cursor = sqlConnection.cursor()
            cursor.execute(upit)
            result = None
            if one:
                result = cursor.fetchone()
            else:
                result = cursor.fetchall()
            cursor.close()
            # print("Akcija 'DOHVATI' uspješno izvršena!")
            return result
        except sqlite3.Error as sqlError:
            print(sqlError)
        except Exception as e:
            print(e)
