# 앞 뒤로 누적합을 구한다.
# 경우의 수 = 앞앞 맨뒤, 맨앞 뒤뒤, 양옆중앙

N = int(input())
li = list(map(int, input().split()))

nu = [0] * N
answer = 0

sum = 0
for i in range(N):
    sum += li[i]
    nu[i] = sum

# 벌이 왼왼 벌통일 경우
# 벌은 0,i에 위치, 벌통은 N-1에 위치
for i in range(1, N-1):
    bee1 = sum-li[0]-li[i]      # 0
    bee2 = sum-nu[i]            # i
    answer = max(answer, bee1+bee2)

# 벌이 벌통 우우일 경우
# 벌은 N-1, i에 위치, 벌통은 0에 위치
for i in range(1, N-1):
    bee1 = sum-li[N-1]-li[i]    # N-1
    bee2 = nu[i-1]              # i
    answer = max(answer, bee1+bee2)

#1 2 3 4
#1 3 6 10

# 벌이 좌우일 경우
# 벌 0, N-1에 위치, 벌통은 i에 위치
for i in range(1, N-1):
    bee1 = nu[i]-li[0]          # 0
    bee2 = (nu[N-2] - nu[i-1])    # N-1
    answer = max(answer, bee1+bee2)

print(answer)