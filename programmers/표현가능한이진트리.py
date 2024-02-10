from collections import deque

def solution(numbers):
    answer = []
    
    for number in numbers:
        temp_answer = 1
        
        # 이진수 변환
        b_str = str(bin(number))[2:]
        
        
        # depth확인
        max_depth = 0
        while len(b_str) > 2**max_depth:
            max_depth += 1
        max_depth -= 1
        
        # 포화이진트리로 만들어줌
        # print(N, 2**xmax_depth)
        if len(b_str) != 2**max_depth:
            b_str = '0' * (2**max_depth - len(b_str)) + b_str
            
        N = len(b_str)
        
        # 중간 노드들만 확인, 1이 아니면 0반환
        dq = deque()
        dq.append((len(b_str) // 2, 1))
        while dq:
            n, depth = dq.popleft()
            
            
            
            # 0인 경우 
            if b_str[n] == '0':
                temp_answer = 0
                break
            
            # 마지막 뎁스인 경우에는 체크하지 않음
            if depth + 1 == max_depth:
                continue
                
            dq.append((n - 2**(max_depth - depth), depth + 1))
            dq.append((n + 2**(max_depth - depth), depth + 1))
            
        answer.append(temp_answer)
    
    return answer