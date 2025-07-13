code = input()
answer = 0
# 짝수 판별
l = 0

for i in range(len(code)):
    if code[i] == '*':
        if i % 2 == 0:
            l = 1
        continue
    n = int(code[i])
    if i % 2 == 0:
        answer += n
    else:
        answer += 3 * n

if l == 1:
    for i in range(10):
        if (answer + i) % 10 == 0:
            print(i)
            break
else:
    for i in range(10):
        if (answer + 3 * i) % 10 == 0:
            print(i)
            break