def sumOfCommon(arr1, arr2):
    sum = 0
    for i in arr1:
        if i in arr2:
            sum += i
    return sum
arr1 = [6, 7, 5, 4, 6, 8]
arr2 = [2, 5, 7, 5, 3]
print(sumOfCommon(arr1, arr2))