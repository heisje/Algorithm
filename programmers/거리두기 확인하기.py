# https://school.programmers.co.kr/learn/courses/30/lessons/81302
from collections import deque

d_x = (0, 0, -1, 1)
d_y = (-1, 1, 0, 0)

def solution(places):
    answer = []
    # p위치 찾기
    
    for place in places:
        # p의 위치를 찾자
        p_points = []
        print(place)
        for y in range(5):
            for x in range(5):
                if place[y][x] == 'P':
                    p_points.append((x, y))
        
        flag = False # 틀린걸 찾았는지 확인
        visited = [[0 for _ in range(5)] for _ in range(5)]
        # p마다 bfs를 돌려보자
        for p_x, p_y in p_points:
            dq = deque()
            dq.append((p_x, p_y, 1))
            visited[p_y][p_x] = 1
            while dq:
                print(visited, dq)
                x, y, value = dq.popleft()
                for d_x, d_y in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                    go_x = x + d_x
                    go_y = y + d_y
                    # 바깥, 벽 예외처리
                    if 0 <= go_x < 5 and 0 <= go_y < 5 and place[go_y][go_x] != 'X':
                        # 빈공간일 때
                        if place[go_y][go_x] == "O" and visited[go_y][go_x] == 0:
                            if value <= 1:
                                dq.append((go_x, go_y, value + 1))
                                visited[go_y][go_x] = value + 1
                        # 사람일 때
                        if place[go_y][go_x] == "P" and visited[go_y][go_x] == 0:
                            print('찾았다!', go_x, go_y )
                            flag = True
                            break
                if flag:
                    break
            if flag:
                break
        # 찾으면 0, 없으면 1
        if flag:
            answer.append(0)
        else:
            answer.append(1)
    return answer


a = [
    ["POOOP", 
     "OXXOX", 
     "OPXPX", 
     "OOXOX", 
     "POXXP"], 

    ["POOPX", 
     "OXPXP", 
     "PXXXO", 
     "OXXXO", 
     "OOOPP"], 

    ["PXOPX", 
     "OXOXP", 
     "OXPOX", 
     "OXXOP", 
     "PXPOX"], 

    ["OOOXX", 
     "XOOOX", 
     "OOOXX", 
     "OXOOX", 
     "OOOOO"], 

    ["PXPXP", 
     "XPXPX", 
     "PXPXP", 
     "XPXPX", 
     "PXPXP"]
]
print(solution(a))
