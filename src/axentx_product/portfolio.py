from .product import Product

class Portfolio:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if not any(p.name == product.name for p in self.products):
            self.products.append(product)

    def get_validated_products(self):
        return [p for p in self.products if p.is_validated()]
