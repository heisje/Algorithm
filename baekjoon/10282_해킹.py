import heapq
FAIL = float("INF")
TESTCASE = int(input())

for _ in range(TESTCASE):
    N, D, C = map(int, input().split())
    nodes = [[] for _ in range(N+1)]
    for _ in range(D):
        A, B, S = map(int, input().split())
        nodes[B].append((A, S))

    hq = []
    dists = [FAIL for _ in range(N+1)]
    dists[C] = 0
    hq.append((0, C))

    cnt = set()
    maxTime = 0
    
    while hq:
        time, pre = heapq.heappop(hq)
        
        if dists[pre] < time: continue

        cnt.add(pre)
        maxTime = max(maxTime, time)

        for go, waitTime in nodes[pre]:
            if waitTime + time < dists[go]:
                dists[go] = waitTime + time
                heapq.heappush(hq, (waitTime+time, go))

    
    print(len(cnt), maxTime)
    

