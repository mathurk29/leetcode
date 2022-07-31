# classmethod

class Pizza:
    def __init__(self, type, ingredients) -> None:
        self.type = type
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        return cls("margherita", "Mozarella,jalapenos")

    @classmethod
    def otc(cls):
        return cls("otc", "Onion, Tomato, Capsicum")


pizza = Pizza("veg overloaded", "various blablabla")
margherita = Pizza.margherita()

margherita.type
margherita.ingredients
