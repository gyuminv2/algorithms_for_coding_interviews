from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

q = deque()

for _ in range(n):
    cmd = input().split()
    if len(cmd) == 1:
        if cmd[0] == 'size':
            print(len(q))
        if cmd[0] == 'empty':
            if len(q) == 0:
                print(1)
            else:
                print(0)
        if cmd[0] == 'front':
            if len(q) != 0:
                print(q[0])
            else:
                print(-1)
        if cmd[0] == 'back':
            if len(q) != 0:
                print(q[-1])
            else:
                print(-1)
        if cmd[0] == 'pop_front':
            if len(q) != 0:
                print(q.popleft())
            else:
                print(-1)
        if cmd[0] == 'pop_back':
            if len(q) != 0:
                print(q.pop())
            else:
                print(-1)
    else:
        if cmd[0] == 'push_front':
            q.appendleft(int(cmd[1]))
        if cmd[0] == 'push_back':
            q.append(int(cmd[1]))