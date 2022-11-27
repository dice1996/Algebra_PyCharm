from MenuItems import MenuItems
import itertools


class Dish(MenuItems):
    id = itertools.count(1)

    def __init__(self, name, price):
        super().__init__(name, price)
        self.id = next(self.id)
