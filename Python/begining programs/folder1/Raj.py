list1 = list(input("Enter the comma seperated values : ").split(','))
list2 = list(input("Enter the comma seperated values : ").split(','))
list1_int = []  # converting string in intiger value
list2_int = []  # converting string in intiger value

# for n in range(0,len(list1)):
#     a = int(list1[n])
#     list1_int.append(a)

list1_int = [int(list1[n]) for n in range(0,len(list1))]
list2_int = [int(list2[n]) for n in range(0,len(list2))]

# for n in range(0,len(list2)):
#     a = int(list2[n])
#     list2_int.append(a)

list1_int.extend(list2_int)   # mixing of both list
list3 = list(set(list1_int))
list3.sort()
print(list3)
difference = list3[1] - list3[0]

for n in range(1,len(list3)):
    if list3[n] - list3[n-1] == difference:
        if n == len(list3)-1:
            print("True")
    else:
        print("False")
        break

