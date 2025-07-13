T = int(input())
for t in range(T):
    N = int(input())
    a = dict()
    for i in range(N):
        s, c = input().split()
        a[int(c)] = s
    print(a[max(a)])