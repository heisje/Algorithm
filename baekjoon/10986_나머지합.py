import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))

r = [0] * m
sum = 0
for i in range(n):
    sum += li[i]
    r[sum % m] += 1

ans = r[0] # 나머지가 0이 되는 경우의 수
for i in range(m):
    # nC2 = n(n-1)/2
    ans += r[i] * (r[i]-1) // 2
print(ans)

# 1 2 2 3 1 2  2  3
# 1 3 5 8 9 11 13 16
# 1 0 2 2 0 2  1  1
# 2 + 1 + 3 + 3

# 2
# 2
# 2
# 1
# 1
# 1