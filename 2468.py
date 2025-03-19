from collections import deque
# 인접 행렬, bfs

n = int(input())
graphs = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y, i):
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y
            if in_range(nx, ny) and graphs[nx][ny] >= i:
                if not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = 1

ans = 0
for i in range(1, 101):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0 and graphs[x][y] >= i:
                bfs(x, y, i)
                cnt += 1
    ans = max(ans, cnt)

print(ans)