n, m = map(int, input().split())
x, y, d = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 북 동 남 서
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
dir_num = d

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

cnt = 0
while 1:
    if grid[x][y] == 0:
        grid[x][y] = -1
        cnt += 1

    for i in range(4):
        d = (d-1) % 4
        nx, ny = x + dxs[d], y + dys[d]
        if in_range(nx, ny) and grid[nx][ny] == 0:
            x, y = nx, ny
            break

    else:
        nx, ny = x + dxs[d] * -1, y + dys[d] * -1
        if in_range(nx, ny) and grid[nx][ny] == 1:
            break
        else:
            x, y = nx, ny

print(cnt)