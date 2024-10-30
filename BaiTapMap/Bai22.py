def mergeProducts(arrA, arrB):
    check = [False for _ in range(len(arrB))]
    set_A = set(arrA)
    for i in range(len(arrB)):
        if arrB[i] not in set_A:
            check[i] = True
    return check

A = ["Banana", "Banana", "Apple"]
B = ["Orange", "Apple", "Banana",
"Watermelon"] 
print(mergeProducts(A, B))