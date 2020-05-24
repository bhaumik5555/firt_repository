def just_print(**kwargs):
    for a, b in kwargs.items():
        print(f"for the key {a} the value will be {b}")
 

just_print(name = "Bhaumik", age = 23, fav_movies = ["Avengers", "ironman"])
