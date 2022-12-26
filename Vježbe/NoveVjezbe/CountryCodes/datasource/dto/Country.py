class CountryDto:
    def __init__(self):
        self.id = None
        self.name = None
        self.mcc = None
        self.europe = 0

    def create_country(self, name, mcc, europe):
        self.name = name
        self.mcc = mcc
        self.europe = europe
        return self

    @staticmethod
    def map_data_from_database(entry: tuple):
        country = CountryDto()
        country.id = entry[0]
        country.name = entry[1]
        country.mcc = entry[2]
        country.europe = entry[3]
        return country

    def __repr__(self):
        return f"CountryDto(id={self.id}, name={self.name}, europe={self.europe}, mcc={self.mcc})"
