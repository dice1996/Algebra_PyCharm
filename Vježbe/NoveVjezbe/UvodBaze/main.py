import sqlite3
from utils.DBUtils import DBUtils as utl
from service.StudentService import StudentService
from datasource.dto.Student import StudentDto
from datasource.dto.Studij import StudijDto
from service.StudijService import StudijService

DB_NAME = "Fakultet.db"

# kreiraj_studij_query = '''
#         CREATE TABLE IF NOT EXISTS "Studij" (
# 	    id INTEGER PRIMARY KEY,
# 	    naziv TEXT NOT NULL UNIQUE
# );
# '''

if __name__ == "__main__":
        sqlConnection = sqlite3.connect(DB_NAME)
        studentService = StudentService(sqlConnection)
        studijService = StudijService(sqlConnection)
        #studentService.dodaj_novog_studenta("Pero", "Perić", "pp@gmail.com", "Osijek", "31000")
        # student = StudentDto()
        # student.kreiraj_studenta("Dino", "Cerjak", "dino.cerjak@yahoo.com", "Osijek", "31000")
        # studentService.dodaj_studenta(student)
        # listaStudenata = studentService.dohvati_sve_studente()
        #print(listaStudenata)

        #studijService.dodaj_novi_studij("Matematika")
        # noviStudij = StudijDto("Informatika")
        # studijService.dodaj_studij(noviStudij)

        studijService.dohvati_studije()
        studij = studijService.dohvati_studij_po_idju(2)

        studijService.izmijeni_studij(studij, "Poslovna informatika")
        studijService.dohvati_studije()
