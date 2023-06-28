import sys
import heapq
INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())
node = [[] for _ in range(V+1)]
for _ in range(E):
    start, end, value = map(int, input().split())
    node[start].append((value, end))

def dijkstra():
    hq = []
    distLi = [INF for _ in range(V+1)]
    heapq.heappush(hq, (0, K))
    distLi[K] = 0
    while hq:
        d, s = heapq.heappop(hq)
        for dist, next  in node[s]:
            newDist = dist + d
            if newDist < distLi[next]:
                distLi[next] = newDist
                heapq.heappush(hq, (newDist, next))
    return distLi    
answer = dijkstra()[1:]
for a in answer:
    if a == INF:
        print('INF')
        continue
    print(a)