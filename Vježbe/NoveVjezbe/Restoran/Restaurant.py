from Drinks import DrinkType


class Restaurant:
    def __init__(self):
        self.dishes = []
        self.alc_drinks = []
        self.drinks = []
        self.orders = []
        self.receipts = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def add_drink(self, drink, dt: DrinkType):
        if dt is DrinkType.regular:
            self.drinks.append(drink)
        elif dt is DrinkType.alcoholic:
            self.alc_drinks.append(drink)

