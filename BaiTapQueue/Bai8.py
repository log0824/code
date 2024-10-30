from collections import deque

q = deque()
for i in range(1, 6):
    q.append(i)

n = int(input())

for _ in range(1, n):
    tmp = q.popleft()
    q.append(tmp)
    q.append(tmp)

print(q[0])
print(q)