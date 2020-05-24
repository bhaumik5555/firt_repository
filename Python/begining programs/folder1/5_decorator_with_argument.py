from functools import wraps

def only_data_type(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper_func(*args, **kwargs):
            l1 = [type(arg) == data_type for arg in args]
            if all(l1):
                return function(*args, **kwargs)
            print("Invalid argument.")
        return wrapper_func
    return decorator


@only_data_type(int)
def mul(*args):
    multiple = 1
    for arg in args:
        multiple *= arg
    return multiple


print(mul(5, 3, 2, 1, 5.6))