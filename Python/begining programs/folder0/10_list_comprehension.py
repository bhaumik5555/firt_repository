l1 = ['abc', 'pqr', 'xyz']
l2 = [''.join([l[2],l[1],l[0]]) for l in l1]
print(l1)
print(l2)
# for l in l1:
#     print(''.join([l[2], l[1], l[0]]))
 