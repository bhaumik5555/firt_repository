from collections import namedtuple

fieldnames = ['first_name', 'last_name', 'age']

Person = namedtuple('Person_info', fieldnames)

bhaumik = Person('Bhaumik', 'Patel', 24)

print(bhaumik[1])
print(bhaumik.age)


