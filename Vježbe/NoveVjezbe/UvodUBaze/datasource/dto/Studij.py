

class StudijDto:

    def __init__(self, naziv):
        self.id = None
        self.naziv = naziv

    @staticmethod
    def mapirajIzBaze(studij: tuple):
        studijDto: StudijDto = StudijDto(studij[1])
        studijDto.id = studij[0]

        return studijDto

    def __repr__(self):
        return f"Studij[{self.id}]: {self.naziv}"

