

class UserDto:
    def __init__(self):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.email = None
        self.oib = None
        self.movie_id = None

    def create_user(self, firstname, lastname, email, oib):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.oib = oib
        self.movie_id = None

    @staticmethod
    def map_user_from_database(entry: tuple):
        user = UserDto()
        user.id = entry[0]
        user.firstname = entry[1]
        user.lastname = entry[2]
        user.email = entry[3]
        user.oib = entry[4]
        return user
