from Drinks import DrinkType


class Restaurant:
    def __init__(self):
        self.dishes = []
        self.drinks = []
        self.orders = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def add_drink(self, drink, dt: DrinkType):
        self.drinks.append(drink)

