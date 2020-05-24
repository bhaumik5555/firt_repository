class Laptop:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    # instance method
    @property
    def lap_name(self):
        return self.brand + " " + self.model_name

HP = Laptop("HP", "Notebook 15", 800)
Lenovo = Laptop("Lenovo", "xyz", 600)

print(HP.model_name)
print(Lenovo.price)
print(f"HP price is ${HP.price}.")
print(HP.lap_name)

