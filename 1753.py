# 다익스트라 알고리즘
# 자료구조 : 우선순위 큐
# 특징
# - 방향 그래프
# - 음수인 경우 사용 X
# - 특정 정점에서 가장 작은 가중치를 가진 정점 선택

import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())
INF = int(1e9)

graph = [
    []
    for _ in range(V+1)
]

# u -> v 로 가는 가중치 w
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 간선 정보 저장
distance = [INF] * (V+1)
distance[0] = -1
def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


dijkstra(k)

for d in distance:
    if d == -1:
        continue

    if d == INF:
        print('INF')
    else:
        print(d)