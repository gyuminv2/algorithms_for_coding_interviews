n = int(input())

if n == 1:
    print(1)
    exit()

dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1
dp[2] = 2
# n = 1 : 1
# n = 2 : 11, 00
# n = 3 : {111, 001} : n=2 에다가 '1' 추가, {100} : n=1 에다가 '00' 추가
for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[n])