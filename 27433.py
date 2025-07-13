n = int(input())
if n == 0:
    print(1)
    exit()
elif n == 1:
    print(1)
    exit()
rtn = 1
for i in range(2, n+1):
    rtn *= i
print(rtn)