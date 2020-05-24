l1 = [
    ["Bhaumik", 24],
    ["Hemil", 21],
    ["Arth", 16]
]

age = lambda item:item[1]
for a in l1:
    print(age(a))

age0 = list(map(age, l1))
age1 = list(filter(lambda item:item[1] > 20, l1))
age2 = list(map(age, l1))
print(age0)
print(age1)
print(age2)
