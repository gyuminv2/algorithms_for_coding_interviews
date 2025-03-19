n, m = map(int, input().split())
x, y, d = map(int, input().split())
maps = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[0] * m for _ in range(n)]
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
dir_num = d
def in_range(x, y):
   return 0 <= x < n and 0 <= y < m
cnt = 1
visited[x][y] = 1
while 1:
    test = 0
    for i in range(4):
        dir_num = (dir_num + 3) % 4
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        if in_range(nx, ny) and maps[nx][ny] == 0 and not visited[nx][ny]:
            x, y = nx, ny
            visited[x][y] = 1
            cnt += 1
            test = 0
        else:
            test += 1
    if test == 4:
        nx, ny = x + dxs[dir_num]*-1, y + dys[dir_num]*-1
        if in_range(nx, ny) and maps[nx][ny] == 0 and not visited[nx][ny]:
            x, y = nx, ny
            visited[x][y] = 1
            cnt += 1
        else:
            break
print(cnt)