# names = ["Bhaumik", "Hemil_Patel", "Arth"]

# print(max(names, key= lambda item:len(item)))

# data = {
#     "Bhaumik" : 24,
#     "Hemil" : 21,
#     "Arth" : 16
# }


# print(max(data, key = lambda item: data.get(item)))

data = {
    "Bhaumik" : {"age" : 24, "fav_movies" : ["Ironman", "Avengers"]},
    "Hemil" : {"age" : 21, "fav_movies" : ["Ironman", "Captain"]},
}

print(max(data, key = lambda item : data.get(item).get("age")))
