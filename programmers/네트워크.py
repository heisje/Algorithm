from collections import deque
def solution(n, computers):
    answer = 0
    N = len(computers)
    
    # 네트워크를 모두 돌면서
    # 이미 방문했던 네트워크면 pass
    visited = set()
    for n in range(N):
        if n in visited:
            continue
        answer += 1
        dq = deque()
        visited.add(n)
        dq.append(n)
        while dq:
            p = dq.popleft()
            for go in range(N):
                if computers[go][p] == 1 and go not in visited:
                    visited.add(go)
                    dq.append(go)
        
    return answer