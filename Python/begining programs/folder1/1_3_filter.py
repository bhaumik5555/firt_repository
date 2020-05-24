l1 = list(range(1,11))
print(l1)

print(list(filter(lambda x:x if x>5 else None, l1)))
print(list(filter(lambda x : x>5, l1)))

