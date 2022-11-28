import sqlite3


class DBUtils:
    @staticmethod
    def izvrsi_i_zapisi(sqlConnection, upit):
        try:
            cursor = sqlConnection.cursor()
            cursor.execute(upit)
            sqlConnection.commit()
            cursor.close()
            print("Akcija uspješno izvršena")
        except sqlite3.Error as sqlError:
            print(sqlError)
        except Exception as e:
            print(e)