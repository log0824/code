import heapq
arr = [1, 2, 3, 1, 4, 5, 2, 4, 3]
k = 3
l = []
q = []

for i in range(0, 3):
    heapq.heappush(q, (-arr[i], i))
l.append(-q[0][0])
for i in range(k, len(arr)):
    heapq.heappush(q, (-arr[i], i))
    while q[0][1] <= i - k:
        heapq.heappop(q)
    l.append(-q[0][0])
print(l)        