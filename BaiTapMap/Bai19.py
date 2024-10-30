def checkSum(arr, sum):
    for i in arr:
        if (sum - i) in arr:
            return True
    return False

arr = [2,5,3,8,9]
sum = 3
print(checkSum(arr, sum))