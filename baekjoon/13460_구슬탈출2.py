import sys
input = lambda:sys.stdin.readline()
from collections import deque

d = (
    (0, 0, 1),
    (1, 1, 0),
    (2, 0, -1),
    (3, -1, 0),
)


N, M = map(int, input().split())
arr = list(list(input().rstrip()) for _ in range(N))
#print(arr)

blu = [0, 0]
red = [0, 0]
hol = [0, 0]

for y in range(N):
    for x in range(M):
        if 'B' == arr[y][x]:
            blu[0], blu[1] = x, y
            arr[y][x] = '.'
        if 'R' == arr[y][x]:
            red[0], red[1] = x, y
            arr[y][x] = '.'
        if 'O' == arr[y][x]:
            hol[0], hol[1] = x, y

#print(arr)
#print(blu,red,hol)
dq = deque()
count = 0
dq.append((blu[:], red[:], count, 10))

g_blu = [0, 0]
g_red = [0, 0]
end_blu = end_red = False
while dq:
    # 블루랑 레드랑 개수를 꺼내온다
    blu, red, count, b_didx = dq.popleft()
    
    arr[blu[1]][blu[0]] = 'B'  # 그려놓기
    arr[red[1]][red[0]] = 'R'
    before_blu = blu[:]  # 이전꺼 저장해두기, 마지막에 바꾸려고
    before_red = red[:]
    print('bf:',blu, red, count)
    # 4방향으로 움직인다 

    for didx, dx, dy in d:
        #if (didx + 2) % 4 != b_didx:
            # 블루랑 레드를 한 방향으로 계속 움직여준다, 벽이나 공을 만날 때 까지
            roop_blu = roop_red = True # 둘 다 행동을 그만두면 멈춰!!
            front_blu = front_red = False # 내 앞에 공있다
            while roop_blu or roop_red:
                g_blu[0], g_blu[1] = blu[0] + dx, blu[1] + dy  # 갈 방향
                g_red[0], g_red[1] = red[0] + dx, red[1] + dy  # 갈 방향

                # 블루 멈춰
                if roop_blu:  # 블루가 진행되고 있고,
                    if arr[g_blu[1]][g_blu[0]] == '.':  # 블루가 진행되고 있고, .아닌걸 만났을 때
                        blu[0], blu[1] = g_blu[0], g_blu[1]  # 진행
                    else:
                        roop_blu = False
                        if arr[g_blu[1]][g_blu[0]] == 'R':  # 내앞에 공있다
                            front_blu = True
                        elif arr[g_blu[1]][g_blu[0]] == 'O':  # 내앞에 구멍있다
                            end_blu = True
                            #exit()
                        
                # 레드 멈춰
                if roop_red:  # 레드가 진행되고 있고,
                    if arr[g_red[1]][g_red[0]] == '.':  # .아닌걸 만났을 때
                        red[0], red[1] = g_red[0], g_red[1]  # 진행
                    else:
                        roop_red = False
                        if arr[g_red[1]][g_red[0]] == 'B':  # 내앞에 공있다
                            front_red = True
                        elif arr[g_red[1]][g_red[0]]== 'O':  # 내앞에 구멍있다
                            end_red = True
                            #exit()
            
            if end_blu:  # 파란공이 들어갔을 때
                print(-1)
                exit()
            elif end_red and front_blu:  # 빨강공이 들어갔지만, 파랑공도 같이 들어갔을 때
                print(-1)
                exit()
            elif end_red:  #빨강공만 들어갔을 때
                print(count + 1)
                exit()

            # 한 방향으로 가는데, 다른 색 공이 나오면 일단 멈췄다가, 그 공의 하나 뒤에 놓는다.
            if front_blu:
                blu[0], blu[1] = red[0] - dx, red[1] - dy
            if front_red:
                red[0], red[1] = blu[0] - dx, blu[1] - dy

            arr[before_blu[1]][before_blu[0]] = '.'  # 다시 .으로 바꿔놓고, 돌릴때 다시해줌.
            arr[before_red[1]][before_red[0]] = '.'
            
            # 진행이 다 됐으므로, 방향별로 dq에 넣는다.
            #print('go:',blu, red, count)
            dq.append((blu[:], red[:], count+1, didx))
print(-1)

                
        





