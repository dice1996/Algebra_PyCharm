from utils.DBUtils import DBUtils
from datasource.dto.Studij import StudijDto
from datetime import datetime as dt

class StudijService:

    TABLE_NAME = "studij"

    def __init__(self, connection):
        self.sqlConnection = connection
        self.kreirajTablicu()


    def kreirajTablicu(self):
        query = f"""
            CREATE TABLE IF NOT EXISTS
                {self.TABLE_NAME} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    naziv VARCHAR(30) UNIQUE
                );
        """
        DBUtils.izvrsiIZapisi(self.sqlConnection, query)

    def dodajNoviStudij(self, naziv):
        query = f"""
            INSERT INTO {self.TABLE_NAME} (naziv) VALUES ('{naziv}');
        """
        DBUtils.izvrsiIZapisi(self.sqlConnection, query)

    def dodajStudij(self, studij: StudijDto):
        self.dodajNoviStudij(studij.naziv)


    def dohvatiSveStudije(self):
        query = f"SELECT * FROM {self.TABLE_NAME};"
        rezultat = DBUtils.dohvatiPodatke(self.sqlConnection, query)
        print(rezultat)
        listaStudija = []
        for studij in rezultat:
            noviStudij: StudijDto = StudijDto.mapirajIzBaze(studij)
            listaStudija.append(noviStudij)

        return listaStudija

    def dohvatiStudijPoIDu(self, id):
        query = f"SELECT * FROM {self.TABLE_NAME} WHERE id = {id};"
        rezultat = DBUtils.dohvatiPodatke(self.sqlConnection, query, one=True)
        return StudijDto.mapirajIzBaze(rezultat)


    def dohvatiStudijPoNazivu(self, naziv):
        query = f"SELECT * FROM {self.TABLE_NAME} WHERE naziv = '{naziv}';"
        rezultat = DBUtils.dohvatiPodatke(self.sqlConnection, query, one=True)
        return StudijDto.mapirajIzBaze(rezultat)

    def izmjeniStudij(self, studijDto: StudijDto, noviNaziv):
        query = f"""
            UPDATE {self.TABLE_NAME} 
                SET naziv = '{noviNaziv}'
                WHERE id = {studijDto.id};
        """
        DBUtils.izvrsiIZapisi(self.sqlConnection, query)
        return self.dohvatiStudijPoIDu(studijDto.id)

    def izbrisiStudijPoIDu(self, id):
        query = f"DELETE FROM {self.TABLE_NAME} WHERE id = {id};"
        izvrseno = DBUtils.izvrsiIZapisi(self.sqlConnection, query)
        if izvrseno:
            print("Entitet obrisan!")
            return True
        else:
            print("Dogodila se pogreska")
            return False




