# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))

# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < m

# def dfs(x, y):
#     if not in_range(x, y):
#         return False
    
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x - 1, y)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         print((x, y))
#         return True
#     return False

# rtn = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             rtn += 1

# print(rtn)

from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 상 하 좌 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    q = deque([(x, y)])
    graph[x][y] = 1  # 방문 표시

    while q:
        x, y = q.popleft()
        # 상하좌우 이동
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and graph[nx][ny] == 0:
                graph[nx][ny] = 1  # 방문 표시
                q.append((nx, ny))

rtn = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(i, j)
            rtn += 1

print(rtn)