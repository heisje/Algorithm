import sys
import heapq
INF = sys.maxsize
# 결과값으로 최단시간 반환
def sToE(S, N, E, node):
    hq = []
    visited = [INF for _ in range(N+1)]
    for goTime, goStart in node[S]:
        heapq.heappush(hq, (goTime, goStart))

    while hq:
        time, start = heapq.heappop(hq)
        if visited[start] < time :
            continue
        if start == E:
            return time
        for goTime, goStart in node[start]:
            if time + goTime < visited[goStart]:
                visited[start] = time + goTime
                heapq.heappush(hq, (goTime+time, goStart))
    return 0
    

# N은 학생 수
# X는 마을 번호
# M은 단방향 도로 개수
N, M, X = map(int, input().split())
node = [[] for _ in range(N+1)]
for _ in range(M):
    START, END, TIME = map(int, input().split())   # Start, End, Time
    node[START].append((TIME, END))


# 집에서 x로 가는 거리 + x에서 집으로 가는 최단 거리의 합
answer = []
for n in range(N):
    if n != X:
        answer.append(sToE(n, N, X, node) + sToE(X, N, n, node))
print(max(answer))