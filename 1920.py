# 이미 들어있는건 검사 안해도 되므로 set 사용

n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

for b in B:
    if b in A:
        print(1)
    else:
        print(0)