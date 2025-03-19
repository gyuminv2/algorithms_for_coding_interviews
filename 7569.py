# 인접 행렬, BFS
from collections import deque

m, n, h = map(int, input().split())
grid = [
    [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    for _ in range(h)
]

# 상 하 좌 우 위 아래
dxs = [-1, 1, 0, 0, 0, 0]
dys = [0, 0, -1, 1, 0, 0]
dzs = [0, 0, 0, 0, -1, 1]

def in_range(x, y, z):
    return 0 <= x < n and 0 <= y < m and 0 <= z < h

def bfs():
    while q:
        z, x, y = q.popleft()

        for dx, dy, dz in zip(dxs, dys, dzs):
            nx, ny, nz = dx + x, dy + y, dz + z
            if in_range(nx, ny, nz) and grid[nz][nx][ny] == 0:
                grid[nz][nx][ny] = grid[z][x][y] + 1
                q.append([nz, nx, ny])

q = deque()
for i in range(h):
    for x in range(n):
        for y in range(m):
            if grid[i][x][y] == 1:
                q.append([i, x, y])

bfs()

day = 0
flag = 0
for i in range(h):
    for x in range(n):
        for y in range(m):
            if grid[i][x][y] == 0:
                flag = 1
            day = max(day, grid[i][x][y])
print(grid)
                

print(day-1 if flag == 0 else -1)