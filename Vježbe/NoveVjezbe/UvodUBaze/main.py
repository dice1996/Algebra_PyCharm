import sqlite3
from utils.DBUtils import DBUtils
from service.StudentService import StudentService
from datasource.dto.Student import StudentDto
from service.StudijService import StudijService
from datasource.dto.Studij import StudijDto
from service.UpisService import UpisService

DB_NAME = "Fakultet.db"

if __name__ == '__main__':
    sqlConnection = sqlite3.connect(DB_NAME)
    studentService = StudentService(sqlConnection)
    studijService = StudijService(sqlConnection)
    upisService = UpisService(sqlConnection)

    # studentService.dodajNovogStudenta("Pero",
    #                                   "Peric",
    #                                   "pperic@gmail.com",
    #                                   "10000",
    #                                   "Zagreb"
    #                                   )
    # student = StudentDto()
    # student.kreirajStudenta("Ana",
    #                         "Anic",
    #                         "aanic@gmail.com",
    #                         "51000",
    #                         "Rijeka")
    #
    # studentService.dodajStudenta(student)
    # listaStudenata = studentService.dohvatiSveStudente()
    # studentService.dohvatiStudentaPoIDu(3)

    # studijService.dodajNoviStudij("Informatika")
    # noviStudij = StudijDto("Matematika")
    # studijService.dodajStudij(noviStudij)
    #studijService.dohvatiSveStudije()
    #print(studijService.dohvatiStudijPoIDu(2))
    # informatikaDto = studijService.dohvatiStudijPoNazivu("Informatika")
    # informatikaDto = studijService.dohvatiStudijPoNazivu("Poslovna informatika")
    #novaInformatika = studijService.izmjeniStudij(informatikaDto, "Informatika")
    #print(novaInformatika)
    # studijService.izbrisiStudijPoIDu(1)
    #studijService.dohvatiSveStudije()
    # studentService.dohvatiSveStudente()
    studentPero = studentService.dohvatiStudentaPoIDu(3)
    studenticaAna = studentService.dohvatiStudentaPoIDu(4)

    studijInformatika = studijService.dohvatiStudijPoIDu(3)
    studijMatematika = studijService.dohvatiStudijPoIDu(2)

    upisService.upisiStudentaNaStudij(studentPero, studijMatematika)
    upisService.upisiStudentaNaStudij(studenticaAna, studijInformatika)
    upisService.upisiStudentaNaStudij(studenticaAna, studijMatematika)





















