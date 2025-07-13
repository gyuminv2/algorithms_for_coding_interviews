n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
l.sort()

rtn = []
for lp in l:
    rtn.append(lp*n)
    n -= 1
print(max(rtn))