def cube_counter(n):
    cube = { }
    for i in range(0, n+1):
        cube[i] = i**3
    return cube
n1 = int(input("Enter the value : "))
print(cube_counter(n1))
