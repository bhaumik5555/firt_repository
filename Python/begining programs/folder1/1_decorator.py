def decorator_function(func):
    print("Hi.")
    def wrapper_function():
        print("Hello there!")
        func()
    return wrapper_function

@decorator_function
def func1():
    print("Hi Bhaumik.")

# func2 = decorator_function(func1)

# func2()

func1()

