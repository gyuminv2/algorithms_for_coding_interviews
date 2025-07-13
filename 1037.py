n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(arr[0]**2)
else:
    print(max(arr) * min(arr))