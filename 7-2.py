n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
for o in m_arr:
    if o in n_arr:
        print('yes', end=' ')
    else:
        print('no', end=' ')