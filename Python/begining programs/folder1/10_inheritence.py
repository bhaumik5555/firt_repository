class Phone:
    def __init__(self, company_name, model_name, price):
        self.company_name = company_name
        self.model_name = model_name
        self.price = price

    def mobile_name(self):
        return f"{self.company_name} {self.model_name}"


class Smartphone(Phone):
    # super(Phone, company_name, model_name, price)
    # super().Phone(company_name, model_name, price)
    # super().__init__(company_name, model_name, price)
    def __init__(self,company_name, model_name, price, smartphone_type):
        super().__init__(company_name, model_name, price)
        self.smartphone_type = smartphone_type


class New_smartphone(Smartphone):
    def __init__(self, company_name, model_name, price, smartphone_type, rear_camera):
        super().__init__(company_name, model_name, price, smartphone_type)
        self.rear_camera = rear_camera


phone1 = Phone("Nokia", 1100, 50)
smartphone1 = Smartphone("Apple", "11 pro", 1300, "IPhone")
new_smartphone1 = New_smartphone("Apple", "SE2", 600, "Iphone", "5 MP")
print(phone1.mobile_name())
print(smartphone1.mobile_name())
print(new_smartphone1.mobile_name())
