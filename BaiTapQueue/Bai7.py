from collections import deque

def rotOrange(matrix):
    q = deque()
    ora = 0
    n = len(matrix)
    m = len(matrix[0])
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 2:
                q.append((r, c))
            elif matrix[r][c] == 1:
                ora += 1
    tmp = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    time = 0
    while q and ora > 0:
        for _ in range(len(q)):
            t1, t2 = q.popleft()
            for i, j in tmp:
                if 0 <= t1 + i < n and 0 <= t2 + j < m and matrix[t1 + i][t2 + j] == 1:
                    q.append((t1 + i, t2 + j))
                    ora -= 1
                    matrix[t1 + i][t2 + j] = 2
        time += 1
    if ora != 0:
        return -1
    return time

matrix = [
[2, 1, 0, 2, 1],
[1, 0, 1, 2, 1],
[1, 0, 0, 2, 1]]
print(rotOrange(matrix))