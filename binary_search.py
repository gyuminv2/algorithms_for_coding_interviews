def binary_search(base, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if base[mid] == target:
            return "yes"
        elif base[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return "no"
            

n = int(input())
base = list(map(int, input().split()))

m = int(input())
target = list(map(int, input().split()))

base.sort()
for i in range(m):
    print(binary_search(base, target[i], 0, n-1), end=" ")