from collections import deque

queue = deque()

n = int(input())
l = [True for _ in range(0, n + 1)]
l[0] = False
l[1] = False
list_nt = [] 
for i in range(2, n + 1):
    for k in range(2, n):
        if i*k > n:
            break
        l[i*k] = False
    if l[i] == True:
        queue.append(i)
        while len(queue) != 0:
            tmp = queue.popleft()
            if tmp != 0:
                if l[tmp]:
                    queue.append(tmp//10)
                else:
                    l[i] = False
                    break
            else:
                list_nt.append(i)
                break
print(list_nt)