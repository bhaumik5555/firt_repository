people = {
    "Bhaumik" : 24,
    "Hemil" : 21,
    "Patel_Arth" : 16
}


print(people.items)
print(list(people.items()))

print(sorted(people, key = lambda item:people.get(item)))
print(min(people, key= lambda item:people.get(item)))
print(min(people))
