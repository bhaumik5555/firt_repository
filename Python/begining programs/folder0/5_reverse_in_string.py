def reverse_in_string(l):
    reversed_string = []
    for i in l:
        j = i[::-1]
        reversed_string.append(j)
    return reversed_string
names = ['bapu', 'Rathin', 'Bhaumik', 'Raj']
print(reverse_in_string(names))
