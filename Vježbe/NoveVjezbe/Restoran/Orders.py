import itertools
from enum import Enum
from Dish import Dish
from Drinks import Drinks


class PaymentType(Enum):
    CASH = "CASH"
    CARD = "CARD"


class Orders:
    id = itertools.count(1000)

    def __init__(self, order_food: list, order_drinks: list):
        self.id = next(self.id)
        self.food = order_food
        self.drinks = order_drinks
        self.receipt_total = self.create_receipt()
        self.jir = None
        self.payment: PaymentType = None

    def create_receipt(self):
        total = 0

        for item in self.food:
            total += item.price
        for item in self.drinks:
            total += item.price

        return total

    def __repr__(self):
        model = {
            "id": self.id,
            "food": self.food,
            "drinks": self.drinks,
            "total": self.receipt_total,
            "payment_type": self.payment,
            "JIR": self.jir
        }

        return str(model)
