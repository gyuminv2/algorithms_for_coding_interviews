n, m = map(int, input().split())
arr = list(map(int, input().split()))
min_arr = min(arr)
max_arr = max(arr)

ans = -1
for i in range(min_arr, max_arr):
    total = 0
    for a in arr:
        if (a - i) > 0:
            total += (a-i)
    if total >= m:
        ans = max(ans, i)
print(ans)