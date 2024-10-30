def frequency(s):
    dict = {}
    for c in s:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    list_frequency = []
    for key in dict:
        list_frequency.append((key, dict[key]))
    return list_frequency

s = "abcaabcca"
print(frequency(s))