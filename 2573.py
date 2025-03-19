n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


# 상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] != 0 and not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = 1

                if grid[nx][ny] == 0:
                    bye[x][y] += 1
                

ans = 0
while 1:

    cnt = 0
    visited = [[0] * m for _ in range(n)]
    bye = [[0] * m for _ in range(n)]    
    for x in range(n):
        for y in range(m):
            if grid[x][y] != 0 and visited[x][y] == 0:
                bfs(x, y)
                cnt += 1

    for x in range(n):
        for y in range(m):
            if bye[x][y] == 0:
                continue
            if grid[x][y] - bye[x][y] < 0:
                grid[x][y] = 0
            else:
                grid[x][y] -= bye[x][y]

    if cnt >= 2:
        print(ans)
        break

    if cnt == 0:
        print(0)
        break        

    ans += 1