# def function1(abc):
#     print(f"Hi there {abc}!")
#     def function2(xyz):
#         print(f"Hello {xyz}.")
#     return function2


# var = function1("Bhaumik")
# var("Hemil")

# def power_to(n):
#     def base(a):
#         return a**n
#     return base


# cube = power_to(3)
# square = power_to(2)

# print(cube(5))
# print(square(4))


def last_name(xyz):
    def first_name(abc):
        print(f"Your name is {abc} {xyz}.")
    return first_name


patel = last_name("Patel")
kapoor = last_name("Kapoor")

patel("Bhaumik")
patel("Hemil")
kapoor("Ranbeer")
kapoor("Karina")
