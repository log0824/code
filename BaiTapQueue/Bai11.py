import heapq

def find_max_product(arr):
    result = []
    top3 = [] 
    for i in range(len(arr)):
        heapq.heappush(top3, arr[i])
        if len(top3) > 3:
            heapq.heappop(top3)        
        if len(top3) < 3:
            result.append(-1)
        else:
            result.append(top3[0] * top3[1] * top3[2])
    
    return result

l = [1, 2, 3, 4, 5, 5, 5, 6]
print(find_max_product(l))
