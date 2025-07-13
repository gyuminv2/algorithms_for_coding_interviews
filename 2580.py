# 3가지 규칙 (1 ~ 9)
# 1. 가로줄
# 2. 세로줄
# 3. 정사각형 내부

grid = [
    list(map(int, input().split()))
    for _ in range(9)
]
        
def check_range(i, j):
    if 0 <= i < 3 and 0 <= j < 3:
        return (0, 0)
    if 0 <= i < 3 and 3 <= j < 6:
        return (0, 3)
    if 0 <= i < 3 and 6 <= j < 9:
        return (0, 6)
    if 3 <= i < 6 and 0 <= j < 3:
        return (3, 0)
    if 3 <= i < 6 and 3 <= j < 6:
        return (3, 3)
    if 3 <= i < 6 and 6 <= j < 9:
        return (3, 6)
    if 6 <= i < 9 and 0 <= j < 3:
        return (6, 0)
    if 6 <= i < 9 and 3 <= j < 6:
        return (6, 3)
    if 6 <= i < 9 and 6 <= j < 9:
        return (6, 6)
    
def is_row(x, num):
    for i in range(9):
        if grid[x][i] == num:
            return False
    return True
        
def is_col(y, num):
    for i in range(9):
        if grid[i][y] == num:
            return False
    return True
    
def is_rect(where, num):
    x, y = where
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if grid[i][j] == num:
                return False
    return True

def find_empty():
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                return (x, y)
    return None

def backtrack():
    empty = find_empty()
    if not empty:
        return True

    x, y = empty
    for num in range(1, 10):
        where = check_range(x, y)
        if is_row(x, num) and is_col(y, num) and is_rect(where, num):
            grid[x][y] = num
            if backtrack():
                return True
            grid[x][y] = 0
    return False

backtrack()
for g in grid:
    print(*g)