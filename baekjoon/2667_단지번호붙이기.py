import sys
sys.stdin = open('input.txt')

#델타
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = 0
count = 2
# 1. 방문한 곳을 2 ~ 로 만든다.
# 2. 숫자마다 개수를 센다.

def dfs(x, y): # 모두 반복하기 위해 상하좌우 다 생성한다.
    map_st[y][x] = count # 원하는 칸을 숫자를 바꿔준다.
    #앞뒤좌우 탐색한다.
    for dir in range(4):
        if 0 <= x + dx[dir] < N and 0 <= y + dy[dir] < N:
            if map_st[y + dy[dir]][x + dx[dir]] == 1:
                dfs(x + dx[dir], y + dy[dir])

N = int(input())
map_st = []
map_check = [[0] * N for _ in range(N)]

for _ in range(N):
    map_st.append(list(map(int, input())))
#print(map_st)
for y in range(N):
    for x in range(N):
        if map_st[y][x] == 1:
            dfs(x, y)
            count += 1
#print(map_st)
result = [0] * (count + 1)
for find in range(1, count + 1):
    for y in range(N):
        result[find] += map_st[y].count(find)
a = sorted(result)
print(count - 2)
for i in a:
    if i != 0:
        print(i, end='\n')
