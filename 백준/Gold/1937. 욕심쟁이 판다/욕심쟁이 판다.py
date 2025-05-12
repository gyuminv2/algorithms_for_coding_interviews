import sys
sys.setrecursionlimit(10**8)

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dis = [-1, 1, 0, 0]
djs = [0, 0, -1, 1]
dp = [[0] * n for _ in range(n)]

def dfs_with_dp(ci, cj):
    if dp[ci][cj] != 0:
        return dp[ci][cj]
    dp[ci][cj] = 1
    
    for dr in [0, 1, 2, 3]:
        ni, nj = ci + dis[dr], cj + djs[dr]
        if 0<=ni<n and 0<=nj<n and grid[ci][cj] < grid[ni][nj]:
            dp[ci][cj] = max(dp[ci][cj], dfs_with_dp(ni, nj)+1)

    return dp[ci][cj]
    

rtn_cnt = 0
for i in range(n):
    for j in range(n):
        rtn_cnt = max(rtn_cnt, dfs_with_dp(i, j))

print(rtn_cnt)

################################
################################

# n = int(input())
# grid = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]
# dis = [-1, 1, 0, 0]
# djs = [0, 0, -1, 1]

# from collections import deque

# def bfs(ci, cj, visited):
#     q = deque([(ci, cj)])
#     visited[ci][cj] = 1

#     mx_cnt = 0
#     while q:
#         ci, cj = q.popleft()
#         for dr in [0, 1, 2, 3]:
#             ni, nj = ci + dis[dr], cj + djs[dr]
#             if 0<=ni<n and 0<=nj<n and grid[ci][cj] < grid[ni][nj] and visited[ni][nj] == 0:
#                 q.append((ni, nj))
#                 visited[ni][nj] = visited[ci][cj] + 1
#                 mx_cnt = max(mx_cnt, visited[ni][nj])
#     return mx_cnt

# rtn_cnt = 0
# for i in range(n):
#     for j in range(n):
#         visited = [[0]*n for _ in range(n)]
#         rtn_cnt = max(rtn_cnt, bfs(i, j, visited))
#         if rtn_cnt == 4:
#             print(i, j)

# print(rtn_cnt)