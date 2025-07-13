# Ai가 등장한 횟수 : F(Ai)
# Ai의 오등큰수 NGF(i) : 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에 가장 왼쪽에 있는 수
# 없다면 : -1

# 1 1 2 3 4 2 1
# F(1) = 3, F(2) = 2, F(3) = 1, F(4) = 1
# -1 -1 1 2 2 1 -1

n = int(input())
arr = list(map(int, input().split()))

F = [0] * 1000001
# F = [0] * 11
NGF = [-1] * n
for i in range(n):
    F[arr[i]] += 1

stack = []
for i in range(n):
    while stack and F[arr[stack[-1]]] < F[arr[i]]:
        NGF[stack.pop()] = arr[i]
    stack.append(i)

print(*NGF)