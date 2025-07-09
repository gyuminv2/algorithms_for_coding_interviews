T = int(input())

def in_range(i, j):
    return 0 <= i < n and 0 <= j < n

def plus(a, si, sj):
    p_s = a[si][sj]
    for d in range(1, m):
        if in_range(si+d, sj):
            p_s += a[si+d][sj]
        if in_range(si, sj+d):
            p_s += a[si][sj+d]
        if in_range(si-d, sj):
            p_s += a[si-d][sj]
        if in_range(si, sj-d):
            p_s += a[si][sj-d]
    return p_s

def xxx(a, si, sj):
    x_s = a[si][sj]
    for d in range(1, m):
        if in_range(si+d, sj+d):
            x_s += a[si+d][sj+d]
        if in_range(si-d, sj-d):
            x_s += a[si-d][sj-d]
        if in_range(si+d, sj-d):
            x_s += a[si+d][sj-d]
        if in_range(si-d, sj+d):
            x_s += a[si-d][sj+d]
    return x_s

for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = [
        list(map(int, input().split())) for _ in range(n)
    ]
    
    # 상 하 좌 우
    dis = [-1, 1, 0, 0]
    djs = [0, 0, -1, 1]

    rtn = -1
    for i in range(n):
        for j in range(n):
            tmp_1 = plus(arr, i, j)
            tmp_2 = xxx(arr, i, j)
            rtn = max(rtn, tmp_1, tmp_2)
    
    print('#', end='')
    print(t, rtn)