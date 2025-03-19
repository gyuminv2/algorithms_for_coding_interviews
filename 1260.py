# n, m, v = map(int, input().split())
# nodes = [
#     input().split()
#     for _ in range(m)
# ]

# graphs = [[] for _ in range(n+1)]

# for a, b in nodes:
#     a, b = int(a), int(b)
#     graphs[a].append(b)
#     graphs[b].append(a)

# for g in graphs:
#     g.sort()

# # dfs : 스택, 재귀
# # bfs : 큐

# visited = [False] * (n+1)

# def dfs(vs):
#     visited[vs] = True
#     print(vs, end=' ')
#     for i in graphs[vs]:
#         if not visited[i]:
#             dfs(i)

# dfs(v)

# print()

# from collections import deque

# visited = [False] * (n+1)

# def bfs(vs):
#     q = deque()
#     q.append(vs)
#     visited[vs] = True

#     while q:
#         x = q.popleft()
#         print(x, end=' ')
#         for i in graphs[x]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = True

# bfs(v)


############################################

n, m, v = map(int, input().split())
graphs = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)
for g in graphs:
    g.sort()
visited = [0] * (n+1)
def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for i in graphs[v]:
        if not visited[i]:
            dfs(i)
dfs(v)
print()
from collections import deque
visited = [0] * (n+1)
def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        nv = q.popleft()
        print(nv, end=' ')
        for i in graphs[nv]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1

bfs(v)