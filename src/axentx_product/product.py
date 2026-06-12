class Product:
    def __init__(self, name, demand_score):
        self.name = name
        self.demand_score = demand_score

    def is_validated(self):
        return self.demand_score == 100
