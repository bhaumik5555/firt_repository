# with open(r'F:\Python\folder2\2_file1.txt', 'r+') as file1:
#     # print(file1.read())
#     # print(file1.tell())
#     # print(file1.seek(0))
#     # print(file1.readline(), end = '')
#     # print(file1.readline(), end = '')
#     # print(file1.readlines())
#     # file1.seek(0)
#     # print(file1.read())
#     # print(file1.name)
#     # print(file1.write())

with open(r'F:\Python\folder2\2_file1.txt', 'r') as file1:
    with open(r'F:\Python\folder2\2_file2.txt', 'w') as file2:
        print(file1.read())
        file1.seek(0)
        file2.write(file1.read())
