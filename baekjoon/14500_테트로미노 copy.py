import sys
lambda input : sys.stdin.readline()


delta = ((0,1), (-1,0), (0,-1), (1,0)) # 오른쪽, 위, 왼쪽, 아래
        

def cjf(x, y): # ㅗ 모양만 찾는 함수
    a = []
    for dx, dy in delta: #상하좌우다 더하기
        if 0 <= y+dy < N and 0 <= x+dx < M:
            a.append(arr[y+dy][x+dx])
    if len(a) == 3: #세개면 그냥
        result.append(arr[y][x] + sum(a))
    else: #네개면 하나씩 뺀게 정답
        sum_a = sum(a)
        temp = []
        for b in a:
            temp.append(sum_a - b)
        result.append(max(temp)+arr[y][x])
    return




N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
new_arr = [[[0,0,0,0]] * M for _ in range(N)]
result = []

print(arr)

for y in range(N):
    for x in range(M):
        for idx in range(4):
            go_x = x + delta[idx][1]
            go_y = y + delta[idx][0]
            if 0 <= go_x < M and 0 <= go_y < N:
                new_arr[y][x][idx] = arr[y][x] + arr[go_y][go_x]

print(new_arr)

for y in range(N): # x y 다 계산
    for x in range(M):
        for idx in range(4): #네 방향 # 오른쪽, 아래, 왼쪽, 위
            temp = []
            go_x = x + delta[idx][1]
            go_y = y + delta[idx][0]
            if 0 <= go_x < M and 0 <= go_y < N:
                for jdx in range(4): #네방향의 위아래 # 오른쪽, 아래, 왼쪽, 위
                    if (jdx + 2) % 2 != idx:
                        temp.append(new_arr[go_y][go_x][jdx])
            if temp:
                result.append(max(temp) + new_arr[y][x][idx])



for y in range(N):
    for x in range(M):
        cjf(x, y)
    
print(max(result))

