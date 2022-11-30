

class StudentDto:
    def __init__(self):
        self.id = None
        self.ime = None
        self.prezime = None
        self.email = None
        self.grad = None
        self.zip = None

    def kreiraj_studenta(self, ime, prezime, email, grad, zip):
        self.ime = ime
        self.prezime = prezime
        self.email = email
        self.grad = grad
        self.zip = zip

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def map_data_from_database(entry: tuple):
        studentDto = StudentDto()
        studentDto.kreiraj_studenta(entry[1], entry[2], entry[3], entry[4], entry[5])
        studentDto.id = entry[0]

        return studentDto