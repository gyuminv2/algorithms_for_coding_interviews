T = int(input())

# 300 60 10
a = [0, 0, 0]
while T >= 300:
    T -= 300
    a[0] += 1
while T >= 60:
    T -= 60
    a[1] += 1
while T >= 10:
    T -= 10
    a[2] += 1

if T == 0:
    print(*a)
else:
    print(-1)