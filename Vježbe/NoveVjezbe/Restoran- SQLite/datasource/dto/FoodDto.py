
TABLE_NAME = "FoodDto"


class FoodDto:
    TABLE_NAME = "Food"

    def __init__(self):
        self.id = None
        self.name = None
        self.price = None

    def add_food_item(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def map_data_from_database(entry: tuple):
        item = FoodDto()
        item.add_food_item(entry[1], entry[2])
        item.id = entry[0]

        return item
