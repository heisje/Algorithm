# sort이후
# 하나씩 돌면서
# 끝날 때 까지 겹치는 것을 전부 제외 시키고
# 범위를 작은 것을 기준으로 하여
# 계속 돈다.
def solution(targets):
    answer = 1
    targets.sort()
    idx = 1
    start = targets[0][0]
    end = targets[0][1]
    while idx < len(targets):
        tStart = targets[idx][0]
        tEnd = targets[idx][1]
        # 겹친다면,
        if tStart < end :
            # 더 짧을 경우
            start = max(tStart, start)
            end = min(tEnd, end)
        # 안겹치면,
        elif end <= tStart:
            start = tStart
            end = tEnd
            answer += 1
        idx += 1
        
    return answer