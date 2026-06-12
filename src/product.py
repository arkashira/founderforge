class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price
