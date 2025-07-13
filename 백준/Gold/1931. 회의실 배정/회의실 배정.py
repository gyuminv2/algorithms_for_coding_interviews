n = int(input())
table = []
for i in range(n):
    s, e = map(int, input().split())
    table.append((s, e))

# end시간, start시간 순으로 정렬 (end 시간 기준으로 loop 순회할 것이기 때문)
table.sort(key=lambda x : (x[1], x[0]))

cnt = 1
end = table[0][1]
# arr = []
# arr.append(table[0])
for i in range(1, n):
    start = table[i][0]
    # 끝나는 시간이 시작 시간보다 크거나 같을 때 갱신
    if start >= end:
        end = table[i][1]
        cnt += 1
        # arr.append(table[i])
print(cnt)