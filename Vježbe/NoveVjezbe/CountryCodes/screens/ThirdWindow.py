import tkinter as tk
from tkinter import ttk
from tkinter import Frame
from services.CountryService import CountryService, CountryDto


class ThirdWindow(tk.Toplevel):
    def __init__(self, MainScreen):
        super().__init__(MainScreen)
        self.title('Add/Edit Data')
        MainFrame(self)


class MainFrame(Frame):
    def __init__(self, topScreen):
        super().__init__(topScreen)
        self.topScreen = topScreen
        self.grid()
        self.style = ttk.Style()

        self.country_name = tk.StringVar()
        self.country_mcc = tk.IntVar()
        self.country_isEurope = tk.BooleanVar()

        #GRUPA 1
        self.action_group_1 = tk.LabelFrame(self, text="DOSTUPNE AKCIJE")
        self.action_button_1 = ttk.Button(self.action_group_1, text="PRIKAŽI/OBRIŠI ZEMLJU", width=35, command=self.show_country_list)
        self.action_button_2 = ttk.Button(self.action_group_1, text="DODAJ ZEMLJU", width=35, command=self.show_user_input_screen)

        #GRUA 2
        self.action_group_2 = tk.LabelFrame(self, text="POPIS ZEMALJA")
        self.country_list = ttk.Treeview(self.action_group_2, columns=["id", "name", "mcc", "is_europe"], show='headings')
        self.style.configure("Treeview", rowheight=30, font=('Calibri Light', 13))
        self.style.configure("Treeview.Heading", font=('Calibri Bold', 14))

        self.country_list.bind("<Double-1>", self.delete_line)

        #GRUPA 3
        self.action_group_3 = tk.LabelFrame(self, text="DODAJ ZEMLJU")


        self.show_menu_group()

    def show_menu_group(self):
        self.action_group_1.grid(row=0, column=0, pady=5, padx=5, sticky="ew")
        self.action_button_1.grid(row=0, column=0, pady=5, padx=5, sticky="ew")
        self.action_button_2.grid(row=0, column=1, pady=5, padx=5, sticky="ew")

    def show_country_list(self):
        self.close_action_group()

        self.action_group_2.grid(row=1, column=0, columnspan=5, padx=5, pady=5)
        ttk.Label(self.action_group_2, text="Dvostrukim klikom odaberi zemlju koju brišeš:", font=('', 12)).grid(
            row=1, column=0, padx=5, pady=5, sticky="w")
        self.fill_list()
        self.country_list.grid(row=0, column=0, pady=5, padx=5)

    def fill_list(self):
        self.country_list.heading("id", text="ID")
        self.country_list.heading("name", text="COUNTRY")
        self.country_list.heading("mcc", text="MCC")
        self.country_list.heading("is_europe", text="IS_EUROPE")
        self.country_list.column("id", anchor="center", width=50)
        self.country_list.column("name", anchor="w", width=300)
        self.country_list.column("mcc", anchor="center", width=150)
        self.country_list.column("is_europe", anchor="w", width=100)

        countries = CountryService().fetch_all()

        for i in self.country_list.get_children():
            self.country_list.delete(i)

        for country in countries:
            country: CountryDto
            self.country_list.insert("", "end", text=country.id, values=[country.id, country.name, country.mcc, country.europe])

    def close_action_group(self):
        self.action_group_2.grid_remove()
        self.action_group_3.grid_remove()

    def delete_line(self, event):
        item = self.country_list.selection()[0]
        id = self.country_list.item(item, "text")

        CountryService().delete_country(id)
        self.show_country_list()

    def show_user_input_screen(self):
        self.close_action_group()

        self.action_group_3.grid(row=1, column=0, pady=5, padx=5, sticky="ew")

        ttk.Label(self.action_group_3, text="COUNTRY NAME").grid(row=0, column=0, pady=5, padx=5, sticky="ew")
        ttk.Label(self.action_group_3, text="MCC").grid(row=0, column=1, pady=5, padx=5, sticky="ew")
        ttk.Label(self.action_group_3, text="IS_EUROPE").grid(row=0, column=2, pady=5, padx=5, sticky="ew")

        self.e_country_name = ttk.Entry(self.action_group_3, textvariable=self.country_name, width=35)
        self.e_country_mcc = ttk.Entry(self.action_group_3, textvariable=self.country_mcc, width=35)
        self.e_country_isEurope = ttk.Checkbutton(self.action_group_3, variable=self.country_isEurope, text='Europe')
        self.save_button = ttk.Button(self.action_group_3, text='Save',
                                      command=lambda: self.save_data(self.country_name.get(), self.country_mcc.get(), self.country_isEurope.get()))

        self.e_country_name.grid(row=1, column=0, padx=10, pady=10)
        self.e_country_mcc.grid(row=1, column=1, padx=10, pady=10)
        self.e_country_isEurope.grid(row=1, column=2, padx=10, pady=10, sticky='n')
        self.save_button.grid(row=2, column=0, columnspan=5, padx=10, pady=5, sticky="e")
        self.save_button.config(width=75)

    def save_data(self, name, mcc, isEurope):
        country = CountryDto()
        country.name = name
        country.mcc = mcc
        country.europe = isEurope
        CountryService().insert_data(country)
        self.country_name.set("")
        self.country_mcc.set("")
        self.country_isEurope.set(0)
        self.show_country_list()
