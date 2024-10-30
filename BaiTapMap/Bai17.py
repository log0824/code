def modifyString(s):
    dict = {}
    for c in s:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    list_sort = sorted(dict.keys(), key=lambda x: (-dict[x], x))
    modified_string = ''.join(list_sort)
    return modified_string
s = "codelearn" 
print(modifyString(s))