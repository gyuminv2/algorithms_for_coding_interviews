n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
t_1, t_2 = divmod(m, k+1)
sub_1 = arr[-1] * k + arr[-2]
sub_2 = arr[-2] * t_2
print(sub_1*t_1 + sub_2)