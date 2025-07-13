n = int(input())
for _ in range(n):
    arr = list(input().rstrip())
    print(arr)

    stack = []
    for ch in arr:
        if len(stack) == 0:
            stack.append(ch)
        else:
            if stack[-1] == '(' and ch == ')':
                stack.pop()
            else:
                stack.append(ch)
    
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')