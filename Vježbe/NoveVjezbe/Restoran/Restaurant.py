from Drinks import DrinkType


class Restaurant:
    def __init__(self):
        self.dishes = []
        self.drinks = []
        self.orders = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def add_drink(self, drink):
        self.drinks.append(drink)

    def add_order(self, order):
        self.orders.append(order)

