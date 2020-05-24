user_data = {}
name = input("Please enter your name : ")
age = int(input("please enter your age : "))
fav_movies = input("Enter your favourite movies : ").split(',')
user_data['name'] = name
user_data['age'] = age
user_data['fav_movies'] = fav_movies
print(user_data)
