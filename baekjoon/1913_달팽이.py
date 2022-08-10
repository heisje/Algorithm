#핵심! =
#달팽이는 나선형을 그린다.
#나선형을 직선으로 N개만큼 그리면 그 다음은 아래로 N-1...
#[N, N-1, N-1, N-2, N-2, ... 1, 1(N-(N-1))]
#개수 2 * (N - 1) + 1
dx = [0, 1, 0, -1] #델타 탐색 (하, 우, 상, 좌)
dy = [1, 0, -1, 0]

N = int(input())
FIND_NUM = int(input())
result = 0
arr = [[0] * (N ) for _ in range(N)]

minus = 0  #N에서 빼는 숫자
x = 0 #현재위치
y = 0 
count = N**2 #넣을 숫자
for i in range(2*(N - 1)+1):   #방향 별 개수의 총 합 만큼
    for j in range(N + minus): #직진 거리 탐색
        if FIND_NUM == count:
            result = (y+1, x+1)
        arr[y][x] = count
        count -= 1
        if j < N + minus -1:
            x += dx[i % 4] #i가 4의 배수에 따라 방향이 바뀜
            y += dy[i % 4]  
        else:
            x += dx[(i+1) % 4] #i가 4의 배수에 따라 방향이 바뀜
            y += dy[(i+1) % 4]  
    minus -= (i+1) % 2 # i가 0, 2, 4, 6일때 갯수를 줄임


for i in range(N):
    print(*arr[i])
print(*result)
