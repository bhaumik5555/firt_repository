temp_c = [0, 5, 10, 15]

c_to_f = lambda temp_c: f"temp_c : {temp_c} ----> temp_f : {9*temp_c/5 + 32}"

print(list(map(c_to_f, temp_c)))
