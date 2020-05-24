def seperate(l):
    even = []
    odd = []
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd


numbers = list(range(1,11))
print(numbers)
print(seperate(numbers))
