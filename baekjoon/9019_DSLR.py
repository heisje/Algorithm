import sys
from collections import deque

TC = int(input())
for _ in range(TC):
    start, FIND = map(int, sys.stdin.readline().split())
    visited = [''] * 10000
    dq = deque()
    dq.append(start)
    visited[start] = 'A' # 아무값이나 넣어둔다.
    while dq:
        n = dq.popleft()
        if n == FIND:
            print(visited[n][1:])
        else:
            temp = n * 2 % 10000
            if not visited[temp]:
                visited[temp] = visited[n] + 'D'
                dq.append(temp)
            
            temp = 9999 if n == 0 else n - 1
            if not visited[temp]:
                visited[temp] = visited[n] + 'S'
                dq.append(temp)
            
            temp = (n % 1000) * 10 + n // 1000
            if not visited[temp]:
                visited[temp] = visited[n] + 'L'
                dq.append(temp)

            temp = n // 10 + (n % 10) * 1000
            if not visited[temp]:
                visited[temp] = visited[n] + 'R'
                dq.append(temp)

# 결론: 이 문제에선 defaultdict 느리니까 쓰지말자 ^^
# 골드4 / 1시간 pypy3 7460ms 