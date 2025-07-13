# N x N

n = int(input())
t = n // 3

grid = [
    [' '] * (n)
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            grid[i][j] = '*'
        else:
            grid[i][j] = '1'
            

def print_grid():
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end='')
        print()

print_grid()