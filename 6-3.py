n = int(input())
arr = [
    input().split()
    for _ in range(n)
]
arr.sort(key=lambda x : int(x[1]))
for a in arr:
    print(a[0], end=' ')