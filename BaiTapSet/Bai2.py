l = [1, 1, 1, 1, 1]
s = set()
min_s = l[0]
for i in l:
    if min_s > i:
        min_s = i
    s.add(i)
s.remove(min_s)
if(len(s) == 0):
    print("NO")
else:
    print(list(s)[0])