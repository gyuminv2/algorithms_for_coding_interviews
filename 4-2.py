cmd = input()
# 8개 | 좌 상 우 하
dxs = [-1, -2, -2, -1, 1, 2, 2, 1]
dys = [-2, -1, 1, 2, 2, 1, -1, -2]
cnt = 0
for dx, dy in zip(dxs, dys):
    nx, ny = dx + int(ord(cmd[0]) - ord('a')), dy + (int(cmd[1]) - 1)
    if 0 <= nx < 8 and 0 <= ny < 8:
        cnt += 1
print(cnt)