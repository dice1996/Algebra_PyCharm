import sqlite3
from tkinter import Frame, messagebox
import tkinter as tk
from tkinter import ttk
import sv_ttk
from services.SmartKeyService import SmartKeyService, SmartKeyDto

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SmartKey")
        #self.geometry("400x400")
        sv_ttk.use_dark_theme()
        SmartKeyService()
        FirstScreen(self)

class FirstScreen(Frame):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)
        self.grid()
        self.style = ttk.Style()

        #Used Variables
        self.ADMIN_PIN = "9529"
        self.list_users = tk.StringVar()
        self.user_id = None

        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.PIN = tk.IntVar()
        self.active = tk.BooleanVar()
        self.keypress = tk.StringVar()

        # First lbFrame
        self.lbFrame = ttk.Labelframe(self, text="Entry")
        self.btn_ring = ttk.Button(self.lbFrame, text = "RING", width=22, command=lambda: messagebox.showinfo("RING RING...RING RING", message="Someone is coming to open the door. Please wait."))
        self.btn_unlock = ttk.Button(self.lbFrame, text="UNLOCK", width=22, command=self.load_unlock_numpad)

        # Second lbFrame
        self.lbFrame2 = ttk.Labelframe(self, text="Enter PIN")
        self.log_screen = tk.Text(self.lbFrame2)
        self.log_screen.config(state="disabled", height=15, width=27)

        # Third lbFrame
        self.lbFrame3 = ttk.Labelframe(self, text="Configuration")
        self.list_view = tk.Listbox(self.lbFrame3, listvariable=self.list_users)
        self.list_view.config(height=15, width=23)
        self.list_view.bind("<<ListboxSelect>>", self.get_id)

        self.e_first_name = ttk.Entry(self.lbFrame3, textvariable=self.first_name)
        self.e_last_name = ttk.Entry(self.lbFrame3, textvariable=self.last_name)
        self.e_PIN = ttk.Entry(self.lbFrame3, textvariable=self.PIN)
        self.cb_active = ttk.Checkbutton(self.lbFrame3, variable=self.active)

        #Load screen
        self.load_screen()

    def allow_entry(self, var):
        self.log_screen.config(state="normal")
        self.log_screen.delete(1.0, "end")
        self.log_screen.config(state="disabled")
        allow, user = SmartKeyService().allow_entry(var)

        if allow:
            self.log_screen.config(state="normal")
            self.log_screen.insert("end", f"Dobrodošao, {user[1]} {user[2]}!")
            self.log_screen.config(state="disabled")
        else:
            self.log_screen.config(state="normal")
            self.log_screen.insert("end", "Pokušaj ponovno s unosom!\nUlazak onemogućen!")
            self.log_screen.config(state="disabled")


    def fill_inputs(self, id):
        try:
            user: SmartKeyDto = SmartKeyService().fetch_by_id(id)
            self.first_name.set(user.first_name)
            self.last_name.set(user.last_name)
            self.PIN.set(user.PIN)
            self.active.set(user.isActive)
        except IndexError:
            pass

    def delete_user(self):
        if self.user_id != None and self.user_id != 0:
            SmartKeyService().delete_user(self.user_id)
            self.clear_all()
        else:
            messagebox.showerror("Error", "Please select valid user!")

    def get_id(self, event):
        try:
            selection = event.widget.curselection()
            user_name = self.users[selection[0]]
            self.user_id = None
            self.user_id = int(user_name.split(".", 1)[0])
            self.fill_inputs(self.user_id)
        except IndexError:
            pass

    def clear_all(self):
        self.first_name.set("")
        self.last_name.set("")
        self.PIN.set("")
        self.active.set(0)
        self.user_id = None
        self.fill_list()

    def check_conditions(self):
        if self.user_id != 0 and self.user_id is not None:
            self.update_user()
            self.clear_all()
        else:
            if self.first_name.get() != "" and self.last_name.get() != "" and self.PIN.get() != "":
                if self.PIN.get()>999:
                    user = SmartKeyDto().create_user(self.first_name.get(), self.last_name.get(), self.PIN.get())
                    SmartKeyService().create_user(user)
                    self.clear_all()
                else:
                    messagebox.showerror("Error", "Please enter a valid PIN!")
            else:
                messagebox.showerror("Error", "Please fill all the fields!")

    def update_user(self):
        SmartKeyService().update_user(self.user_id, self.first_name.get(), self.last_name.get(), self.PIN.get(), self.active.get())

    def load_screen(self):
        self.lbFrame.grid(row=0, column=0, padx=5, pady=5, sticky="ewns")
        self.btn_ring.grid(row=2, column=0,padx=5, pady=5, sticky="w")
        self.btn_unlock.grid(row=2, column=2, padx=5, pady=5, sticky="e")

    def load_unlock_numpad(self):
        self.lbFrame2.grid(row=1, column=0, pady=5, padx=5, sticky="ewns")
        self.log_screen.grid(row=1, column=3, pady=5, padx=5, columnspan=1, rowspan=5, sticky="n")

        keys = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['C', '0'],
        ]

        for y, row in enumerate(keys, 1):
            for x, key in enumerate(row):
                b = ttk.Button(self.lbFrame2, text=key, command=lambda key=key: self.button_press(key))
                b.grid(row=y, column=x, ipadx=10, ipady=10, pady=5, padx=5)
        ttk.Label(self.lbFrame2, font=("", 7), text="C - Clear PIN").grid(row=6, column=0, columnspan=5,
                                                                                    pady=5, padx=5, sticky="w")

    def load_config_screen(self):
        self.lbFrame3.grid(row=2, column=0, pady=5, padx=5, sticky="ewns")
        self.fill_list()
        self.list_view.grid(row=0, column=0, rowspan=5, pady=5, padx=5, sticky="e")

        #Lables
        ttk.Label(self.lbFrame3, text="Ime").grid(row=0, column=1, padx=5, pady=5, sticky="e")
        ttk.Label(self.lbFrame3, text="Prezime").grid(row=1, column=1, padx=5, pady=5, sticky="e")
        ttk.Label(self.lbFrame3, text="PIN (4 broja)").grid(row=2, column=1, padx=5, pady=5, sticky="e")
        ttk.Label(self.lbFrame3, text="Aktivan").grid(row=3, column=1, padx=5, pady=5, sticky="e")
        #Buttons
        ttk.Button(self.lbFrame3, text="Spremi", command=self.check_conditions).grid(row=4, column=1, pady=5, padx=5, sticky="ew")
        ttk.Button(self.lbFrame3, text="Odustani", command=self.clear_all).grid(row=4, column=2, pady=5, padx=5, sticky="ew")
        ttk.Button(self.lbFrame3, text="Izbriši", command=self.delete_user).grid(row=4, column=3, pady=5, padx=5, sticky="ew")
        #Entries
        self.e_first_name.grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky="ew")
        self.e_last_name.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky="ew")
        self.e_PIN.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky="ew")
        self.cb_active.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky="ew")


    def fill_list(self):
        self.users = []
        self.users = SmartKeyService().fetch_users_for_list()
        self.list_users.set(self.users)

    def button_press(self, key):
        if key == "C":
            self.keypress.set("")
            self.lbFrame3.grid_remove()
            self.log_screen.config(state="normal")
            self.log_screen.delete(1.0, "end")
            self.log_screen.config(state="disabled")
        else:
            var: str = self.keypress.get() + key
            self.keypress.set(var)

            if len(var)>3:
                if var == self.ADMIN_PIN:
                    self.load_config_screen()
                    self.keypress.set("")
                else:
                    self.allow_entry(int(var))
                    self.keypress.set("")