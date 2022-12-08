from utils.DBUtils import DBUtils
from datasource.dto.Student import StudentDto
from datasource.dto.Studij import StudijDto

class UpisService:

    TABLE_NAME = "upis"

    def __init__(self, connection):
        self.connection = connection
        self.kreirajTablicu()

    def kreirajTablicu(self):
        query= f"""
            CREATE TABLE IF NOT EXISTS
                {self.TABLE_NAME} (
                    student_id INTEGER NOT NULL,
                    studij_id INTEGER NOT NULL,
                    FOREIGN KEY (student_id) REFERENCES student(id),
                    FOREIGN KEY (studij_id) REFERENCES studij(id),
                    PRIMARY KEY (student_id, studij_id)
                );
        """
        DBUtils.izvrsiIZapisi(self.connection, query)


    def upisiStudentaNaStudij(self, studentDto: StudentDto, studijDto: StudijDto):
        query = f"""
            INSERT INTO {self.TABLE_NAME} (student_id, studij_id)
            VALUES ({studentDto.id}, {studijDto.id});
        """
        DBUtils.izvrsiIZapisi(self.connection, query)


    def priprema(self):
        query = """
            SELECT * from upis
            JOIN student as s ON upis.student_id=s.id
            JOIN studij ON upis.studij_id=studij.id
            WHERE studij.naziv = 'Matematika';
        """