"""
Zadatak 14.
Napisati zadatak za vodenje restorana.

menu podjeliti na segmente:
jela,
alkoholna,
bezalkoholna pića
(dodatne podvrste po želji)

omoguciti unos u meni (svaki od segmenata)
omoguciti narucivanje - vise stvari
izrada racuna prema narudzbi
placanje - keš/kartica
dostupni stolovi - rezervacija - u izdradi

restoran mora cuvati sve racune

sve zamisli za prosirenje aplikacije po izboru.
Rijesavati sa klasama.

osmisliti metodu za fiskalizaciju racuna (neki kod po želji, polu nasumican), racun se fiskalizira kod placanja

"""
from RestaurantService import RestaurantService
from Utils import Utils as utl

main_menu = {

    1: "Input menu item",
    2: "Order",
    3: "Pay order",
    4: "Print order receipt",
    5: "Reservation / Available seats (in progress)",
    0: "Exit"
}

submenu = {
    1: "Input food item",
    2: "Input drink item",
    0: "Back"
}

if __name__ == "__main__":
    service = RestaurantService()

    while True:
        utl.clear_screen()
        selection = utl.menu_selection(main_menu, "main menu")
        if selection == 0:
            break
        elif selection == 1:
            while True:
                utl.clear_screen()
                sub_selection = utl.menu_selection(submenu, "submenu")
                if sub_selection == 0:
                    break
                elif sub_selection == 1:
                    service.add_dish()
                elif sub_selection == 2:
                    service.add_drink()
            continue
        elif selection == 2:
            utl.clear_screen()
            service.crate_order()
        elif selection == 3:
            utl.clear_screen()
            service.create_payment()
        elif selection == 4:
            service.print_receipt()
        elif selection == 5:
            #Nije napravljeno još
            pass
