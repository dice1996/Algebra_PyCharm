from tkinter import Frame
import tkinter as tk
from tkinter import  ttk
from PIL import Image, ImageTk

import sv_ttk


class PrviProzor(Frame):
    def __init__(self, mainWindow):
        super().__init__(master=mainWindow)
        self.grid()
        self['relief'] = tk.RAISED
        self['borderwidth'] = 4
        self.toggleProzor2 = False
        sv_ttk.use_light_theme()
        self.kreiraj_prvu_grupu_widgeta()
        self.theme_button = ttk.Button(self, text="Toggle Light/Dark Theme", command=self.toggleTheme)
        self.toggleThemeCondition = True
        self.theme_button.grid()
        self.toggleFlag = False

    def kreiraj_prvu_grupu_widgeta(self):

        imgShow =Image.open(r"./img/show.png")
        imgHide = Image.open(r"./img/hide.png")

        self.prozor1 = tk.LabelFrame(self, text="Login", width=60)
        self.prozor1.grid(row=0, column=0, pady=10, padx=10)

        self.lblUsername = ttk.Label(self.prozor1, text="Username:")
        self.lblUsername.grid(row=0, column=0, pady=5,padx=5)

        self.username = tk.StringVar()
        self.eUsername = ttk.Entry(self.prozor1, textvariable=self.username)
        self.eUsername.grid(row=0, column=1, padx=5, pady=5)

        self.lblPassword = ttk.Label(self.prozor1, text="Password")
        self.lblPassword.grid(row=1, column=0, padx=5, pady=5)

        self.password = tk.StringVar()

        self.ePassword = ttk.Entry(self.prozor1, textvariable=self.password, show="*")
        self.ePassword.grid(row=1, column=1, pady=5, padx=5)

        self.ePassword.bind("<Return>", self.loginEnter)

        self.tkImgShow = ImageTk.PhotoImage(imgShow)
        self.tkImgHide = ImageTk.PhotoImage(imgHide)

        self.btnToggleVisibility = ttk.Button(self.prozor1, image=self.tkImgHide, command=self.promijeniVidljivost)
        self.btnToggleVisibility.grid(row=1, column=2, pady=5, padx=5)

        self.btlLogin = ttk.Button(self.prozor1, text="Login", command=self.login)
        self.btlLogin.grid(row=2, column=0, pady=5, padx=5)

        self.warning = tk.StringVar()

        self.lblWarning = ttk.Label(self.prozor1, textvariable=self.warning)
        self.lblWarning.grid(row=3, column=0, padx=5, pady= 5, columnspan= 2)

    def promijeniVidljivost(self):
        if not self.toggleFlag:
            self.ePassword.config(show="")
            self.btnToggleVisibility.config(image=self.tkImgShow)
            self.toggleFlag = True
        else:
            self.ePassword.config(show="*")
            self.btnToggleVisibility.config(image=self.tkImgHide)
            self.toggleFlag = False

    def login(self):

        self.kreiraj_drugu_grupu_widgeta()
        self.prozor1.grid_remove()

        # print(self.username.get())
        # print(self.password.get())
        #
        # if self.username.get() == "admin" and self.password.get() == "pass":
        #     self.kreiraj_drugu_grupu_widgeta()
        #     self.prozor1.grid_remove()
        # else:
        #     self.warning.set("Username ili password nisu ispravni!")

    def loginEnter(self, event):
        self.login()

    def kreiraj_drugu_grupu_widgeta(self):

        self.prozor2 = tk.LabelFrame(self, text="Grupa 2")
        self.prozor2.grid(row=0, column=0, pady=5, padx=5)

        self.rbOpcija = tk.IntVar()
        self.listaGradova = ["Zagreb", "Osijek"]

        rb1 = ttk.Radiobutton(self.prozor2, text=self.listaGradova[0], variable=self.rbOpcija, value=0, command=self.klikRadioButton)
        rb2 = ttk.Radiobutton(self.prozor2, text=self.listaGradova[1], variable=self.rbOpcija, value=1, command=self.klikRadioButton)
        rb1.grid(row=0, column=0, pady=5, padx=5)
        rb2.grid(row=1, column=0, padx=5, pady=5)

        self.odabraniGrad = tk.StringVar()
        cbGradovi = ttk.Combobox(self.prozor2, textvariable=self.odabraniGrad)
        cbGradovi.grid(row=2, column=0, padx=5, pady=5)

        cbGradovi.state(["readonly"])
        cbGradovi['values'] = ('Osijek', 'Zagreb', 'Rijeka', 'Split')

        cbGradovi.bind("<<ComboboxSelected>>", self.provjeriGrad)

        self.korisnici = []
        for i in range(100):
            self.korisnici.append(f"Korisnik {i + 1}")

        self.listaKorisnika = tk.StringVar(value=self.korisnici)
        lbKorisnici = tk.Listbox(self.prozor2, listvariable=self.listaKorisnika)
        lbKorisnici.grid(row=3, column=0, pady=5, padx=5)

        #lbKorisnici.bind("<<ListboxSelect>>", self.listaOdabir)
        lbKorisnici.bind("<Double-1>", self.listaOdabir)

        self.checkBox1 = tk.BooleanVar()
        cbPrvi = ttk.Checkbutton(self.prozor2, text = "Prvi check", variable=self.checkBox1, command=self.provjeriCheckButtone)
        cbPrvi.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.checkBox2 = tk.BooleanVar()
        cbDrugi = ttk.Checkbutton(self.prozor2, text="Drugi check", variable=self.checkBox2, command=self.provjeriCheckButtone)
        cbDrugi.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        self.log = tk.Text(self.prozor2)
        self.log.grid(row=0, column=1, pady=6, padx=5, rowspan=6)
        self.log.config(state="disabled")

        self.input = tk.StringVar()
        eInput = ttk.Entry(self.prozor2, textvariable=self.input)
        eInput.grid(row=7, column=1, padx=5, pady=5, sticky="ew")

        eInput.bind("<Return>", self.zapisiLog)


    def zapisiLog(self, event):
        self.log.config(state="normal")
        self.log.insert("end", self.input.get() + "\n")
        self.input.set("")
        self.log.config(state="disabled")

    def listaOdabir(self, event):
        odabir = event.widget.curselection()
        print(self.korisnici[odabir[0]])

    def provjeriCheckButtone(self):
        print(f"CB1: {self.checkBox1.get()}")
        print(f"CB2: {self.checkBox2.get()}")

    def provjeriGrad(self, event):
        print(event)
        print(self.odabraniGrad.get())

    def klikRadioButton(self):
        print(self.listaGradova[self.rbOpcija.get()])

    def toggleTheme(self):
        if not self.toggleThemeCondition:
            sv_ttk.use_light_theme()
            self.toggleThemeCondition = True
        else:
            sv_ttk.use_dark_theme()
            self.toggleThemeCondition = False
