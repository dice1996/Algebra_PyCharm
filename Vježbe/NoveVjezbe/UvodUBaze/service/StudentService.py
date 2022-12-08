from utils.DBUtils import DBUtils
from datasource.dto.Student import StudentDto
from enum import Enum

class StudentIndex(Enum):
    ID = 0
    IME = 1
    PREZIME = 2
    EMAIL = 3
    ZIP = 4
    GRAD = 5


class StudentService:

    TABLE_NAME = "student"

    def __init__(self, connection):
        self.sqlConnection = connection
        self.kreirajTablicu()


    def kreirajTablicu(self):
        query = f'''
            CREATE TABLE IF NOT EXISTS
                {self.TABLE_NAME} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ime VARCHAR(30) NOT NULL,
                    prezime VARCHAR(30) NOT NULL,
                    email VARCHAR(60) NOT NULL UNIQUE,
                    zip VARCHAR(5) NOT NULL,
                    grad VARCHAR(30) NOT NULL
                );
        '''

        DBUtils.izvrsiIZapisi(self.sqlConnection, query)

    def dodajNovogStudenta(self, ime, prezime, email, zip, grad):
        query = f'''
            INSERT INTO {self.TABLE_NAME} (ime, prezime, email, zip, grad)
            VALUES("{ime}", "{prezime}", "{email}", "{zip}", "{grad}");
        '''

        DBUtils.izvrsiIZapisi(self.sqlConnection, query)

    def dodajStudenta(self, student: StudentDto):
        self.dodajNovogStudenta(student.ime,
                                student.prezime,
                                student.email,
                                student.zip,
                                student.grad
                                )


    def dohvatiSveStudente(self):
        query = f"SELECT * FROM {self.TABLE_NAME};"

        rezultat = DBUtils.dohvatiPodatke(self.sqlConnection, query)
        print(rezultat)
        listaStudenata = []
        for student in rezultat:
            studentDto = StudentDto()
            i = StudentIndex
            studentDto.kreirajStudenta(student[i.IME.value], student[i.PREZIME.value],
                                       student[i.EMAIL.value], student[i.ZIP.value],
                                       student[i.GRAD.value])
            studentDto.id = student[i.ID.value]
            listaStudenata.append(studentDto)

        for s in listaStudenata:
            print(s)
        return listaStudenata

    def dohvatiStudentaPoIDu(self, id):
        query = f"SELECT * FROM {self.TABLE_NAME} WHERE id={id};"
        rezultat = DBUtils.dohvatiPodatke(self.sqlConnection, query, one=True)
        noviStudent = StudentDto.mapirajIzBaze(rezultat)
        return noviStudent





