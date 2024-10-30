def largestElement(arr):
    dict = {}
    for c in arr:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    list_sort = sorted(dict.keys(), key=lambda x: (dict[x], -x))
    return list_sort[0]
arr = [1,3,4,5,5] 
print(largestElement(arr))