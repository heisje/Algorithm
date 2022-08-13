#https://www.acmicpc.net/problem/1244

#문제:   1.스위치를 주고
#        2. 
N = int(input())
switch = list(map(int, input().split()))
HU_NUM = int(input())

change = lambda a:abs(a-1)
for _ in range(HU_NUM):
    gender, idx = map(int, input().split())
    if gender == 1:
        for i in range(len(switch)):
            if i % 3 == 2:
                change(switch[i])
    if gender == 2:
        pass
    
