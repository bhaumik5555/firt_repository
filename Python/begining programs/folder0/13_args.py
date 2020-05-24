def power(a, *args):
    return [n ** a for n in args]


a = int(input("Enter the value of power"))
print(power(a, *range(0,11)))
