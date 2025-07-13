def rotate(arr, si, sj):
    n = len(arr)
    n_arr = [a[:] for a in arr]
    for i in range(si, si+n):
        for j in range(sj, sj+n):
            # n_arr[si+i][sj+j] = arr[si-j+3-1][sj+i]
            n_arr[si+i][sj+j] = arr[si+j][sj-i+n-1]
    return n_arr
    

n = 3
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n_arr = [a[:] for a in arr]
n_arr = rotate(n_arr, 0, 0)
arr = n_arr
for a in arr:
    print(*a)