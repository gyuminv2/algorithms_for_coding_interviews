m = int(input())
n = int(input())

# 제한시간 : 1초
# 1 ~ 10000 -> 100,000,000

# 0 : 소수 아님, 1 : 소수
def find_ood(target):
    if target == 1:
        return 0
    if target == 2:
        return 1
    for i in range(2, target):
        if target % i == 0:
            return 0
    return 1

arr = []
for i in range(m, n+1):
    if find_ood(i):
        arr.append(i)

if not arr:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))