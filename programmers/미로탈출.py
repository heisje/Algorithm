# 레버에서 출구까지
# 입구에서 레버까지
# 두개를 더한다.
from collections import deque
def solution(maps):
    answer = 0
    N = len(maps)
    M = len(maps[0])
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    startPoint = [0, 0]
    reverPoint = [0, 0]
    exitPoint = [0, 0]
    
    # find points
    for n in range(N):
        for m in range(M):
            if maps[n][m] == 'S':
                startPoint = [m, n]
            elif maps[n][m] == 'L':
                reverPoint = [m, n]
            elif maps[n][m] == 'E':
                exitPoint = [m, n]
    
    def bfs(startX, startY, endX, endY):
        visited = [[False for _ in range(M)] for _ in range(N)]
        dq = deque()
        dq.append((0, startX, startY))
        visited[startY][startX] = True
        
        while dq:
            time, x, y = dq.popleft()
            # print(x,y )
            if x == endX and y == endY:
                return time
            for gx, gy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= gx < M and 0 <= gy < N and visited[gy][gx] is False and maps[gy][gx] in ('S', 'E', 'L', 'O'):
                    visited[gy][gx] = True
                    dq.append((time + 1, gx, gy))
        return -1
    
    # 입구부터 레버까지
    entranceToRever = bfs(startPoint[0], startPoint[1], reverPoint[0], reverPoint[1])
    if entranceToRever == -1:
        return -1
    # 레버부터 출구까지
    reverToExit = bfs(reverPoint[0], reverPoint[1], exitPoint[0], exitPoint[1])
    if reverToExit == -1:
        return -1
    return entranceToRever + reverToExit