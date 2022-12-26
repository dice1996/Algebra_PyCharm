import tkinter as tk
from tkinter import ttk
from tkinter import Frame
from services.CountryService import CountryService, CountryDto


class SecondWindow(tk.Toplevel):
    def __init__(self, MainScreen, var):
        super().__init__(MainScreen)
        self.title('Edit data')
        MainFrame(self, var)


class MainFrame(Frame):
    def __init__(self, topScreen, var):
        super().__init__(topScreen)
        self.topScreen = topScreen
        self.var = var
        self.grid()

        #Frame #1
        self.frame = tk.Frame(self)

        #VAR
        self.country_id = tk.IntVar()
        self.country_name = tk.StringVar()
        self.country_mcc = tk.IntVar()
        self.country_isEurope = tk.BooleanVar()
        #entry
        self.e_country_name = ttk.Entry(self.frame, textvariable=self.country_name)
        self.e_country_mcc = ttk.Entry(self.frame, textvariable=self.country_mcc)
        self.e_country_isEurope = ttk.Checkbutton(self.frame, variable=self.country_isEurope, text='Europe')
        self.save_button = ttk.Button(self.frame, text='Save',
                                      command=lambda: self.save_data(self.country_id.get(), self.country_name.get(), self.country_mcc.get(), self.country_isEurope.get()))
        self.assign_values()

    def assign_values(self):
        self.frame.grid()
        country = CountryService().fetch_by_mcc(self.var)

        self.country_id.set(country.id)
        self.country_name.set(country.name)
        self.country_mcc.set(country.mcc)
        self.country_isEurope.set(country.europe)

        ttk.Label(self.frame, text='Country').grid(row=0, column=0, padx=10, pady=3, sticky='n')
        ttk.Label(self.frame, text='MCC').grid(row=0,column=1, padx=10, pady=3, sticky='n')
        ttk.Label(self.frame, text='Is Europe?').grid(row=0,column=3, padx=10, pady=3, sticky='n')
        self.e_country_name.grid(row=1, column=0, padx=10, pady=10)
        self.e_country_mcc.grid(row=1, column=1, padx=10, pady=10)
        self.e_country_isEurope.grid(row=1, column=2, padx=10, pady=10, sticky='n')
        self.save_button.grid(row=2, column=0, columnspan=5, padx=10, pady=5, sticky="e")
        self.save_button.config(width=80)

    def save_data(self, country_id, country_name, mcc, is_Europe):
        CountryService().update_country(country_id, country_name, mcc, is_Europe)
        self.topScreen.destroy()
