arr = [1, 2, 3, 1, 2, 3, 5, 5, 4]
dict = {}

for i in arr:
    if i in dict:
        dict[i]+= 1
    else:
        dict[i] = 1

sort_dict = sorted(dict.keys())

for key in sort_dict:
    print(f"{key}: {dict[key]}")