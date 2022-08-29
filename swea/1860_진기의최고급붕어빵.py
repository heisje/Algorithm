import sys
from collections import deque
sys.stdin = open('input.txt')


TC = int(input())
for tc in range(1, TC + 1):
    N, M, K = map(int, input().split())
    hi = list(map(int, input().split()))
    hi.sort(reverse=True)

    dp = [0]
    t = 1
    while t <= 11111: #dp[t] >= 0:
        #누적하기
        if t % M == 0:
            dp.append(dp[t-1]+K)
        else:
            dp.append(dp[t-1])

        #계산하기
        count = 0
        while hi and hi[-1] == t: #뺼 값이 T와 같으면 계속 빼면서 count 누적 , 인덱싱 오류방지
            hi.pop()
            count += 1
        dp[t] -= count

        #종료조건
        if dp[t] < 0:
            print(f'#{tc} Impossible')
            break
        elif hi == []: #들어있지 않으면
            print(f'#{tc} Possible')
            break
        t += 1 #시간 늘리기
    else:
        print(f'#{tc} Impossible')