n, m = map(int, input().split())

# line = []
# for _ in range(m):
#     s, b = map(int, input().split())
#     # 처음 들어가는 경우
#     if s not in line and b not in line:
#         line.append(s)
#         line.append(b)
#     else:
#         # s가 있는 경우
#         if b not in line:
#             line.append(b)
#         # b가 있는 경우
#         if s not in line:
#             # b 바로 앞에다 둠
#             idx = line.index(b)
#             line.insert(idx, s)

# for v in line:
#     if v != 0:
#         print(v, end=' ')


# 제한시간 : 2초 -> 시간초과
# 최악 시간 계산 : m * (n + n) = m*n ~= 32000 * 100000 = 3,200,000,000 = 32억 ~= 32초
############################################
############################################

# 위상 정렬 알고리즘으로 해결
# 위상 정렬 : O(V + E)
# 방향 그래프, 진입차수, 진출차수
# 각 노드가 큐에 들어온 순서 == 결과
# [동작과정]
# 1 - 진입차수가 0인 모든 노드를 큐에 삽입
# 2 - 큐 순회
## 2-1 - 큐에서 원소를 꺼내 간선 그래프 제거
## 2-2 - 새롭게 진입차수가 0이 된 노드를 큐에 삽입

from collections import defaultdict, deque
graph = defaultdict(list)
indegree = [0] * (n + 1)

for _ in range(m):
    s, b = map(int, input().split())
    graph[s].append(b)
    indegree[b] += 1

queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])
result = []

while queue:
    cur = queue.popleft()
    result.append(cur)
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

print(*result)