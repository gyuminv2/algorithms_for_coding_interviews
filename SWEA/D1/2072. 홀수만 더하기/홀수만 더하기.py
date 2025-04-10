n = int(input())
for i in range(1, n+1):
    arr = list(map(int, input().split()))
    s = 0
    for a in arr:
        if a % 2 != 0:
            s += a
    print('#', end='')
    print(i, s)