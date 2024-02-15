from collections import deque
INF = float('INF')

def solution(x, y, n):
    answer = 0
    dp = [INF for _ in range((y+1)*3)]
    dp[x] = 0
    for i in range(x, y):
        if dp[i] == INF:
            continue
        dp[i*2] = min(dp[i*2], dp[i] + 1)
        dp[i*3] = min(dp[i*3], dp[i] + 1)
        dp[i+n] = min(dp[i+n], dp[i] + 1)
        
    if dp[y] == INF:
        return -1
    return dp[y]