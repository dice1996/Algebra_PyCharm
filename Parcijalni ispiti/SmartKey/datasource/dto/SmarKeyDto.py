
class SmartKeyDto:
    def __init__(self):
        self.id = None
        self.first_name = None
        self.last_name = None
        self.PIN = None
        self.isActive = 1

    def create_user(self, first_name, last_name, PIN):
        self.first_name = first_name
        self.last_name = last_name
        self.PIN = PIN
        return self

    @staticmethod
    def map_data_from_database(entry: tuple):
        user = SmartKeyDto()
        user.id = entry[0]
        user.first_name = entry[1]
        user.last_name = entry[2]
        user.PIN = entry[3]
        user.isActive = entry[4]
        return user

