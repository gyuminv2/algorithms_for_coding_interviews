table = dict()
# 총총 만나면 1
# 1인 애 만나면 1
# 나머지 싹 다 0

n = int(input())
for _ in range(n):
    f, s = input().split()
    if f == 'ChongChong' or s == 'ChongChong':
        table[f] = 1
        table[s] = 1
        continue

    # 둘 다 이미 있는 경우
    if f in table and s in table:
        # 한 명 이상 1인 경우
        if table[f] == 1:
            table[s] = 1
        elif table[s] == 1:
            table[f] = 1
        continue

    # 둘 중 한 명만 이미 있는 경우
    if f not in table and s in table:
        # s가 1인 경우
        if table[s] == 1:
            table[f] = 1
        else:
            table[f] = 0
    elif f in table and s not in table:
        # f가 1인 경우
        if table[f] == 1:
            table[s] = 1
        else:
            table[s] = 0
    else:
        table[f] = 0
        table[s] = 0
print(list(table.values()).count(1))