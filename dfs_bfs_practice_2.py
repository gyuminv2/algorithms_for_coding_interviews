from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# def bfs(x, y):
#     q = deque()
#     q.append((x, y))
#     while q:
#         x, y = q.popleft()
#         for dx, dy in zip(dxs, dys):
#             nx, ny = dx + x, dy + y
#             if not in_range(nx, ny):
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 q.append((nx, ny))
#     return graph[n-1][m-1]

def dfs(x, y):
    for dx, dy in zip(dxs, dys):
        nx, ny = dx + x, dy + y
        if not in_range(nx, ny):
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            dfs(nx, ny)
    return graph[n-1][m-1]

print(dfs(0, 0))
# print(bfs(0, 0))