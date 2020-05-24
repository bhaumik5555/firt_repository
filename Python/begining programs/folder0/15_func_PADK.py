def func(*args, reverse_str = False):
    return [name[::-1].title() if reverse_str == True else name.title() for name in args]


names = ['bhaumik', 'hemil']
print(func(*names))
