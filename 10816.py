n = int(input())
san = list(map(int, input().split()))
m = int(input())
test = list(map(int, input().split()))

d = dict()
for i in range(n):
    if san[i] in d:
        d[san[i]] += 1
    else:
        d[san[i]] = 1

for i in range(m):
    if test[i] in d:
        print(d[test[i]], end=' ')
    else:
        print(0, end=' ')