from datasource.dto.Student import StudentDto
from utils.DBUtils import DBUtils
from enum import Enum

class StudentIndex(Enum):
    ID = 0
    IME = 1
    PREZIME = 2
    EMAIL = 3
    GRAD = 4
    ZIP = 5


class StudentService:
    TABLE_NAME = "student"

    def __init__(self, sqlConnection):
        self.sqlConnection = sqlConnection
        self.kreiraj_tablicu()

    def kreiraj_tablicu(self):
        query = f'''
            CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
                id INTEGER PRIMARY KEY,
                ime VARCHAR(30) NOT NULL,
                prezime VARCHAR(30) NOT NULL,
                email VARCHAR(60) NOT NULL UNIQUE,
                grad VARCHAR(30) NOT NULL,
                zip VARCHAR(5) NOT NULL
            );
        '''
        DBUtils.izvrsi_i_zapisi(self.sqlConnection, query)

    def dodaj_novog_studenta(self, ime, prezime, email, grad, zip):

        query = f'''
            INSERT INTO {self.TABLE_NAME} (ime, prezime, email, zip, grad)
            VALUES ('{ime}', '{prezime}', '{email}', '{zip}', '{grad}')   
        '''
        DBUtils.izvrsi_i_zapisi(self.sqlConnection, query)

    def dodaj_studenta(self, student: StudentDto):
        self.dodaj_novog_studenta(student.ime, student.prezime, student.email, student.grad, student.zip)

    def dohvati_sve_studente(self):
        query = f"SELECT * FROM {self.TABLE_NAME};"

        rezultat = DBUtils.dohvati_podatak(self.sqlConnection, query)
        listaStudenata = []
        i = StudentIndex
        for student in rezultat:
            studentDto = StudentDto.map_data_from_database(student)
            listaStudenata.append(studentDto)

        for s in listaStudenata:
            print(s)

        return listaStudenata

    def dohvati_studenta_po_idu(self, id):
        query = f"SELECT * FROM {self.TABLE_NAME} WHERE id = {id};"

        rezultat = DBUtils.dohvati_podatak(self.sqlConnection, query, True)
        noviStudent = StudentDto.map_data_from_database(rezultat)
        print(noviStudent)