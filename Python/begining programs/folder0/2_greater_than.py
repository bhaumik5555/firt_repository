def grater_number(numbers):
    a = numbers[0]
    for i in numbers:
        if i > a:
            a=i
    return a 
num1 = int(input("enter the num1: "))
num2 = int(input("enter the num2: "))
num3 = int(input("enter the num3: "))
num4 = int(input("enter the num4: "))
numbers = [num1, num2, num3, num4]
print(f"the greatest number among them all is {grater_number(numbers)}.")
