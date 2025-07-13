n = int(input())
Q = [0, 0, 0, 0, 0]
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        Q[4] += 1
    elif x > 0 and y > 0:
        Q[0] += 1
    elif x > 0 and y < 0:
        Q[3] += 1
    elif x < 0 and y > 0:
        Q[1] += 1
    elif x < 0 and y < 0:
        Q[2] += 1
print('Q1:', Q[0])
print('Q2:', Q[1])
print('Q3:', Q[2])
print('Q4:', Q[3])
print('AXIS:', Q[4])