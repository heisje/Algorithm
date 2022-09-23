import sys
input = lambda: sys.stdin.readline()
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
fishes = deque()
shark = None
for y in range(N):
    for x in range(N):
        if arr[y][x] == 9:
            shark = [x, y, 2]
        elif arr[y][x] != 0:
            fishes.append([x, y, arr[y][x]])

target = []
while True:
    
    # 크기재서 먹을 수 있으면, 거리를 재기 추가
    for fish in fishes:
        if shark[2] > fish[2]:
            target.append(fish)
