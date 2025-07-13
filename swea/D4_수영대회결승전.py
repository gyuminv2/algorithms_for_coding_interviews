from collections import deque

# 하 상 좌 우 + 제자리
dis = [1, -1, 0, 0, 0]
djs = [0, 0, -1, 1, 0]

def in_range(i, j):
    return 0 <= i < n and 0 <= j < n

def bfs(si, sj):
    # visited[i][j][t%3]
    visited = [[[False]*3 for _ in range(n)] for _ in range(n)]
    q = deque([(si, sj, 0)])
    visited[si][sj][0] = True

    while q:
        ci, cj, t = q.popleft()
        if (ci, cj) == (ei, ej):
            return t

        for di, dj in zip(dis, djs):
            ni, nj = ci + di, cj + dj
            nt = t + 1

            if not in_range(ni, nj): 
                continue
            if visited[ni][nj][nt % 3]:
                continue

            # 1) 제자리 대기
            if (di, dj) == (0, 0):
                visited[ni][nj][nt % 3] = True
                q.append((ni, nj, nt))
                continue

            cell = grid[ni][nj]
            # 2) 섬(1)은 무조건 불가
            if cell == 1:
                continue
            # 3) 소용돌이(2)는 출발 시점 t 기준으로만 허용
            if cell == 2 and (t % 3) != 2:
                continue

            # 4) 빈 바다(0) 또는 위 조건 통과한 소용돌이
            visited[ni][nj][nt % 3] = True
            q.append((ni, nj, nt))

    return -1

# 입력 처리
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    ans = bfs(si, sj)
    print(f"#{tc} {ans}")
