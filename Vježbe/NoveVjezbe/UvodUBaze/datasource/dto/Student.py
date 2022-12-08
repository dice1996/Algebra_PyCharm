

class StudentDto:

    def __init__(self):
        self.id = None
        self.ime = None
        self.prezime = None
        self.email = None
        self.zip = None
        self.grad = None

    def kreirajStudenta(self, ime, prezime, email, zip, grad):
        self.ime = ime
        self.prezime = prezime
        self.email = email
        self.zip = zip
        self.grad = grad

    @staticmethod
    def mapirajIzBaze(student: tuple):
        studentDto = StudentDto()
        studentDto.kreirajStudenta(student[1], student[2],
                                   student[3], student[4],
                                   student[5])
        studentDto.id = student[0]
        return studentDto



    def __repr__(self):
        return str(self.__dict__)
