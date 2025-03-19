from collections import deque

n, m = map(int, input().split())
grid = [
    list(map(int, input()))
    for _ in range(n)
]

visited = [[0] * m for _ in range(n)]

# 우 하 상 좌
dxs = [0, -1, 1, 0]
dys = [1, 0, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y
            if in_range(nx, ny) and grid[nx][ny] == 1:
                if visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
            
bfs(0, 0)
print(visited[n-1][m-1])