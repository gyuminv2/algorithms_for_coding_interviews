from collections import deque
n, m = map(int, input().split())
grid = [
    list(map(int, input()))
    for _ in range(n)
]
visited = [[0] * m for _ in range(n)]
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
def bfs():
    q = deque([(0, 0)])
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0<=nx<n and 0<=ny<m and grid[nx][ny] == 1 and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
bfs()
print(visited[n-1][m-1])