from collections import deque

q = deque()

arr = [1, 3, -8, 2, 4, 3, -6, 10]
k = 2
l = []

for i in range(0, len(arr)):
    if arr[i] < 0:
        q.append(i)
    if i >= k - 1:
        if len(q) != 0 and q[0] < i - k + 1:
            q.popleft()
        if len(q) != 0:
            l.append(arr[q[0]])
        else:
            l.append(0)

print(l)