with open('abc') as f:

    read_chars = f.read(100)

    while len(read(f)) > 0:
        print(read_chars)
        read_chars = f.read(100)

