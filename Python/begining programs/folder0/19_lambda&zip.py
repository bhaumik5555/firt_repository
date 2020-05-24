l1= list(range(1,4))
l2 = list(range(4,7))
l3 = list(range(7,10))
l4 = list(range(10, 13))
l5 = list(range(13, 16))

# print(l1, l2, l3)
# for numbers in zip(l1, l2, l3):
#     print(sum(numbers) / len(numbers))

# ave = lambda numbers:[sum(numbers)/len(numbers) for numbers in zip(a, b)]
# print(ave(l1, l2))

ave = lambda *args:[sum(numbers)/len(numbers) for numbers in zip(*args)]
print(ave(l1, l2, l3, l4, l5))