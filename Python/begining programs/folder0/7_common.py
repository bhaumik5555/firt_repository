def common(l1, l2):
    common_items = []
    for i in l1:
        for j in l2:
            if i == j:
                common_items.append(i)
    return common_items

    
list1 = [1, 2, 5, 8, 9, 4]
list2 = [1, 5, 9, 3, 6, 3]
print(common(list1, list2))
