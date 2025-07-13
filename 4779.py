def cut(i, tn):
    if tn == 1:
        return
    for i in range(i + tn//3, i + (tn//3) * 2):
        result[i] = ''

while 1:
    try :
        n = int(input())
        result = ['-']*(3**n)
        # cut(0,3**n) # 자르기
        print(''.join(result))
    except :
        break