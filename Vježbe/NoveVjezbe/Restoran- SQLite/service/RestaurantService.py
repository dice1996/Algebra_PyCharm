import time

from prettytable import PrettyTable, ALL
from datasource.dto.FoodDto import FoodDto
from datasource.dto.DrinksDto import DrinkType, DrinksDto
from service.FoodService import FoodService
from service.DrinksService import DrinksService
from service.OrderServce import OrdersService
from service.TablesService import TablesService
from utils.Utils import Utils as utl
from datasource.dto.OrdersDto import OrdersDto, Payments


class RestaurantService:

    def __init__(self, sqlConnection):
        self.sqlConnection = sqlConnection
        TablesService(sqlConnection)

    def add_food_item(self):
        name = input("Insert name of the dish: ")
        price = utl.input_number("Insert price (in €): ")
        FoodService(self.sqlConnection).add_food_item(name, price)
        print(f"{name} successfully added to menu.")
        time.sleep(2)

    def add_drink_item(self):
        print("Select drink type by inputting a number of a selection\n1: Alcoholic\n2: Regular")
        while True:
            selection = utl.input_number("Your selection: ")
            if selection == 1:
                selection = DrinkType.alcoholic.value
                break
            elif selection == 2:
                selection = DrinkType.regular.value
                break
            else:
                print("Try again, not correct input!")
        DrinksService(self.sqlConnection).add_drink_item(input("Insert name of the drink: "),
                                                         input("Insert price (in €): "), selection)
        print(f"Drink successfully added to menu.")
        time.sleep(2)

    def print_menu_items(self, food=True):
        if food is True:
            menu_list = FoodService(self.sqlConnection).fetch_food_items()
            print("FOOD")
            t = PrettyTable(["FOOD ID", "FOOD NAME", "FOOD PRICE (in €)"], padding_width=3, hrules=ALL)
        elif food is False:
            menu_list = DrinksService(self.sqlConnection).fetch_drink_items()
            print("DRINKS")
            t = PrettyTable(["DRINK ID", "DRINK NAME", "DRINK PRICE (in €)", "DRINK TYPE"], padding_width=3, hrules=ALL)
        for item in menu_list:
            if food is True:
                t.add_row([item.id, item.name, item.price])
            elif food is False:
                t.add_row([item.id, item.name, item.price, item.type])
        print(f"{t}\n")

    def crate_order(self):
        utl.clear_screen()
        print("Create your order in few easy steps!\n")
        self.print_menu_items()
        counter = 1
        food = []
        drinks = []
        while True:
            flag = False
            selection = int(utl.input_number(f"Choose you {counter}. item (to skip, press 0): "))
            menu_list = FoodService(self.sqlConnection).fetch_food_items()
            if selection == 0:
                print("Skipping food!")
                break
            else:
                for item in menu_list:
                    if item.id == selection:
                        print(f"{counter}. item added to a list.")
                        food.append(item)
                        counter += 1
                        flag = True
                if not flag:
                    print("ID does not exists! Try again!")
        utl.clear_screen()
        self.print_menu_items(False)
        counter = 1
        while True:
            flag = False
            menu_list = DrinksService(self.sqlConnection).fetch_drink_items()
            selection = int(utl.input_number(f"Choose you {counter}. item (to skip, press 0): "))
            if selection == 0:
                print("Skipping drinks!")
                break
            else:
                for item in menu_list:
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
            price, row_id = OrdersService(self.sqlConnection).add_order(food, drinks)
            print(f"Order ID is {row_id} and total amount to pay is {price}€.")
            time.sleep(2)
            utl.clear_screen()

    def print_open_orders(self):
        print("OPEN ORDERS\nBelow is a list of open orders that are awaiting payment.")
        t = PrettyTable(["ORDER ID", "ORDER PRICE (in €)", "TABLE", "STATUS"], padding_width=3, hrules=ALL)
        orders = OrdersService(self.sqlConnection).fetch_open_orders()
        for item in orders:
            item: OrdersDto
            t.add_row([item.id, item.price, "None", "OPEN"])
        print(f"{t}\n")

    def create_payment(self):
        self.print_open_orders()
        orders = OrdersService(self.sqlConnection).fetch_open_orders()
        selection = utl.input_number("Input order ID you wish to pay (to cancel input 0): ")
        if selection == 0:
            print("Payment canceled. Returning to main menu...")
            time.sleep(2)
        else:
            for item in orders:
                item: OrdersDto
                if int(item.id) == selection:
                    print("Select payment type by entering ID:\n1: CASH\n2: CARD")
                    while True:
                        pt = utl.input_number("Your selection: ")
                        if pt == 1:
                            pt = Payments.CASH.value
                            break
                        elif pt == 2:
                            pt = Payments.CARD.value
                            break
                        else:
                            print("Try again, not correct input!")
                    OrdersService(self.sqlConnection).order_payment(selection, pt, utl.create_jir())
                    print("Payment successful. Returning to main menu...")
                    time.sleep(2)
                elif int(item.id) == selection:
                    print("Order does not exists. returning to main manu...")
                    time.sleep(2)
