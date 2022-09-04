from collections import deque
N, K = map(int, input().split())
if N > K:
    print(N-K)
    exit()
visited = [0]*100001
visited[N] = 1
dq = deque()
dq.append(N)
while deque: # bfs
    n = dq.popleft()
    if n == K:
        break
    elif n > K: # n > K, n이 K보다 크면 갈래가 -1밖에 없다.
        if visited[n-1] == 0:
            dq.append(n-1)
            visited[n-1] = visited[n] + 1
    else:
        if 0 <= n-1 <= 100000 and visited[n-1] == 0: #조건 달고 # and를 써준다.
            dq.append(n-1)
            visited[n-1] = visited[n] + 1
        if 0 <= n+1 <= 100000 and visited[n+1] == 0:
            dq.append(n+1)
            visited[n+1] = visited[n] + 1
        if 0 <= n*2 <= 100000 and visited[n*2] == 0:
            dq.append(n*2)
            visited[n*2] = visited[n] + 1
print(visited[K]-1)
    
    

