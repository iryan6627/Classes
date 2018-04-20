class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f"Pizza Stuff: ({self.ingredients})"

    @classmethod
    def margherita(cls):
        return cls(["cheese", "tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(["cheese", "tomatoes", "ham", "mushrooms"])

print(Pizza.margherita())