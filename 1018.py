# 완전탐색
# 총 2개의 8x8 배열과 비교

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(input())

w_first = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

b_first = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]

def proc(i, j):
    cnt1 = 0
    cnt2 = 0
    si = 0
    for x in range(i, i+8):
        sj = 0
        for y in range(j, j+8):
            if grid[x][y] != w_first[si][sj]:
               cnt1 += 1
            if grid[x][y] != b_first[si][sj]:
               cnt2 += 1
            sj += 1
        si += 1
    return min(cnt1, cnt2)


rtn_cnt = 987654321
for i in range(n-7):
    for j in range(m-7):
        # 8x8 처리
        tmp_cnt = proc(i, j)
        rtn_cnt = min(rtn_cnt, tmp_cnt)

print(rtn_cnt)