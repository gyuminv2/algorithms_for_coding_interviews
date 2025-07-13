import sys
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [[-1]*m for _ in range(n)]
dp[n - 1][m - 1] = 1
dis = [-1, 1, 0, 0]
djs = [0, 0, -1, 1]

def dfs(ci, cj):
    if dp[ci][cj] != -1:
        return dp[ci][cj]

    cnt = 0
    for dr in [0, 1, 2, 3]:
        ni, nj = ci + dis[dr], cj + djs[dr]

        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] < grid[ci][cj]:
            cnt += dfs(ni, nj)

    dp[ci][cj] = cnt
    return dp[ci][cj]

print(dfs(0, 0))