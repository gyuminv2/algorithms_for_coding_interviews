# import sys
# sys.setrecursionlimit(10**7)

# n, k = map(int, input().split())

# visited = [0] * 100001
# dxs = [2, -1, 1]

# from collections import deque

# def bfs(v):
#     global ans
#     q = deque([v])
#     visited[v] = 1

#     while q:
#         x = q.popleft()
#         for dx in dxs:
#             nx = x * 2 if dx == 2 else dx + x
#             if 0 <= nx < 100001:
#                 if not visited[nx]:
#                     q.append(nx)
#                     visited[nx] = visited[x] + 1
   
# bfs(n)
# print(visited[k]-1)

########################################################################

n, k = map(int, input().split())
visited = [0] * 100001
dxs = [-1, 1, 2]
from collections import deque
def bfs(v):
    visited[v] = 1
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            break
        for dx in dxs:
            if dx == 2:
                nx = v * 2
            else:
                nx = v + dx
            if 0 <= nx < 100001:
                if not visited[nx]:
                    visited[nx] = visited[v] + 1
                    q.append(nx)
bfs(n)
print(visited[k]-1)