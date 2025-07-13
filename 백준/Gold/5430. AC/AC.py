from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cmd = input().strip()
    n = int(input())
    arr_input = input().strip()

    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, arr_input[1:-1].split(',')))

    is_reversed = False
    error = False

    for c in cmd:
        if c == 'R':
            is_reversed = not is_reversed
        elif c == 'D':
            if not arr:
                print('error')
                error = True
                break
            if is_reversed:
                arr.pop()
            else:
                arr.popleft()

    if not error:
        if is_reversed:
            arr.reverse()
        print('[' + ','.join(map(str, arr)) + ']')