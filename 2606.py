# # 인접리스트 + dfs 풀이

# n = int(input())
# m = int(input())
# graphs = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graphs[a].append(b)
#     graphs[b].append(a)
# visited = [0] * (n+1)

# def dfs(v):
#     visited[v] = 1

#     for i in graphs[v]:
#         if not visited[i]:
#             dfs(i)

# dfs(1)
# print(sum(visited)-1)

################################################
n = int(input())
m = int(input())
graphs = [
    [] for _ in range(n+1)
]
for _ in range(m):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)
visited = [0] * (n+1)
def dfs(v):
    visited[v] = 1
    for i in graphs[v]:
        if not visited[i]:
            dfs(i)
dfs(1)
print(sum(visited)-1)