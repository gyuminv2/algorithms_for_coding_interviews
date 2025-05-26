n = int(input())

# num : 영화 제목에 들어갈 수
# cnt : 666이 포함된 n번째 수
num = 666
cnt = 0
while 1:
    if '666' in str(num):
        cnt += 1

    if cnt == n:
        break

    num += 1

print(num)