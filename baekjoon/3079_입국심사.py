"""
# 끝나는 시간을 기준으로 심사인원를 체크한다.
# 시간이 끝날 때 빈 사람이 있으면 넣어준다.

N, m = map(int, input().split())
times = [int(input()) for _ in range(N)]
times.sort()
time = 1
while m > 0:
    # 모든 타임을 돌면서..? 이럼 안되는데
    # 타임이 1000000000개다.
"""
# 그렇다면, 이분탐색으로 최대시간인 1,000,000,000의 반을 따졌을 때
# 몇 명이 가능한지 체크-> M보다 커지면 바로 반절로 줄이는 것을 반복
# 몇 명이 가능한지는 나누기 계산으로 찾는다.
# import sys
# sys.setrecursionlimit(3000)
# input = sys.stdin.readline

# def counter(time):
#     count = 0
#     for t in times:
#         count = count + time // t
#         if count >= M:
#             return 'LEFT'
#     return 'RIGHT'

# def binarySearch(left, right):
#     # print(left, right)
#     # 경곗값에 대한 확신 부족
#     if abs(right - left) == 0:
#         return 
#     elif abs(right - left) == 1:
#         if counter(right) == 'LEFT':
#             answer[0] = right
#         if counter(left) == 'LEFT':
#             answer[0] = left
#         return 

#     center = (left + right) // 2

#     count = counter(center)
#     if count == 'LEFT':
#         answer[0] = center
#         right = center - 1
#     elif count == 'RIGHT':
#         left = center + 1

#     binarySearch(left, right)

# N, M = map(int, input().split())
# times = [int(input()) for _ in range(N)]
# answer = [0]

# right = 1E20 #max(times) * M # 최대 시간
# left = 1    # 최소 시간

# binarySearch(left, right)
# print(int(answer[0]))

import sys

input = sys.stdin.readline

def solution(n, times):
	# 가능한 최솟값과 최댓값을 left와 right로 설정
    left = 1
    right = max(times) * n
    
    # 이분탐색이니 left가 right 이하인 동안
    while left <= right:
    	# 가운데 : 더하고 2로 나눈 몫(정수)
        mid = (left+right)//2
        # 심사한 사람 수
        people = 0
     	
        for time in times:
        	# 해당 심사대에서 주어진 시간동안 심사 받은 수 더하기
            people += mid//time
            
            # 중간에라도 이미 n명보다 많이 심사했다면 break
            if people >= n:
                break
        # n명 초과 심사했다면, 시간이 너무 많은 것
        # 딱 n명 심사했더라도, 시간이 남을 가능성 있음
        if people >= n:
            answer = mid
            right = mid -1
        # n명 미만 심사했다면, 시간이 너무 부족하다
        else :
            left = mid + 1
    return answer

N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]
print(solution(M, times))
