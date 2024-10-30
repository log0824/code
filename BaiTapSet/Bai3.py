def diversity(s, k):
    s_set = set()
    tmp = 0
    for i in s:
        s_set.add(i)
    if len(s) >= k:
        tmp = 0 if len(s_set) >= k else (k - len(s_set))
        print(tmp)
    else:
        print("impossible")

s = input()
k = int(input())
diversity(s, k)