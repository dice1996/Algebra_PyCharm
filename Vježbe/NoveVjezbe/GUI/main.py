import tkinter as tk
from tkinter import ttk
from screens.PrviProzor import PrviProzor
import sv_ttk

# root = tk.Tk()
# root.title("Python Developer")
# root.geometry("1000x600")
#
# label = ttk.Label(root, text="labela primjer")
# label.grid(row=0,column=0, padx=10,  pady=10, sticky="w")
#
# label2 = ttk.Label(root, text="labela primjer s malo dužim tekstom")
# label2.grid(row=1,column=0, padx=10,  pady=10)
#
# unos = ttk.Entry(root)
# unos.grid(row=0, column=1, pady=10)
#
# gumb = ttk.Button(root, text="Spremi")
# gumb.grid(row=1, column=1, pady=10)
#
# text = tk.Text(root, width=80, height=10)
# text.grid(row=2, column=0, pady=10, columnspan=2, rowspan=5)
#
# root.mainloop()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Developer")
        self.geometry("1000x600")
        self.kreiraj_prvi_prozor()


    def kreiraj_prvi_prozor(self):
        PrviProzor(self)



if __name__ == "__main__":
    app = App()
    app.mainloop()