n, m = map(int, input().split())
basket = [i for i in range(1, n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    swap_range = basket[a:b+1]
    swap_range = swap_range[::-1]

    j = 0
    for i in range(a, b+1):
        basket[i] = swap_range[j]
        j += 1
        
print(*basket)