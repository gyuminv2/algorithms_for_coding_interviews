from collections import deque

T = int(input())

for _ in range(T):
    q = deque()
    n, m = map(int, input().split())

    priority = list(map(int, input().split()))

    for i in range(len(priority)):
        q.append((priority[i], i))

    cnt = 0
    while 1:
        mx = max(q)[0]
        tmp = q.popleft()
        if mx == tmp[0] and m == tmp[1]:
            cnt += 1
            break
        elif mx == tmp[0]:
            cnt += 1
            continue
        else:
            q.append(tmp)

    print(cnt)