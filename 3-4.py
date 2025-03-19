n, k = map(int, input().split())
cnt = 0
while n != 1:
    n = n//k if n % k == 0 else n-1
    cnt += 1
print(cnt)