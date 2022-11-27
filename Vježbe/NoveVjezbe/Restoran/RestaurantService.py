from Drinks import DrinkType, Drinks
from Restaurant import Restaurant
from Utils import Utils as utl
from Dish import Dish


class RestaurantService:

    def __init__(self):
        self.restaurant = Restaurant()

    def add_dish(self):
        dish = Dish(input("Insert name of the dish: "), utl.input_number("Insert price: "))
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
        drink = Drinks(input("Insert name of the drink: "), utl.input_number("Insert price: "), selection)
        self.restaurant.add_drink(drink, selection)

    def print_dish(self):
        for d in self.restaurant.dishes:
            print(d)

    def print_drink(self):
        for d in self.restaurant.drinks:
            print(d)

        for d in self.restaurant.alc_drinks:
            print(d)