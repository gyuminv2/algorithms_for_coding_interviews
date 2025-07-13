from collections import deque

n, k = map(int, input().split())

d = deque(i+1 for i in range(n))

rtn = []
while d:
    for _ in range(k-1):
        d.rotate(-1)
    rtn.append(d.popleft())

print('<', end='')
for i in range(len(rtn)):
    if rtn[i] != rtn[-1]:
        print(rtn[i], end=', ')
    else:
        print(rtn[i], end='')
print('>', end='')