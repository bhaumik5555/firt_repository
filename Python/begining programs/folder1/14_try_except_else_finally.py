def div(a,b):   
    try:
        return a/b
    except ZeroDivisionError:
        print('Don\'t divide by zero.')
    except:
        print("Unknown Error.")

print(div(4,2))
print(div(4,0))


