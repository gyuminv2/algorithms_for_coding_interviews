s = int(input())
i = 0
while 1:
    if s - i > 0:
        i += 1
        s -= i
    else:
        print(i)
        break