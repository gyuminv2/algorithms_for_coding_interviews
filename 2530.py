s, b, c = map(int, input().split())
c += int(input())

while c >= 60:
    c -= 60
    b += 1

while b >= 60:
    b -= 60
    s += 1

while s >= 24:
    s -= 24

print(s, b, c)