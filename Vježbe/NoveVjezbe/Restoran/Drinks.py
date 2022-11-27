from enum import Enum
from MenuItems import MenuItems
import itertools


class DrinkType(Enum):
    alcoholic = "ALCOHOLIC"
    regular = "REGULAR"


class Drinks(MenuItems):
    id = itertools.count(1)

    def __init__(self, name, price, dt: DrinkType):
        super().__init__(name, price)
        self.id = next(self.id)
        self.type = dt
