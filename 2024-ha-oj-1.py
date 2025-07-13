from collections import deque

def find_route(x, y):
    v = [[0]*n for _ in range(n)]
    q = deque([(x, y, [])])
    v[x][y] = 1

    while q:
        x, y, route = q.popleft()

        for dr in [1, 5, 7, 3]:
            nx, ny = x + dxs[dr], y + dys[dr]
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and v[nx][ny] == 0:
                v[nx][ny] = 1
                if (nx, ny) == (park_x, park_y):
                    return route
                q.append((nx, ny, route + [(nx, ny)]))
    return -1       # 목적지 못 찾음

def rm_warrier(x, y):
    for i in range(len(warrier)-1, -1, -1):
        if [warrier[i][0], warrier[i][1]] == [x, y]:
            warrier.pop(i)

def mark_line(v, cx, cy, dr):
    while 0<=cx<n and 0<=cy<n:
        v[cx][cy] = 2                                   # for 시각적 구분
        cx, cy = cx + dxs[dr], cy + dys[dr]             # 해당 방향으로 한 칸 이동

def mark_safe(v, sx, sy, dr, ddr):
    # [1] 직선 방향 표시
    cx, cy = sx + dxs[dr], sy + dys[dr]
    mark_line(v, cx, cy, dr)                            # v에 dr방향으로 이동가능지역 표시

    # [2] 바라보는 방향으로 한줄씩 표시
    cx, cy = sx + dxs[ddr], sy + dys[ddr]
    while 0<=cx<n and 0<=cy<n:                          # 범위 내라면 계속 진행
        mark_line(v, cx, cy, dr)                        # v에 dr방향으로 이동가능지역 표시
        cx, cy = cx + dxs[ddr], cy + dys[ddr]

# tV, tStone = make_stone(wArr, mx, my, dr)
def make_stone(wArr, mx, my, dr):
    v = [[0]*n for _ in range(n)]
    stone_cnt = 0
    # [1] : dr 방향으로 만날때까지 1표시, 그 후 2표시
    nx, ny = mx + dxs[dr], my + dys[dr]
    while 0<=nx<n and 0<=ny<n:                              # 범위 내라면 계속 진행
        v[nx][ny] = 1
        if wArr[nx][ny] > 0:
            stone_cnt += wArr[nx][ny]
            nx, ny = nx + dxs[dr], ny + dys[dr]
            mark_line(v, nx, ny, dr)                        # v에 dr방향으로 이동가능지역 표시
            break
        nx, ny = nx + dxs[dr], ny + dys[dr]

    # [2] : dr-1, dr+1 방향으로 동일처리, 대각선 원점 잡고 dr 방향 처리 (50:30)
    for ddr in [((dr-1)%8), ((dr+1)%8)]:
        sx, sy = mx + dxs[ddr], my + dys[ddr]               # 첫 대각선 위치부터 체크
        while 0<=sx<n and 0<=sy<n:                          # 대각선 방향으로 초기위치 탐색 후 직선단위 처리
            if v[sx][sy] == 0 and wArr[sx][sy] > 0:         # 전사 만나면 전사가 바라보는 방향 처리
                v[sx][sy] = 1
                stone_cnt += wArr[sx][sy]                   # 돌로만든 전사 수 누적
                mark_safe(v, sx, sy, dr, ddr)               # v에 dr방향으로 이동가능지역 표시
                break

            cx, cy = sx, sy                                 # 첫 위치가 전사가 아닌 경우 직선으로 내려오며 탐색
            while 0<=cx<n and 0<=cy<n:                      # 범위 내라면 계속 진행
                if v[cx][cy] == 0:                          # 처음 방문
                    v[cx][cy] = 1
                    if wArr[cx][cy] > 0:                    # 전사로 막혔으면
                        stone_cnt += wArr[cx][cy]
                        mark_safe(v, cx, cy, dr, ddr)       # v에 dr방향으로 이동가능지역 표시
                        break
                else:
                    break
                cx, cy = cx + dxs[dr], cy + dys[dr]
            sx, sy = sx + dxs[ddr], sy + dys[ddr]
    
    return v, stone_cnt

# total_move, attk_cnt = move_warrier(v, mx, my)
def move_warrier(v, mx, my):
    move, attk = 0, 0

    # 상하좌우, 좌우상하 | 메두사 시야 = 1 피해서
    for dr in ([1, 5, 7, 3], [7, 3, 1, 5]):
        for i in range(len(warrier)-1, -1, -1):
            cx, cy = warrier[i]
            if v[cx][cy] == 1:                              # 메두사 시야면 얼음
                continue
            
            dist = abs(mx-cx) + abs(my-cy)                  # 현재 거리
            for ddr in dr:
                nx, ny = cx + dxs[ddr], cy + dys[ddr]
                # 범위 내 메두사시야 아니고 현재보다 줄어드는 방향이면 (상하좌우 우선순위로 이동)
                if 0<=nx<n and 0<=ny<n and v[nx][ny] != 1 and dist > abs(mx-nx) + abs(my-ny):
                    if (nx, ny) == (mx, my):
                        attk += 1
                        warrier.pop(i)
                    else:
                        warrier[i] = [nx, ny]
                    move += 1
                    break
    return move, attk
        
# ===============================================================
# ===============================================================

n, m = map(int, input().split())
home_x, home_y, park_x, park_y = map(int, input().split())
w_pos = list(map(int, input().split()))
warrier = []
for i in range(0, m*2, 2):
    warrier.append(w_pos[i:i+2])
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
# 0: 좌상, 1: 상, 2: 우상, 3: 우, 4: 우하, 5: 하, 6: 좌하, 7: 좌
dxs = [-1, -1, -1, 0, 1, 1, 1, 0]
dys = [-1, 0, 1, 1, 1, 0, -1, -1]

# [0] 메두사 집 -> 공원 최단 경로
route = find_route(home_x, home_y)
if route == -1:
    print(-1)
else:
    for mx, my in route:
        # 출력 (전사 이동 거리 합, 돌 수, 공격 수)
        total_move, attk_cnt = 0, 0

        # [1] 메두사의 이동 : 지정된 최단거기로 한 칸 이동 (전사 만날 시 pop)
        if [mx, my] in warrier:       # 역순으로 삭제
            rm_warrier(mx, my)

        # [2] 메두사의 시선 : 상하좌우 네 방향 가장 많이 돌로 만들 수 있는 방향 찾기
        # => v[]에 표시해서 이동시 참조(메두사 시선 == 1, 전사에 가려짐 == 2)
        # wArr[][] : 지도에 있는 전사 수 표시
        wArr = [[0]*n for _ in range(n)]
        for wx, wy in warrier:
            wArr[wx][wy] += 1

        mStone = -1
        v = []
        for dr in [1, 5, 7, 3]:         # 상하좌우 순서로 처리
            tV, tStone = make_stone(wArr, mx, my, dr)
            if mStone < tStone:
                mStone = tStone
                v = tV
        
        # [3] 전사들의 이동 (한 칸씩 두번) : 메두사 있는 경우 공격 후 pop
        total_move, attk_cnt = move_warrier(v, mx, my)

        print(total_move, mStone, attk_cnt)
    print(0)