data = {
    "Bhaumik" : {"age" : 24, "fav_movies" : ["Ironman", "Avengers"]},
    "Hemil" : {"age" : 21, "fav_movies" : ["Ironman", "Captain"]},
}

print(data.get("Bhaumik").get("age"))

def func():
    """ This is trial doc string. """
    print("hello.")

print(4)
func()
print(func.__doc__)
print(sum.__doc__)
print(sorted.__doc__)
print(print.__doc__)

