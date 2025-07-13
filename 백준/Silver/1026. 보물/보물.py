n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse = True)
rtn = 0
for i in range(n):
    rtn += a[i] * b[i]

print(rtn)