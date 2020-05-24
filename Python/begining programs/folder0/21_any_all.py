numbers = list(range(0, 11))

print(numbers)

print(all([a%2 == 0 for a in numbers]))
print(any([a%2 == 0 for a in numbers]))
if all([a%2 == 0 for a in numbers]):
    print("All the numbers are even")
else:
    print("sorry.")    
