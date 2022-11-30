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

    # @staticmethod
    # def dohvati_listu_podataka(sqlConnection, upit):
    #     try:
    #         cursor: sqlite3.Cursor = sqlConnection.cursor()
    #         cursor.execute(upit)
    #         rezultat = cursor.fetchall()
    #         cursor.close()
    #         print("Akcija 'DOHVATI' uspješno izvršena!")
    #         return rezultat
    #     except sqlite3.Error as sqlError:
    #         print(sqlError)
    #     except Exception as e:
    #         print(e)
    #
    # @staticmethod
    # def dohvati_podatak(sqlConnection, upit):
    #     try:
    #         cursor: sqlite3.Cursor = sqlConnection.cursor()
    #         cursor.execute(upit)
    #         rezultat = cursor.fetchone()
    #         cursor.close()
    #         print("Akcija 'DOHVATI' uspješno izvršena!")
    #         return rezultat
    #     except sqlite3.Error as sqlError:
    #         print(sqlError)
    #     except Exception as e:
    #         print(e)

    @staticmethod
    def dohvati_podatak(sqlConnection, upit, one = False):
        try:
            cursor: sqlite3.Cursor = sqlConnection.cursor()
            cursor.execute(upit)
            rezultat = None
            if one:
                rezultat = cursor.fetchone()
            else:
                rezultat = cursor.fetchall()
            cursor.close()
            print("Akcija 'DOHVATI' uspješno izvršena!")
            return rezultat
        except sqlite3.Error as sqlError:
            print(sqlError)
        except Exception as e:
            print(e)