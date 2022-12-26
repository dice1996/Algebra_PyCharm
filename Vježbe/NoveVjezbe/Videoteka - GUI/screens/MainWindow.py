import sqlite3
from tkinter import Frame
import tkinter as tk
from tkinter import ttk
import sv_ttk
from service.VideotekaService import VideotekaService
from datasource.dto.Movie import MovieDto

DB_NAME = "videoteka.db"


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("VIDEOTEKA -GUI")
        sv_ttk.use_dark_theme()
        VideotekaService()
        FirstScreen(self)


class FirstScreen(Frame):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)
        self.pack()
        self.style = ttk.Style()

        #prva grupa akcija - gumbi akcija
        self.action_group_1 = tk.LabelFrame(self, text="VIDEOTEKA - AKCIJE")
        self.action_button_1 = ttk.Button(self.action_group_1, text="POSUDI FILM", width=30, command=self.rent_movie)
        self.action_button_2 = ttk.Button(self.action_group_1, text="VRATI FILM", width=30)
        self.action_button_3 = ttk.Button(self.action_group_1, text="DODAJ KORISNIKA", width=30, command=self.show_user_input_screen)
        self.action_button_4 = ttk.Button(self.action_group_1, text="UNESI FILM", width=30, command=self.show_movie_input_screen)
        self.action_button_5 = ttk.Button(self.action_group_1, text="PRIKAŽI POVIJEST", width=30)

        #druga grupa - izdavanje filma
        self.action_group_2 = tk.LabelFrame(self, text="VIDEOTEKA - AKCIJA POSUDI FILM")
        self.movie_list = ttk.Treeview(self.action_group_2, columns=["id", "name", "year", "director", "status"], show='headings')
        self.style.configure("Treeview", rowheight = 30, font = ('Calibri Light', 13))
        self.style.configure("Treeview.Heading", font=('Calibri Bold', 14))

        #treća grupa - unos filma
        self.action_group_3 = tk.LabelFrame(self, text="VIDEOTEKA - AKCIJA UNOS FILMA")
        self.movie_name = tk.StringVar()
        self.movie_year = tk.IntVar()
        self.movie_director = tk.StringVar()
        self.movie_status = tk.IntVar()
        self.e_movie_name = ttk.Entry(self.action_group_3, textvariable=self.movie_name, width=45)
        self.e_movie_year = ttk.Entry(self.action_group_3, textvariable=self.movie_year, width=30)
        self.e_movie_director = ttk.Entry(self.action_group_3, textvariable=self.movie_director, width=45)
        self.action_button_6 = ttk.Button(self.action_group_3, text="SPREMI FILM", width=36, command=self.save_movie)

        #četvrta grupa - unos korisnika
        self.action_group_4 = tk.LabelFrame(self, text="VIDEOTEKA - AKCIJA DODAJ KORISNIKA")
        self.user_firstname = tk.StringVar()
        self.user_lastname = tk.StringVar()
        self.user_email = tk.StringVar()
        self.user_oib = tk.IntVar()
        self.e_user_firstname = ttk.Entry(self.action_group_4, textvariable=self.user_firstname, width=30)
        self.e_user_lastname = ttk.Entry(self.action_group_4, textvariable=self.user_lastname, width=30)
        self.e_user_email = ttk.Entry(self.action_group_4, textvariable=self.user_email, width=30)
        self.e_user_oib = ttk.Entry(self.action_group_4, textvariable=self.user_oib, width=31)
        self.action_button_7 = ttk.Button(self.action_group_4, text="DODAJ KORISNIKA", command=self.save_user, width=31)

        self.show_menu_group()

    def show_menu_group(self):
        self.action_group_1.grid(row=0, column=0, pady=5, padx=5, sticky="ew")
        self.action_button_1.grid(row=0, column=0, pady=5, padx=5, sticky="ew")
        self.action_button_2.grid(row=0, column=1, pady=5, padx=5, sticky="ew")
        self.action_button_3.grid(row=0, column=2, pady=5, padx=5, sticky="ew")
        self.action_button_4.grid(row=0, column=3, pady=5, padx=5, sticky="ew")
        self.action_button_5.grid(row=0, column=4, pady=5, padx=5, sticky="ew")

    def show_rent_movie_screen(self):
        self.close_action_group()

        self.action_group_2.grid(row=1, column=0, columnspan=5, padx=5, pady=5)
        ttk.Label(self.action_group_2, text="Dvostrukim klikom odaberi film koji želiš posuditi:", font=('', 12)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.fill_movie_list()
        self.movie_list.grid(row=0, column=0, pady=5, padx=5)

    def show_movie_input_screen(self):
        self.close_action_group()
        self.action_group_3.grid(row=1, column=0, pady=5, padx=5, sticky="ew")
        ttk.Label(self.action_group_3, text="FILM").grid(row=0, column=0, pady=5, padx=5, sticky="ew")
        ttk.Label(self.action_group_3, text="GODINA").grid(row=0, column=1, pady=5, padx=5, sticky="ew")
        ttk.Label(self.action_group_3, text="REDATELJ").grid(row=0, column=2, pady=5, padx=5, sticky="ew")
        ttk.Label(self.action_group_3, text="Unesi podatke za film. Pazi da je godina u brojčanom formatu!").grid(
            row=2, column=0, columnspan=5, pady=5, padx=5, sticky="ew")
        self.e_movie_name.grid(row=1, column=0, pady=5, padx=5, sticky="ew")
        self.movie_year.set("")
        self.e_movie_year.grid(row=1, column=1, pady=5, padx=5, sticky="ew")
        self.e_movie_director.grid(row=1, column=2, pady=5, padx=5, sticky="ew")
        self.action_button_6.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

    def show_user_input_screen(self):
        self.close_action_group()
        self.action_group_4.grid(row=1, column=0, pady=5, padx=5, sticky="ew")
        self.user_oib.set("")
        ttk.Label(self.action_group_4, text="IME").grid(row=0, column=0, pady=5, padx=5, sticky="ew")
        ttk.Label(self.action_group_4, text="PREZIME").grid(row=0, column=1, pady=5, padx=5, sticky="ew")
        ttk.Label(self.action_group_4, text="EMAIL").grid(row=0, column=2, pady=5, padx=5, sticky="ew")
        ttk.Label(self.action_group_4, text="OIB").grid(row=0, column=3, pady=5, padx=5, sticky="ew")
        ttk.Label(self.action_group_4, text="Unesi podatke za korisnika. Pazi da je OIB u brojčanom formatu!").grid(row=2, column=0, columnspan=5, pady=5, padx=5, sticky="ew")
        self.e_user_firstname.grid(row=1, column=0, pady=5, padx=5, sticky="ew")
        self.e_user_lastname.grid(row=1, column=1, pady=5, padx=5, sticky="ew")
        self.e_user_email.grid(row=1, column=2, pady=5, padx=5, sticky="ew")
        self.e_user_oib.grid(row=1, column=3, pady=5, padx=5, sticky="ew")
        self.action_button_7.grid(row=1, column=4, pady=5, padx=5, sticky="ew")

    def fill_movie_list(self):
        self.movie_list.heading("id", text="ID")
        self.movie_list.heading("name", text="FILM")
        self.movie_list.heading("year", text="GODINA")
        self.movie_list.heading("director", text="REDATELJ")
        self.movie_list.heading("status", text="STATUS")
        self.movie_list.column("id", anchor="center", width=100)
        self.movie_list.column("name", anchor="w", width=500)
        self.movie_list.column("year", anchor="center", width=150)
        self.movie_list.column("director", anchor="w", width=500)
        self.movie_list.column("status", anchor="center", width=100)
        self.movie_list.columnconfigure(0, weight=1)
        self.movie_list.configure(height=15)
        self.load_available_movies()

    def rent_movie(self):
        self.show_rent_movie_screen()
        self.movie_list.bind("<Double-1>", self.return_movie_id)

    def return_movie_id(self, event):
        item = self.movie_list.selection()[0]
        id = self.movie_list.item(item, "text")
        self.selected_movie_id = id

    def close_action_group(self):
        self.action_group_2.grid_remove()
        self.action_group_3.grid_remove()
        self.action_group_4.grid_remove()

    def save_user(self):
        pass

    def save_movie(self):
        try:
            message = VideotekaService().create_movie(self.movie_name.get(), self.movie_year.get(), self.movie_director.get())
            ttk.Label(self.action_group_3, text=message).grid(row=2, column=3, padx=5, pady=5, sticky="w")
            self.movie_name.set("")
            self.movie_year.set("")
            self.movie_director.set("")
        except:
            ttk.Label(self.action_group_3, text="Pogrešno je upisana godina!").grid(row=2, column=3, padx=5, pady=5, sticky="ew")
        #self.close_action_group()

    def load_available_movies(self):
        movies = VideotekaService().show_available_movies()
        # očisti listu filmova
        for i in self.movie_list.get_children():
            self.movie_list.delete(i)
        # dodaj film na listu za ispis
        for movie in movies:
            movie: MovieDto
            self.movie_list.insert('', tk.END, text=movie.id, values=[movie.id, movie.name, movie.year, movie.director, movie.status])

