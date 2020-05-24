while True:
    try:
        age = int(input("Enter your age please : "))
        break
    except ValueError:
        print("Please enter the number. ")
    except:
        print("Unknown Error.")

if age < 18 : 
    print("Underaged.")
else:
    print("You are eligible. ")

