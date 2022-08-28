# 212ms
#https://www.acmicpc.net/problem/5430
# 문제: R과 D로 된 함수목록과 배열을 주고, 배열에 함수목록을 사용하는 법
# 포인트: 리버스를 항상하지 않는다, 에러처리를 한다.
# 힘들었던 부분: []만 들어왔을 경우, ''를 정수로 변환하면서 오류를 처리했었는데,
#              이유는 모르겠지만 []를 pop(), leftpop()에서 오류처리를 하니까 해결됨

import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

TC = int(input())
for tc in range(TC):
    func = input().rstrip()
    N = int(input())

    arr = deque(input().rstrip()[1:-1].split(','))
    if N == 0:
        arr = deque()
    r_count = 0
    try:
        for active in func:
            if active == 'R':
                r_count += 1
            elif active == 'D':
                if r_count % 2 == 1:
                    arr.pop()
                else:
                    arr.popleft()
    except:
        print('error')
        continue

    if r_count % 2 == 1:
        arr.reverse()

    print('[', end='')
    print(','.join(arr), end='')
    print(']')








