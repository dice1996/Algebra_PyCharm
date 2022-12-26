import sqlite3
from tkinter import Frame
import tkinter as tk
from tkinter import ttk
import sv_ttk
from services.CountryService import CountryService, CountryDto
from screens.SecondWindow import SecondWindow
from screens.ThirdWindow import ThirdWindow
from PIL import Image, ImageTk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CC")
        sv_ttk.use_dark_theme()
        CountryService()
        CountryService().prefill_database()
        FirstScreen(self)

class FirstScreen(Frame):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)
        self.grid()
        self.style = ttk.Style()

        #Load image
        self.imgEurope = Image.open(r"./img/europe.png")
        self.tkImage = ImageTk.PhotoImage(self.imgEurope)

        #HELPER SCREEN
        self.action_group_1 = tk.Frame(self)
        self.input_text_var = tk.StringVar()
        self.e_input_window = ttk.Entry(self.action_group_1, textvariable=self.input_text_var, justify="center", width=20)
        self.e_input_window.config(state="disabled")
        self.labelEurope = ttk.Label(self.action_group_1, image=self.tkImage)

        #result output
        self.country_label = ttk.Label(self.action_group_1, wraplength=100, justify="center")

        #button_grid
        self.action_group_2 = tk.Frame(self)
        self.show_menu_group()

        #Edit screen
        self.edit_var = tk.IntVar()

    def show_menu_group(self):
        self.action_group_1.grid(row=0, column=0, sticky='news')
        self.e_input_window.grid(row=1, column=0, padx=10, pady=10)

        self.action_group_2.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        keys = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['E', '0', 'R'],
        ]

        for y, row in enumerate(keys, 1):
            for x, key in enumerate(row):
                b = ttk.Button(self.action_group_2, text=key, command=lambda key=key: self.button_press(key))
                b.grid(row=y, column=x, ipadx=10, ipady=10, pady=5, padx=5)
        ttk.Label(self.action_group_2, font=("", 7), text="E - Edit/Add data").grid(row = 6, column=0, columnspan=5, pady=5, padx=5, sticky="w")
        ttk.Label(self.action_group_2, font=("", 7), text="R - Reset").grid(row=6, column=0, columnspan=5, pady=5,
                                                                                padx=5, sticky="e")

    def open_edit_window(self, var):
        window = SecondWindow(self, var)
        window.resizable(False, False)
        window.grab_set()
        self.button_press("R")

    def open_add_delete_window(self):
        window = ThirdWindow(self)
        window.resizable(False, False)
        window.grab_set()

    def show_result(self, country: CountryDto):
        self.country_label.grid_remove()
        if country is not None:
            self.country_label.config(text=f"{country.name} - {country.mcc}")
            if country.europe == 1:
                self.labelEurope.place(anchor="w")
                self.labelEurope.grid(row=3, column=0, pady=5, padx=5, sticky="w")
                self.country_label.grid(row=3, column=0, pady=5, padx=5, sticky="e")
            else:
                self.labelEurope.grid_remove()
                self.country_label.grid(row=3, column=0, pady=5, padx=5, sticky="n")
        else:
            self.labelEurope.grid_remove()
            self.edit_var.set(0)
            self.country_label.config(text= "Country not found!")
            self.country_label.grid(row=3, column=0, pady=5, padx=5, sticky="n")

    def button_press(self, value):
        if value == "R":
            self.input_text_var.set("")
            self.edit_var.set(0)
            self.country_label.grid_remove()
            self.labelEurope.grid_remove()
        elif value == "E":
            if self.edit_var.get() != 0:
                self.open_edit_window(self.edit_var.get())
                self.edit_var.set(0)
            else:
                self.open_add_delete_window()
        else:
            var: str = self.input_text_var.get() + value

            if len(var)>2:
                self.edit_var.set(0)
                self.input_text_var.set(var)
                country = CountryService().fetch_by_mcc(int(var))
                self.edit_var.set(var)
                self.show_result(country)
                self.input_text_var.set("")
            else:
                self.input_text_var.set(var)