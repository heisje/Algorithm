#https://school.programmers.co.kr/learn/courses/30/lessons/42895
# 555-55를 구현할 수 있어야되나..?
from collections import deque
def solution(N, number):
    answer = 0

    dq = deque()
    # 현재값, 들어올 값, 트리거, 횟수
    dq.append((0,N,"",0))

    answer = 0
    while dq:
        a, b, trg, num = dq.popleft()
        answer = num
        if num > 8:
            return -1 

        temp = a+b
        if temp != number:
            dq.append((temp,N,trg,num+1))
        else:
            break
        temp = a-b
        if temp != number:
            dq.append((temp,N,trg,num+1))  
        else:
            break 
        if num != 0:
            temp = a*b
            if temp != number:
                dq.append((temp,N,trg,num+1))  
            else:
                break
        elif num == 0:
            dq.append((N,N,trg,num+1))
          
        temp = a//b
        if temp != 0 and temp != number:
            dq.append((temp,N,trg,num+1))
        elif temp == number:
            break
        if b > 0:
            dq.append((temp,10*b+N,trg,num+1))
        if b < 0:
            dq.append((temp,10*b-N,trg,num+1))
    else:
        return -1

    return answer + 1

n = 5
number = 12
print(solution(n, number))
n = 2
number = 11
print(solution(n, number))
