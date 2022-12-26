from time import sleep as delay
from threading import Thread

# class Obicna:
#
#     def __init__(self, name):
#       self.name = name
#
#     def pokreni(self):
#         for i in range(10):
#             print(f"[{self.name}]: {i + 1}")
#             delay(1)
#
# objekt1 = Obicna("objekt 1")
# objekt2 = Obicna("objekt 2")
#
# objekt1.pokreni()
# objekt2.pokreni()


class Dretva(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(10):
            print(f"[{self.name}]: {i + 1}\n")
            delay(1)


d1 = Dretva("Dretva1")
d2 = Dretva("Dretva2")

d1.start()
d2.start()