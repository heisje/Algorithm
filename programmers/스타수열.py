from collections import Counter

def solution(a):
    answer = -1
    if len(a) == 1:
        return 0
    
    c = Counter(a)
    
    for k, v in c.items():
        # k의 값을 기준으로 스타수열을 만드는데
        # 2배가 최대의 max길이 배열인데 answer보다 작다면 진행할필요 x(시간초과 방지)
        if c[k]*2 < answer:
            continue
            
        idx = 0
        max_value = k
        length = 0
        while idx < len(a)-1:
            # idx랑 idx+1의 max_value의 값이 없으면 진행x
            # 둘의 값이 같다면 진행x
            if (a[idx] != max_value and a[idx+1] != max_value) or a[idx] == a[idx+1]:
                idx += 1
                continue
            
            # max_value를 포함하고 둘의 값이 같지 않다면
            # 조건을 만족하기 때문에 길이랑 idx랑 2씩 증가후 다음 배열 탐색
            length += 2
            idx += 2
        
        answer = max(answer, length)
        
    return answer