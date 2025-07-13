# 가로 세로 길이 : 10

grid = [
    [0] * 100
    for _ in range(100)
]

# 가로, 세로 순
n = int(input())
for _ in range(n):
    si, sj = map(int, input().split())
    for i in range(si, si + 10):
        for j in range(sj, sj + 10):
            grid[i][j] = 1

total = 0
for col in grid:
    total += sum(col[:])
print(total)