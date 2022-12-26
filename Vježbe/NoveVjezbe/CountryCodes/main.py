"""
Napraviti aplikaciju s grafickim suceljem.

Aplikacija treba imati bazu podataka sa spremljenom drzavom i mcc-om (mobile country code)
te sadrzavati informaciju da li je drzava Europe ili nije.
npr Hrvatska | 385 | je drzava europe, Canada 302 nije drzava europe
arhitektura baze je proizvoljna i pozeljno je da je napravljena u pythonu. (slobodno koristiti utilse)
Unesite podatke za 10 drzava.

sucelje se sastoji od ispisa 3 znamenke koje unosimo preko tipkovnice iz grafickog sucelja

sucelje se sastoji od 10 tipka (0-9) i tipke reset

 | X Y Z |

[1] [2] [3]
[4] [5] [6]
[7] [8] [9]
    [0]
[  reset  ]

preko virtualne tipkovnice unosite 3 broja koji se zapisuju u ispis XYZ prikazan gore

nakon sto su upisane 3 znamenke ako mcc postoji u bazi ispisu se podaci o drzavi,
ako mcc nije ispravan ime drzave se ispise "Unknown".
ako je drzava iz Europe, pokraj naziva se prikaze slika "europe.png"

"""


import tkinter as tk
import sv_ttk
from screens.MainWindow import MainWindow


if __name__ == "__main__":
    app = MainWindow()
    app.anchor("n")
    app.resizable(False, False)
    app.mainloop()