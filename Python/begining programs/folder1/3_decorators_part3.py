from functools import wraps

def print_func_data(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        print(func.__name__)
        print(func.__doc__)
        return func(*args, **kwargs)
    return wrapper_func


@print_func_data
def addition(*args):
    """This function adds the values given."""
    total = 0
    for i in args:
        total += i
    return total
    


print(addition(4, 5, 6, 8))
