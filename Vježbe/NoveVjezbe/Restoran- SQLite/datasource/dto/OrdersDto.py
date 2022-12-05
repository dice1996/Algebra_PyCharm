from enum import Enum


class Payments(Enum):
    CASH = "CASH"
    CARD = "CARD"


class OrdersDto:
    TABLE_NAME = "Orders"

    def __init__(self):
        self.id = None
        self.food_list = None
        self.drinks_list = None
        self.price = None
        self.seats = None
        self.jir = None
        self.payment = None

    def add_order(self, order_food, order_drinks, price):
        self.food_list = order_food
        self.drinks_list = order_drinks
        self.price = price

    @staticmethod
    def map_data_from_database(entry: tuple):
        item = OrdersDto()
        item.id = entry[0]
        item.food_list = entry[1]
        item.drinks_list = entry[2]
        item.price = entry[3]
        item.seats = entry[4]
        item.payment = entry[5]
        item.jir = entry[6]
        return item



