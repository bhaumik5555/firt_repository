name = ['Bhaumik', 'Hemil', 'Arth']
age = [24, 21, 16]
birthdate = ['May 6', 'Feb 28']

data = list(zip(name, age, birthdate))
print(data)
print(list(zip(*data)))