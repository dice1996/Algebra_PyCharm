from utils.DBUtils import DBUtils
from datasource.dto.Studij import StudijDto


class StudijService:

    TABLE_NAME = "studij"

    def __init__(self, sqlConnection):
        self.sqlConnection = sqlConnection
        self.kreiraj_tablicu()


    def kreiraj_tablicu(self):
        query = f'''
            CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
            id INTEGER PRIMARY KEY,
            naziv TEXT NOT NULL UNIQUE
            );
        '''
        DBUtils.izvrsi_i_zapisi(self.sqlConnection, query)


    def dodaj_novi_studij(self, naziv):
        query = f'''
            INSERT INTO {self.TABLE_NAME} (naziv)
            VALUES ("{naziv}");
        '''

        DBUtils.izvrsi_i_zapisi(self.sqlConnection, query)

    def dodaj_studij(self, studij: StudijDto):
        self.dodaj_novi_studij(studij.naziv)


    def dohvati_studije(self):
        query = f'''
            SELECT * FROM {self.TABLE_NAME};
        '''
        rezultat = DBUtils.dohvati_podatak(self.sqlConnection, query)

        listaStudija = []

        for studij in rezultat:
            listaStudija.append(StudijDto.map_data_from_database(studij))

        print(listaStudija)

    def dohvati_studij_po_idju(self, id):
        query = f"SELECT * FROM {self.TABLE_NAME} WHERE id = {id};"

        rezultat = DBUtils.dohvati_podatak(self.sqlConnection, query, True)
        studij = StudijDto.map_data_from_database(rezultat)
        return studij

    def izmijeni_studij(self, studij: StudijDto, naziv):

        query = f'''
            UPDATE {self.TABLE_NAME}
            SET naziv = "{naziv}"
            WHERE id = {studij.id};
        '''
        DBUtils.izvrsi_i_zapisi(self.sqlConnection, query)