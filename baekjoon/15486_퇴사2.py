# dp로 막풀기
# 예제
import sys
input = lambda: sys.stdin.readline().rstrip()
"""
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
2 9
1 10
"""
# N = int(input())
# schedules = [tuple(map(int, input().split())) for _ in range(N)]
# dp = [0] * (N+1)

# for day in range(N):
#     takenDay, value = schedules[day]
#     max_ = max(dp[day-1], dp[day])
#     if day+takenDay < N+1:
#         dp[day+takenDay] = max(max_ + value, dp[day+takenDay])
# print(max(dp[N-1], dp[N]))

N = int(input())
schedules = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

for day in range(0, N):
    takenDay, value = schedules[day]
    dp[day] = max(dp[day-1], dp[day])
    if day+takenDay <= N:
        dp[day+takenDay] = max(dp[day] + value, dp[day+takenDay])
print(max(dp[N-1], dp[N]))