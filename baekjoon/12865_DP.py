n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()
dp = [0] * (k+1)
for w, v in arr:
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)
print(dp[k])