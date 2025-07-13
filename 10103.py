n = int(input())

man = [100, 100]
for i in range(n):
    a, b = map(int, input().split())
    
    if a > b:
        man[0] -= a
    elif a == b:
        continue
    else:
        man[1] -= b
print(man[1])
print(man[0])