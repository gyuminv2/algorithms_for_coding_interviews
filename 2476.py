N = int(input())

total = []
for i in range(N):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != a[1] and a[0] != a[2] and a[1] != a[2]:
        total.append(a[2] * 100)
    elif a[0] == a[1] == a[2]:
        total.append(10000 + a[0] * 1000)
    else:
        total.append(1000 + a[1] * 100)

print(max(total))