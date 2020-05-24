from functools import wraps

def only_numbers(function):
    @wraps(function)
    def wrapping_function(*args, **kwargs):
        l1 = [type(i) == int or type(i) == float for i in args]
        if all(l1):
            return function(*args, **kwargs)
        else:
            print("Only numbers allowed.")
    return wrapping_function


@only_numbers
def add(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add(3,5,7,4,8, 4, 6.454))
