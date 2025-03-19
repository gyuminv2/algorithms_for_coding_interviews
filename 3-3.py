n, m = map(int, input().split())
M = -1
for _ in range(n):
    M = max(M, min(list(map(int, input().split()))))
print(M)