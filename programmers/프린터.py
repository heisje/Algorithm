from collections import deque

def solution(priorities, location):
    ans = 0
    target = (location, priorities[location])
    q = deque()
    q.extend([(idx, i) for idx, i in enumerate(priorities)])
    
    while q:
        max_v = max(q, key=lambda x:x[1])
        idx, i = q.popleft()
        if (idx, i) == max_v:
            ans += 1
            if (idx, i) == target:
                return ans
        else:
            q.append((idx, i))