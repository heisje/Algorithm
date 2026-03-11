# 7795_먹을것인가먹힐것인가.py
q = '''
2
5 3
8 1 7 3 1
3 6 1
3 4
2 13 7
103 11 290 215
'''

import sys
'''
1 1 3 7 8
1 3 6
'''


N = int(input())
for n in range(N):
    M1, M2 = map(int, input().split())
    L1 = sorted(list(map(int, input().split())))
    L2 = sorted(list(map(int, input().split())))

    answer = 0
    for l in L1:
        left = 0
        right = len(L2) - 1
        
        point = 0
        point_tf = False

        while left <= right:
            mid = (left + right) // 2
            if L2[mid] < l:
                left = mid + 1
                point = mid
                point_tf = True
            else:
                right = mid - 1
            
        if(point_tf):
            answer += point + 1
    print(answer)