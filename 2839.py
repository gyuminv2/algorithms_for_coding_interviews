n = int(input())
# 최소 봉지 배달 개수
# 봉지 2개
# 1. 3kg
# 2. 5kg
dp = [0] * (n+1)
dp[3] = 1
for i in range(4, n+1):
    if i % 3 == 0 and i % 5 == 0:
        dp[i] = min(dp[i-3] + 1, i//5)
    elif i % 3 == 0:
        dp[i] = dp[i-3] + 1
    elif i % 5 == 0:
        dp[i] = dp[i-5] + 1
    else:
        if dp[i-3] != 0 and dp[i-5] != 0:
            dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)
        else:
            dp[i] = 0

print(-1 if dp[n] == 0 else dp[n])