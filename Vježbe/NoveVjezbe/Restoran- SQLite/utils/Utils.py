import os
import time
import secrets


class Utils:

    @staticmethod
    def print_main_menu(menu: dict):
        for selection in menu.keys():
            print(f"{selection}:\t{menu[selection]}")

        print("_" * 30)

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def menu_selection(menu, title: str):
        while True:
            print(f"{title.upper()}\n")
            Utils.print_main_menu(menu)
            choice = Utils.input_number("\nSelect: ")
            if choice not in menu.keys():
                print("Selection not valid! Try again!")
                time.sleep(2)
                Utils.clear_screen()
            else:
                if choice == 0:
                    Utils.clear_screen()
                    return 0
                else:
                    return choice

    @staticmethod
    def input_number(text=None, index=None):
        while True:
            try:
                if text is None and index is None:
                    return int(input("Input selection: "))
                elif text is None and index is not None:
                    return int(input(f"Input {index}. selection: "))
                else:
                    return float(input(text))
            except:
                print("Input not valid!")

    @staticmethod
    def create_jir():
        return secrets.token_hex(12)

    @staticmethod
    def create_receipt(food_list, drinks_list):
        total = 0
        for item in food_list:
            total += item.price
        for item in drinks_list:
            total += item.price
        return total
