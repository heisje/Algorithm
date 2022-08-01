M, N= map(int, input().split()) #x = N, y = M

miro = [[0 for _ in range(N)]for _ in range(M)]

for m in range(M):
    li = list(map(int, input()))
    for n in range(N):
        miro[m][n] = li[n]


count = 0 #이동 횟수
from collections import deque
go = deque() #이동 목록
go.append((0, 0))

#append갯수 오류 잡기위해
go_len = 1 #반복횟수
 #누적

roop = True
while roop:
    trg = False # 이동 하였는가?
    for _ in range(len(go)):
        m, n = go.popleft()
        
        if miro[m][n] == 1:
            if n != 0:
                if miro[m][n-1] == 1:
                    go.append((m, n-1))
            if n != N - 1:
                if miro[m][n+1] == 1:
                    go.append((m, n+1))
            if m != 0:
                if miro[m-1][n] == 1:
                    go.append((m-1, n))
            if m != M - 1:
                if miro[m+1][n] == 1:
                    go.append((m+1, n))
            miro[m][n] = 2
        if n == N -1 and m == M -1:
            roop = False
            break
    
    count += 1

print(count)
        

