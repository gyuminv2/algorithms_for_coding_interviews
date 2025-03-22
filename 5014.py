# from collections import deque

# F, S, G, U, D = map(int, input().split())

# # 목표 G, 버튼 누르는 최소 횟수, 없다면 "use the stairs"

# visited = [0] * (F+1)

# def bfs(v):
#     q = deque([v])
#     visited[v] = 1

#     while q:
#         x = q.popleft()

#         if x == G:
#             break
#         else:
#             for dx in (U, -D):
#                 nx = dx + x
#                 if 0 < nx <= F:
#                     if not visited[nx]:
#                         visited[nx] = visited[x] + 1
#                         q.append(nx)

# bfs(S)
# print(visited[G]-1 if visited[G] != 0 else "use the stairs")

########################################################################

F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)
from collections import deque
def bfs(v):
    cnt = 0
    visited[v] = 1
    q = deque([v])
    while q:
        v = q.popleft()
        if v == G:
            break

        for dx in (U, -D):
            nx = v + dx
            if 0 < nx <= F:
                if not visited[nx]:
                    cnt += 1
                    q.append(nx)
                    visited[nx] = visited[v] + 1
bfs(S)
print("use the stairs" if visited[G]-1 == -1 else visited[G]-1)