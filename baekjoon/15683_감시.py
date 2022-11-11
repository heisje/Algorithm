from copy import deepcopy 
from collections import deque

# 상하좌우
d_x = ( 0, 0, -1, 1)
d_y = (-1, 1,  0, 0)

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
visited = deepcopy(arr)

# cctv위치구하기
cctvs = []
cctvs_5 = []
for n in range(N):
    for m in range(M):
        if arr[n][m] == 5:
            cctvs_5.append((n, m))
        elif arr[n][m] != 0 and arr[n][m] != 6:
            cctvs.append((arr[n][m], n, m))
cctvs.sort(key=lambda x:x[0])
for cctv in cctvs_5:
    y = cctv[0]
    x = cctv[1]
    for in_x in x:
        visited[y][in_x]
        
print(arr)
print(visited)
print(cctvs)
def rotate_1():
    pass
