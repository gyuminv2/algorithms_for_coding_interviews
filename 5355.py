T = int(input())
for i in range(T):
    cmd = list(input().split())
    
    result = float(cmd[0])
    for j in range(len(cmd)):
        # 첫번째 숫자
        if j == 0:
            continue
        
        if cmd[j] == '@':
            result *= 3
        if cmd[j] == '%':
            result += 5
        if cmd[j] == '#':
            result -= 7
    
    print(format(result, ".2f"))