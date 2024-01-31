from collections import deque
import heapq

# 3 2 1
# 1 2 3
# 5 1 1
# 4 2 1

        
def solution(K, N, reqs):
    # 배열의 개수가 K개인 최대값이 N인 배열 만들기
    # 1~남은 N까지 반복하며 K개를 APPEND한다.
    # 이후 if 문을 통해 총 합이 N 이하인 것을 제거해준다.
    results = []
    def find_array(k, n, array):
        if k == 0 and sum(array) == N:
            results.append(array.copy())
        elif k == 1 and n > 0:
            find_array(0, 0, array+[n])
            return
        elif k <= 0 or n <= 0:
            return
        
        for i in range(1, n+1):
            find_array(k-1, n-i, array+[i])
            
    find_array(K, N, [])
    answer = float('INF')
    kReqs = [[] for _ in range(K+1)]
    for start, spend, type_ in reqs:
        kReqs[type_].append((start, spend))
    # print(kReqs)
    waitTime = [0 for _ in range(K+1)]
    
    for result in results:
        waitTime = [0 for _ in range(K+1)]
        for i in range(1, K+1):
            mentors = [0 for _ in range(result[i-1])]
            heapq.heapify(mentors)
            for start, spend in kReqs[i]:
                # print(mentors)
                # 사람을 다 돌면서
                # 가장 끝나는 시간이 짧은 사람한테 간다.
                # pop한 뒤 도착시간을 누적해준다.
                befEnd = heapq.heappop(mentors)
                heapq.heappush(mentors, max(start+spend, befEnd+spend))
                waitTime[i] += befEnd - start if befEnd > start else 0
        answer = min(sum(waitTime), answer)
        
    # print(waitTime)
    
    
    return answer