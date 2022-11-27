

class MenuItems:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        model = {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }
        return str(model)
