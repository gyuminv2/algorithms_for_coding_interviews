T = int(input())
a = [0, 0]
for t in range(T):
    for i in range(9):
        y, k = map(int, input().split())
        a[0] += y
        a[1] += k

    if a[0] == a[1]:
        print('Draw')
    elif a[0] > a[1]:
        print('Yonsei')
    else:
        print('Korea')