# heapq (우선 순위 큐) 알고리즘 사용

import sys
input = sys.stdin.readline
n = int(input())

import heapq
heap = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)