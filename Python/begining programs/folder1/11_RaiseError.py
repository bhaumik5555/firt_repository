def add(a, b):
    if type(a) == int and type(b) == int:
        return a+b
    raise TypeError("Sorry you entered the wrong value.")


print(add(4,5))
print(add('4', '5'))
