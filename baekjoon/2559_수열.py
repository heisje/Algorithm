#import sys
#sys.stdin = open('input.txt')

#DP문제였네 . . . . . . .
#이전값을 기억해서 이전값에서 앞에꺼 뺴고 뒤에꺼 넣고
N, K = map(int, input().split())

arr = list(map(int, input().split()))

dp = [0] * (N - K + 1) #이런거 갯수 구하기 좀 헷갈림

dp[0] = sum(arr[0:0+K])
for n in range(1, N-K+1):#이런거도 ㅜㅜ
    dp[n] = dp[n-1] - arr[n-1] + arr[n+K-1]
print(max(dp))