# 1428ms pypy3 / 3860ms python
import sys
import heapq

input = sys.stdin.readline
FAIL = float("INF")
N, M = map(int, input().split())
nodes = [[] for _ in range(N+1)]
for m in range(M):
    a, b = map(int, input().split())
    nodes[a].append((b, m))
    nodes[b].append((a, m))

hq = []
dists = [FAIL] * (N+1)
heapq.heappush(hq, (0, 1))
dists[1] = 0

while hq:
    time, pre = heapq.heappop(hq)
    
    if pre == N:
        break

    if time > dists[pre]: continue

    for go, goTime in nodes[pre]:
        waitTime = 0
        if time % M == goTime:
            # 안기다려도 된다.
            waitTime = 0
        elif time % M > goTime:
            # 주기 하나를 넘어 기다린다.
            waitTime = (goTime + M) - (time % M)
        elif time % M < goTime:
            # 해당 주기에서 기다린다.
            waitTime = (goTime) - (time % M)
        
        if waitTime + time < dists[go]:
            dists[go] = waitTime + time + 1
            heapq.heappush(hq, (waitTime + time + 1, go))

print(dists[N])

