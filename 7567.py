a = input()

total = 0
for c in range(len(a)):
    if c == 0:
        total += 10
        continue
    if a[c] == a[c-1]:
        total += 5
    else:
        total += 10
print(total)