import heapq

arr = [2, 5, -1, 7, -3, -1, -2]
sum = 0
minq = []
maxq = []
k = 4

for i in range(k):
    heapq.heappush(minq, (arr[i], i))
    heapq.heappush(maxq, (-arr[i], i))
sum += minq[0][0] - maxq[0][0]

for i in range(k, len(arr)):
    heapq.heappush(minq, (arr[i], i))
    heapq.heappush(maxq, (-arr[i], i))
    while maxq[0][1] <= i - k:
        heapq.heappop(maxq)
    while minq[0][1] <= i - k:
        heapq.heappop(minq)
    sum += minq[0][0] - maxq[0][0]

print(sum)