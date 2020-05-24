name = "Bhaumik Patel"
char_in_string = {char: name.count(char) for char in name}
print(char_in_string)
print(char_in_string.get("B", "Not in there"))
print(char_in_string.get("b","not in there"))



months = ["Jan", "Feb", "Mar", "April", "May", "June"]

print({num+1:month for num,month in enumerate(months)})