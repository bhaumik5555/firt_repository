import os,shutil

print(os.getcwd())
# print(os.mkdir('1'))
# print(os.path.exists(os.getcwd()))
# os.rmdir('1')
os.chdir(r'F:\Python')
# print(os.getcwd())
# print(os.listdir())
# print(os.chdir('folder3'))
# print(os.getcwd())
#  print(os.name)
# for item in os.listdir():
#     print(os.path.join(r'F:\programming_lactures\Machine_Learning', item))

# item = os.walk(r'F:\Python')
# for a,b,c in item:
#     print(
#     a,
#     b,
#     c
#     )

print(os.listdir())
# os.rmdir('temp_folder')
# shutil.rmtree('temp_folder')
# os.mkdir("temp_folder")
# shutil.copytree('folder3', r'F:\Python\temp_folder')
# shutil.copy(r'F:\Python\folder0\3_palindrome.py', r'F:\Python\temp_folder\palindrome2.py')
shutil.rmtree('temp_folder')
