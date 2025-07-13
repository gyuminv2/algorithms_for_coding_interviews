# 5초에 한 명씩 태울 수 있음
# 친구가 도착하지 않으면 양보
# 절약한 시간 출력

# //초기
# Ab9AAb2bC2
# //최종
# 9AAAbbbC22
# -> 9 A b C 2 순으로 정렬되어야 함 (마지막 인덱스 기준)

from collections import defaultdict

def proc(arr):
    # dict에 추가
    d = defaultdict(list)
    for i in range(len(arr)):
        d[arr[i]].append(i)

    # dict의 마지막 인덱스 기준으로 sd에 {key, list} 형태로 정렬
    # sd 순서대로 narr에 문자열 기록
    sd = sorted(d.items(), key=lambda x : max(x[1]))
    narr = []
    for k, n in sd:
        for i in range(len(n)):
            narr.append(k)
    # reverse 이유는 계산 시 index 찾기 수월하기 때문
    narr.sort(reverse=True)

    # 기다린 시간 계산
    # (정렬 전 마지막 index - 정렬 후 마지막 index) * 5 * 개수
    rtn = 0
    for k in d:
        rtn += (d[k][-1] - (len(narr) - narr.index(k) - 1)) * 5 * len(d[k])

    return rtn


t = int(input())
for _ in range(t):
    _ = int(input())
    arr = input()

    print(proc(arr))
