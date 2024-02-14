from collections import deque
def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    A = deque(A)
    B = deque(B)
    # print(A, B)
    while A:
        bigA, bigB = A.popleft(), B[0]
        
        if bigA >= bigB:
            B.pop()
        elif bigA < bigB:
            B.popleft()
            answer += 1
    return answer