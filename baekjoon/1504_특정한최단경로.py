# https://www.acmicpc.net/problem/1504
import heapq
FAIL = 100000000

def solution(start, target):
    dists = [FAIL] * (N+1)
    hq = []
    heapq.heapify(hq)
    heapq.heappush(hq, (0, start))
    dists[start] = 0

    while hq:
        dist, pre = heapq.heappop(hq)
        if dist > dists[pre]: continue
        
        for go, goDist in nodes[pre]:
            if goDist + dist < dists[go]:
                dists[go] = goDist + dist
                heapq.heappush(hq, (dist + goDist, go))
    
    return dists[target]

N, E = map(int, input().split())
nodes = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int, input().split())
    nodes[a].append((b, c))
    nodes[b].append((a, c))
v1, v2 = map(int, input().split())

path1 = solution(1, v1) + solution(v1, v2) + solution(v2, N)
path2 = solution(1, v2) + solution(v2, v1) + solution(v1, N)
if path1 >= FAIL and path2 >= FAIL:
    print(-1)
else:
    print(min(path1, path2))