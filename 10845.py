from collections import deque

n = int(input())

queue = deque()
for _ in range(n):
    cmd = input().split()
    if len(cmd) == 1:
        if cmd[0] == 'front':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        elif cmd[0] == 'back':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])
        elif cmd[0] == 'empty':
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif cmd[0] == 'size':
            print(len(queue))
        elif cmd[0] == 'pop':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.popleft())
    else:
        if cmd[0] == 'push':
            queue.append(int(cmd[1]))