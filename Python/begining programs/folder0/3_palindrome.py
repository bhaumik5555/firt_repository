def palindrome(name):
    new_name = ""
    for i in range(0,len(name)):
        new_name += name[len(name)-i-1]
    if new_name == name:
        return True
    else:
        return False


in_name = input("Please enter your name : ")
print(palindrome(in_name))
