from datasource.dto.FoodDto import FoodDto
from enum import Enum


class DrinkType(Enum):
    alcoholic = "ALCOHOLIC"
    regular = "REGULAR"


class DrinksDto(FoodDto):
    TABLE_NAME = "Drinks"

    def __init__(self):
        super().__init__()
        self.type: DrinkType = None

    def add_drink_item(self, name, price, dt: DrinkType):
        self.name = name
        self.price = price
        self.type = dt

    @staticmethod
    def map_data_from_database(entry: tuple):
        item = DrinksDto()
        item.add_drink_item(entry[1], entry[2], entry[3])
        item.id = entry[0]

        return item
