from collections import deque

dis = [-1, -1, -1, 0, 0, 1, 1, 1]
djs = [-1,  0,  1,-1, 1,-1, 0, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    
    # 1) 각 칸마다 인접 지뢰 개수 계산
    adj = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                cnt = 0
                for d in range(8):
                    ni, nj = i + dis[d], j + djs[d]
                    if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == '*':
                        cnt += 1
                adj[i][j] = cnt
    
    visited = [[0]*N for _ in range(N)]
    ans = 0
    
    # 2) adj[i][j] == 0 덩어리마다 한 번씩 클릭 (BFS로 덩어리 전체 열기)
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.' and adj[i][j] == 0 and not visited[i][j]:
                ans += 1
                q = deque()
                q.append((i, j))
                visited[i][j] = 1
                
                while q:
                    x, y = q.popleft()
                    # 인접 8칸 모두 열어 보고,
                    # 0인 칸은 다시 큐에 넣어 확산
                    for d in range(8):
                        nx, ny = x + dis[d], y + djs[d]
                        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == '.' and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            if adj[nx][ny] == 0:
                                q.append((nx, ny))
    
    # 3) 아직 열리지 않은(visited=False) 일반 숫자 칸들은 각각 클릭
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.' and not visited[i][j]:
                ans += 1
    
    print(f"#{tc} {ans}")
