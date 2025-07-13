N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]

for k in range(M):
	i, j = map(int, input().split())
	arr2 = arr[i-1:j]
	arr2.reverse()
	arr[i-1:j] = arr2

print(*arr)