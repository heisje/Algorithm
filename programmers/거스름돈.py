
def solution(n, money):
    answer = 0
    money.reverse()
    dp = [1]+[0] * (n)
    for m in money:
        for i in range(m,n+1):
            dp[i] += dp[i - m]
    # print(dp)
    return dp[-1] % 1000000007