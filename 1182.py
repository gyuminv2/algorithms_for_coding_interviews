n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def subset(i, sum):
    global cnt

    if i >= n:
        return
    
    sum += arr[i]
    if sum == s:
        cnt += 1
    
    subset(i+1, sum)
    subset(i+1, sum - arr[i])

subset(0, 0)
print(cnt)