'''
def thrd(n, X, Y):
    if n == 1:
        for y in range(3):
            for x in range(3):
                result[1 + arr[Y+y][X+x]] += 1
        return
    for nine in [(0,0), (n,0), (2*n,0), (0,n), (n,n), (2*n,n), (0,2*n), (n,2*n), (2*n,2*n)]: # x, y
        save = arr[Y+nine[1]][X+nine[0]]
        different = False
        for y in range(n):
            y += Y + nine[1]
            for x in range(n):
                x += X + nine[0]
                if save != arr[y][x]: # 세개 x축 세개중 하나라도 다르면
                    different = True
                    break
        #print(n, x, y, different, save)
        if different == True:  # 9개 중 다른게 있으면
            thrd(n//3, nine[0], nine[1])
        else: # 다 똑같으면
            result[1+save] += 1
'''
from collections import deque
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = [0,0,0] #-1, 0, 1

if N == 1:
    result[1 + arr[0][0]] += 1
    for a in range(3):
        print(result[a])
    exit()

dq = deque()
dq.append(N//3, (0,0))
while True:
    n, dxy = dq.popleft()
    for xy in [(0,0), (n,0), (2*n,0), (0,n), (n,n), (2*n,n), (0,2*n), (n,2*n), (2*n,2*n)]: # 3 * 3의 x, y
        seti = set()
        for y in range(n):
            seti.update(arr[xy[1]+y+dxy[1]][xy[0] +dxy[0]: xy[0] + n+dxy[0]])
            if len(seti) > 1: #다른 숫자가 있으면
                dq.append(n//3, xy)
            else: #다른 숫자가 없으면
                result[1+seti.pop()] += 1
