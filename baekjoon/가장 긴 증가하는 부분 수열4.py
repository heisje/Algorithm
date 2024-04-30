# dp배열에 증가하는 순서대로 누적시킨다. ex [0,10,20,30,40,50]
# 더 낮은 것이 온다면, 증가하는 index를 근사 낮은값의 뒤로 저장한다.
# ex [0, 10, 20, 25, 40, 50]
# 반복한다.

# 역추적이 필요했다.
# rank란 것을 만들어 등수를 저장해준뒤, 역추적해주자.

N = int(input())
li = list(map(int, input().split()))
dp = []
dp.append(li[0])
rank = [0]*N

def find(num, left, right):
    center = (left+right) // 2
    if left == right:
        if dp[right] >= num:
            return right
        if dp[right] < num:
            return right + 1

    if right - left == 1:
        if dp[left] == num:
            return left
        if dp[right] == num:
            return right
        if dp[left] < num < dp[right]:
            return right

    if num < dp[center]:
        right = center
    if num == dp[center]:
        return center
    if num > dp[center]:
        left = center
    return find(num, left, right)

#LFS
for idx, num in enumerate(li):
    if dp[-1] < num:
        dp.append(num)
        rank[idx] = len(dp) - 1
        continue

    if num <= dp[-1]:
        findIdx = find(num, 0, len(dp)-1)
        rank[idx] = findIdx
        dp[findIdx] = num

print(len(dp))
# 역추적
order = max(rank)
arr = []
for i in range(N-1, -1, -1):
    if rank[i]==order:
        arr.append(li[i])
        order-=1
        
arr.reverse()
print(' '.join(map(str,arr)))

# for i in arr:
#     print(i, end=' ')
#
# import sys

# N = int(sys.stdin.readline())
# num = list(map(int, sys.stdin.readline().split()))

# dp = [1]*N

# for i in range(1, N):
#     for j in range(i):
#         if num[i]>num[j]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(dp)
# print(max(dp))
# order = max(dp)
# arr = []
# for i in range(N-1, -1, -1):
#     if dp[i]==order:
#         arr.append(num[i])
#         order-=1
        
# arr.reverse()
# for i in arr:
#     print(i, end=' ')
