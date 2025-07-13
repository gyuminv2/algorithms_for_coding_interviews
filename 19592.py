T = int(input())

for _ in range(T):
    N, X, Y = map(int, input().split())
    V = list(map(int, input().split()))

    winner = max(V)

    # 부스터 사용 없이 내가 우승한 경우
    if V.count(winner) == 1 and V[N-1] == winner:
        print(0)
        continue
    else:
        winner = X / winner

        def booster(v, bv):
            dist = X - bv
            return (dist / v) + 1
        
        l, r = 0, Y
        time = X / V[-1]

        while 1:
            m = (l + r) // 2
            boost = booster(V[-1], m)
            if l > r:
                break
            if boost >= winner:
                l = m + 1
            else:
                r = m - 1
    if l > Y:
        print(-1)
    else:
        print(l)