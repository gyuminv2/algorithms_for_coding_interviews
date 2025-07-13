from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    st = input()
    d = deque()
    for i in st:
        d.append(i)
    k = int(input())
    cal = list(map(int, input().split()))


    for c in cal:
        if c > 0:
            t = c
            for _ in range(t):
                d.append(d.pop(0))
        elif c < 0:
            t = c
            for _ in range(-t):
                d.insert(0, d.popleft())
        else:
            continue
    
    for c in d:
        print(c, end='')
    print()