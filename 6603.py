def dfs(d, i):
    if d == 6:
        print(*answer)
        return

    for i in range(i, k):
        answer.append(arr[i])
        dfs(d + 1, i + 1)
        answer.pop()

while 1:
    k_n = list(map(int, input().split()))
    k, arr = k_n[0], k_n[1:]
    answer = []

    if k == 0:
        break
    dfs(0, 0)
    print()