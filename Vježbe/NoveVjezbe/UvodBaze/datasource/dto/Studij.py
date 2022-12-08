

class StudijDto:

    def __init__(self, naziv):
        self.id = None
        self.naziv = naziv

    @staticmethod
    def map_data_from_database(entry: tuple):
        studij = StudijDto(entry[1])
        studij.id = entry[0]

        return studij

    def __repr__(self):
        return f"Studij [{self.id}]: {self.naziv}"