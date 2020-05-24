def decorator_function(func):
    def wrapper_function(*args):
        print("This is from wrapper function.")
        return func(*args)
    return wrapper_function


@decorator_function
def function1(a):
    print(f"This is function 1 with the value {a}.")


function1(5)

@decorator_function
def addition(a, b):
    return a + b


print(f"addition of number {3} and {2} is {addition(3, 2)}")


