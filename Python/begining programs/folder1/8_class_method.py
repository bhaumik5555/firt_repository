class Laptop:
    object_number = 0
    def __init__(self, brand_name, model_name, price):
        Laptop.object_number += 1
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price


    def discount(self, percentage):
        self.price = self.price * (100-percentage) / 100
        


laptop1 = Laptop("HP", "Notebook 15", 730)
laptop2 = Laptop("Lenovo", "don't know", 700)
print(Laptop.object_number)

print(laptop1.brand_name)
print(laptop1.price)
print(laptop2.price)
print(laptop2.discount(10))
print(laptop2.price)
