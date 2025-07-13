import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    ch = input().rstrip()
    if ch in arr:
        continue
    arr.append(ch)
arr.sort(key = lambda x : (len(x), x))

print('\n'.join(arr))