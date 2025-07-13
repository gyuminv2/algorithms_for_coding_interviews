T = int(input())

for i in range(T):
    r, e, c = map(int, input().split())

    pay = e-r-c
    if pay > 0:
        print('advertise')
    elif pay == 0:
        print('does not matter')
    else:
        print('do not advertise')