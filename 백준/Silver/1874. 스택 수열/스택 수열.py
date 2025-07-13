n = int(input())

cnt = 1
flag = 1
stack = []
op = []

for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        op.append('+')
        cnt += 1
    
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        flag = 0
        break

if flag:
    for o in op:
        print(o)
else:
    print('NO')