# # (휴게소 간 거리의 최댓값)을 최소로 만드는 문제
# # 휴게소 간 거리가 가장 큰 것의 중심에 휴게소를 반복적으로 짓는다.
# # 휴게소 간 거리가 가장 큰 것을 찾기 위해 heap을 이용한다.
# import sys
# import heapq
# input = sys.stdin.readline

# _, m, L = map(int, input().split())
# stations = [0] + [list(map(int, input().split()))] + [L]
# stations.sort()

# gaps = heapq.heapify([])
# for i in range(1, len(stations)):
#     gap = stations[i] - stations[i-1]
#     heapq.heappush(gaps, (gap, stations[i-1], stations[i-1]))

# while m > 0:
#     gap, start, end = heapq.heappop(gaps)

#     center = (start + end)//2
#     heapq.heappush(gaps, (center - start, start, center))
#     input = heapq.heappush(gaps, (end - center, center, end))

#     m -= 1


# 휴게소가 없는 구간의 최댓값을 이분탐색으로 찾는다.
# 휴게소가 없는 구간이기 때문에, 휴게소간 거리를 나누기를 통해, 최소 몇 개가 들어가야 하는지 검색한다.
# 경갯값이 너무 어렵다.
import sys
input = sys.stdin.readline
_, M, L = map(int, input().split())
stations = [0] + list(map(int, input().split())) + [L]
stations.sort()

answer = float("INF")
left = 1
right = L-1

while left <= right:
    center = (left + right) // 2
    #print(left, right, center)
    current = stations[0]
    count = 0
    maxGap = 0
    # 휴게소간 거리를 나누기를 통해, 최소 몇 개가 들어가야 하는지 검색한다.
    for i in range(1, len(stations)):
        # 거리가 더 크면, 최댓값을 
        num = (stations[i] - current-1) // center
        count += num

        current = stations[i]
        # 카운터를 다 썼는데, 더 큰 갭이 있는 경우 == 거리를 더 늘려야 한다.
        if count > M:
            break
    
    #print(count, M)
    # 이 거리를 가정했을 때, 휴게소의 갯수가 더 많아졌다. == 휴게소를 줄여야한다 
    # == 거리를 더 늘린다. == 불가능 하다(휴게소를 아무데나 놔두어도 이 거리가 최소가 되지 않는다.)
    if count > M:
        left = center + 1
    # 이 거리를 가정했을 때, 휴게소의 갯수가 부족하다. == 휴게소를 늘려야한다. == 거리를 줄인다. 
    # == 가능하다.(아무데나 지어도 최대 거리는 이거보다 작다.)
    elif count <= M:
        right = center - 1
        answer = min(answer, center)
    
print(answer)



