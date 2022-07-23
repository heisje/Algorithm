import sys
input = sys.stdin.readline
from collections import deque

def check_0(li):
    0 in li
    return 

m, n = map(int,input().rstrip().split()) #m = x축 크기  , n = y축 크기
box = deque()
#box = [[None for _ in range(m)] for _ in range(n)]
#for y in range(n): #2중 리스트로 만들기
    #box[y] = deque(map(int, input().rstrip().split()))
box = [[int(N) for N in input().split(" ")] for _ in range(n)]
check_old = True #초기값 #하나라도 익었는지 체크
count = 0
time = 1
deq = deque()

for y in range(n): #재귀로 풀어야하나
    for x in range(m):
        if box[y][x] == 1:
            deq.append((x,y))

while deq:
    check_old = False #하나라도 익었는지 체크
    for _ in range(len(deq)):
        x, y = deq.popleft()
        if box[y][x] == 1: #현재 칸이 익었고, 한 번이상 안지나가게
            if y != 0 :               #상단
                if box[y-1][x] == 0: 
                    box[y-1][x] = 1
                    deq.append((x,y-1))
                    check_old = True
            if x != 0 :               #좌측
                if box[y][x-1] == 0 : 
                    box[y][x-1] = 1
                    deq.append((x-1,y))
                    check_old = True
            if x != m-1 :             #우측
                if box[y][x+1] == 0: 
                    box[y][x+1] = 1
                    deq.append((x+1,y))
                    check_old = True
            if y != n-1:              #하측
                if box[y+1][x] == 0: 
                    box[y+1][x] = 1
                    deq.append((x,y+1))
                    check_old = True
            box[y][x] = 2
    if check_old == True:
        count = count + 1
    time += 1
    
    '''
    for y in range(0, n):
        for x in range(0, m):
            print(str(box[y][x])+' ',end='')
        print()
    '''
if any(0 in l for l in box):
    print(-1)
else:print(count)

