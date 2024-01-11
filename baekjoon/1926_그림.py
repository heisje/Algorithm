from collections import deque

delta = ((1,0),(0,1),(-1,0),(0,-1))
N, M = map(int,input().split())

map_ = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
visited[0][0]
answer = 0

for x in range(M):
    for y in range(N):
        if map_[y][x] == 1:
            queue = deque()
            queue.append((x,y))
            map_[y][x] = 0
            cnt_ = 1

            while queue:
                cnt, m, n = queue.popleft()
                
                for dM, dN in delta:
                    goM, goN = dM + m, dN + n
                    if 0 <= goM < M and 0 <= goN < N and map_[goN][goM] == 1:
                        map_[goN][goM] = 0
                        cnt_ += 1
                        queue.append((goM, goN))
            answer = max(cnt_, answer)
print(map_)
print(cnt_)
print(answer)