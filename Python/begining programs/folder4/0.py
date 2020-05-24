class Person:

    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    # @classmethod
    # def abc(cls,data):
    #     firstname, lastname, age = data.split(",")

    @classmethod
    def csv(cls,info):
        first, last, age = info.split(",")
        cls.first = first
        cls.last = last
        cls.age = age

    @property
    def age_after_10(self):
        return (self.age + 10)

    @age_after_10.setter
    def age_after_10(self, any_value):
         self.age = max(80,any_value)


        

person1 = Person('Bhaumik', "Patel", 24)

Person.csv("Hemil,Patel,21")

print(f'{Person.first} {Person.last} is {Person.age} years old.')

print(person1.age_after_10 = 50)
print(person1.age_after_10)


