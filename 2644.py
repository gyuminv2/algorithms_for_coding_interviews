# # 인접 리스트, 스택

# n = int(input())
# x, y = map(int, input().split())
# m = int(input())
# graphs = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graphs[a].append(b)
#     graphs[b].append(a)
# visited = [0] * (n+1)

# x_ = -1
# def dfs(x, f):
#     global x_
#     f += 1
#     visited[x] = 1
    

#     for i in graphs[x]:
#         if not visited[i]:
#             if i == y:
#                 x_ = f
#                 return
#             dfs(i, f)

# dfs(x, 0)
# print(x_)


####################################
n = int(input())
a, b = map(int, input().split())
m = int(input())
graphs = [
    [] for _ in range(n+1)
]
for _ in range(m):
    p, c = map(int, input().split())
    graphs[p].append(c)
    graphs[c].append(p)
visited = [0] * (n+1)
ans = -1
def dfs(a, n):
    global ans
    visited[a] = 1
    n += 1
    for i in graphs[a]:
        if not visited[i]:
            if i == b:
                ans = n
                return 
            dfs(i, n)
dfs(a, 0)
print(ans)