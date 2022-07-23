import sys
input = sys.stdin.readline

def check_0(li):
    0 in li
    return 

m, n = map(int,input().rstrip().split()) #m = x축 크기  , n = y축 크기
#box = [[0]*m for i in range(0, n)]
box = list()
for y in range(n): #2중 리스트로 만들기
    box.append(list(map(int,input().rstrip().split()))) 

check_old = True #초기값 #하나라도 익었는지 체크
count = 0
time = 1
while check_old == True:
    check_old = False #하나라도 익었는지 체크
    for y in range(n): #재귀로 풀어야하나
        for x in range(m):
            if box[y][x] == time: #현재 칸이 익었고, 한 번이상 안지나가게
                if y != 0 :               #상단
                    if box[y-1][x] == 0: 
                        box[y-1][x] = time + 1
                        check_old = True
                if x != 0 :               #좌측
                    if box[y][x-1] == 0 : 
                        box[y][x-1] = time + 1
                        check_old = True
                if x != m-1 :             #우측
                    if box[y][x+1] == 0: 
                        box[y][x+1] = time + 1
                        check_old = True
                if y != n-1:              #하측
                    if box[y+1][x] == 0: 
                        box[y+1][x] = time + 1
                        check_old = True
                
                box[y][x] = 3
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

