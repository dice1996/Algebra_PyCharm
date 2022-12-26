import tkinter as tk
from screens.FirstScreen import FirstScreen
import sv_ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUI - TODO")
        self.geometry("1000x600")
        self.kreiraj_prvi_prozor()
        sv_ttk.use_light_theme()

    def kreiraj_prvi_prozor(self):
        FirstScreen(self)


DB_NAME = "todo.db"

if __name__ == "__main__":
    app = App()
    app.mainloop()
