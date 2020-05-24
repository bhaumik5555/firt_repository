def map2(func_name, l):
    l1 = []
    for i in l:
        l1.append(func_name(i))
    return l1

names = ["Bhaumik", "Hmil", "Arth"]

print(map2(len, names))


lenght = [len(i) for i in names]

print(lenght)

lnght = lambda l:len(l)

def map3(func, l2):
    return [func(j) for j in l2]
    


print(map3(lnght, names))
