# from collections import deque
# # 인접 행렬, bfs

# n = int(input())
# graphs = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]

# # 상하좌우
# dxs = [-1, 1, 0, 0]
# dys = [0, 0, -1, 1]

# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < n

# def bfs(x, y, i):
#     q = deque([(x, y)])
#     visited[x][y] = 1

#     while q:
#         x, y = q.popleft()
#         for dx, dy in zip(dxs, dys):
#             nx, ny = dx + x, dy + y
#             if in_range(nx, ny) and graphs[nx][ny] >= i:
#                 if not visited[nx][ny]:
#                     q.append([nx, ny])
#                     visited[nx][ny] = 1

# ans = 0
# for i in range(1, 101):
#     visited = [[0] * n for _ in range(n)]
#     cnt = 0
#     for x in range(n):
#         for y in range(n):
#             if visited[x][y] == 0 and graphs[x][y] >= i:
#                 bfs(x, y, i)
#                 cnt += 1
#     ans = max(ans, cnt)

# print(ans)


################################################################
from collections import deque
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
max_under = 0
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
def bfs(x, y, k):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[x][y] >= k:
                if not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
for i in range(1, 100):
    under = 0
    visited = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if grid[x][y] >= i and not visited[x][y]:
                bfs(x, y, i)
                under += 1
    max_under = max(max_under, under)
print(max_under)