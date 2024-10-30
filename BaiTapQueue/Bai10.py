import heapq
import math
def visited(arr, k):
    pq = []
    for i in range(len(arr)):
        tmp = arr[i][0]*arr[i][0] + arr[i][1]*arr[i][1]
        if len(pq) < k:
            heapq.heappush(pq, (-tmp, arr[i]))
        elif -pq[0][0] > tmp:
            heapq.heappop(pq)
            heapq.heappush(pq, (-tmp, arr[i]))
    return [item[1] for item in pq]

l = [(1, 0), (2, 1), (3, 6), (-5, 2), (1, -4)]
k = 3
print(visited(l, k))