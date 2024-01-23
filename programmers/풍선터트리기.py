def solution(a):
    answer = 0
    min_idx = a.index(min(a))
    
    min_value = float('inf')
    for i in a[:min_idx]:
        if min_value > i:
            answer += 1
            min_value = i
        
    min_value = float('inf')
    for i in reversed(a[min_idx+1:]):
        if min_value > i:
            answer += 1
            min_value = i
        
    return answer + 1