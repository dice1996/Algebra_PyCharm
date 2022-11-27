import time

from Drinks import DrinkType, Drinks
from Restaurant import Restaurant
from Utils import Utils as utl
from Dish import Dish
from Orders import Orders, PaymentType
from prettytable import PrettyTable, ALL


class RestaurantService:

    def __init__(self):
        self.restaurant = Restaurant()

    def add_dish(self):
        dish = Dish(input("Insert name of the dish: "), utl.input_number("Insert price (in €): "))
        self.restaurant.add_dish(dish)

    def add_drink(self):
        print("Select drink type by inputting a number of a selection\n1: Alcoholic\n2: Regular")
        while True:
            selection = utl.input_number("Your selection: ")
            if selection == 1:
                selection = DrinkType.alcoholic
                break
            elif selection == 2:
                selection = DrinkType.regular
                break
            else:
                print("Try again, not correct input!")
        drink = Drinks(input("Insert name of the drink: "), utl.input_number("Insert price (in €): "), selection)
        self.restaurant.add_drink(drink)

    def print_drink_items(self):
        print("DRINKS")
        t = PrettyTable(["DRINK ID", "DRINK NAME", "DRINK PRICE (in €)", "DRINK TYPE"], padding_width=3, hrules=ALL)
        for item in self.restaurant.drinks:
            item: Drinks
            t.add_row([item.id, item.name, item.price, item.type.value])
        print(f"{t}\n")

    def print_food_items(self):
        print("FOOD")
        t = PrettyTable(["FOOD ID", "FOOD NAME", "FOOD PRICE (in €)"], padding_width=3, hrules=ALL)
        for item in self.restaurant.dishes:
            item: Dish
            t.add_row([item.id, item.name, item.price])
        print(f"{t}\n")

    def print_open_orders(self):
        print("OPEN ORDERS\nBelow is a list of open orders that are awaiting payment.")
        t = PrettyTable(["ORDER ID", "ORDER PRICE (in €)", "STATUS"], padding_width=3, hrules=ALL)
        for item in self.restaurant.orders:
            item: Orders
            if item.jir is None:
                t.add_row([item.id, item.receipt_total, "OPEN"])
        print(f"{t}\n")

    def crate_order(self):
        utl.clear_screen()
        print("Create your order in few easy steps!\n")
        self.print_food_items()
        counter = 1
        food = []
        drinks = []
        while True:
            flag = False
            selection = int(utl.input_number(f"Choose you {counter}. item (to skip, press 0): "))
            if selection == 0:
                print("Skipping food!")
                break
            else:
                for item in self.restaurant.dishes:
                    if int(item.id) == selection:
                        print(f"{counter}. item added to a list.")
                        food.append(item)
                        counter += 1
                        flag = True

                if not flag:
                    print("ID does not exists! Try again!")

        utl.clear_screen()
        self.print_drink_items()
        counter = 1
        while True:
            flag = False
            selection = int(utl.input_number(f"Choose you {counter}. item (to skip, press 0): "))
            if selection == 0:
                print("Skipping drinks!")
                break
            else:
                for item in self.restaurant.drinks:
                    if int(item.id) == selection:
                        print(f"{counter}. item added to a list.")
                        drinks.append(item)
                        counter += 1
                        flag = True
                if not flag:
                    print("ID does not exists! Try again!")
        if food == [] and drinks == []:
            print("No items added. Skipping order!")
        else:
            order = Orders(food, drinks)
            print(f"Order ID is {order.id} and total amount to pay is {order.receipt_total}€.")
            self.restaurant.add_order(order)
            time.sleep(2)
            utl.clear_screen()

    def create_payment(self):
        self.print_open_orders()
        selection = utl.input_number("Input order ID you wish to pay (to cancel input 0): ")
        if selection == 0:
            print("Payment canceled. Returning to main menu...")
            time.sleep(2)
        else:
            for item in self.restaurant.orders:
                item: Orders
                if int(item.id) == selection:
                    print("Select payment type by entering ID:\n1: CASH\n2: CARD")
                    while True:
                        pt = utl.input_number("Your selection: ")
                        if pt == 1:
                            pt = PaymentType.CASH
                            break
                        elif pt == 2:
                            pt = PaymentType.CARD
                            break
                        else:
                            print("Try again, not correct input!")
                    item.jir = utl.create_jir()
                    item.payment = pt
                    print("Payment successful. Returning to main menu...")
                    time.sleep(2)
                else:
                    print("Order does not exists. returning to main manu...")
                    time.sleep(2)
