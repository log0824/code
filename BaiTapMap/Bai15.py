arr = [4, 7, 2, 8, 4, 8, 3, 2]
dict = {}
max_f = 0

for i in arr:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
    if dict[i] > max_f:
        max_f = dict[i]

for key in dict:
    if dict[key] == max_f:
        print(f"{key} : {dict[key]}")