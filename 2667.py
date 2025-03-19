from collections import deque

n = int(input())
graph = [
    list(map(int, input()))
    for _ in range(n)
]
visited = [[0] * n for _ in range(n)]

# 하 상 좌 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y):
    skrrr = 1
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y
            if in_range(nx, ny) and graph[nx][ny] == 1:
                if visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    skrrr += 1

    home.append(skrrr)
        
home = []
house = 0
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1 and visited[x][y] == 0:
            bfs(x, y)
            house += 1
home.sort()
print(house)
for h in home:
    print(h)