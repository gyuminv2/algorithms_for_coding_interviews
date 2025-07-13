N = int(input())

a = [0, 0]
for i in range(N):
    n = int(input())
    if n == 0:
        a[0] += 1
    else:
        a[1] += 1
print('Junhee is not cute!' if a[0] > a[1] else 'Junhee is cute!')