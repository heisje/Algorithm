# 뒤로갔다가 앞으로 가는 경우
# A A A B A A A A A A B B
# 직선으로 가는 경우
# 뒤로만 가는 경우
def solution(name):
    cnt = 0
    for i in range(len(name)):
        cnt += min(ord(name[i]) - ord('A'), 1 + ord('Z') - ord(name[i]))
    
    
    # A를 전부 찾아 계산식에 의해 계산을 한다.
    # 계산식1 = n - 1 - A끝
    # 계산식2 = A시작 - 1
    # 두개 중 작은 것 * 2 + 큰 수
    move_cnt = len(name) - 1
    stack = []
    for i in range(1, len(name)):
        if ord(name[i]) == ord('A'):
            stack.append(i)
        elif stack:
            startA, endA = stack[0], stack[len(stack) - 1]
            temp1 = len(name)-1-endA
            temp2 = startA-1
            
            temp_cnt = 0
            if temp1 > 0 and temp2 > 0:
                temp_cnt = min(temp1, temp2) * 2 + max(temp1, temp2)
            if temp1 == 0 or temp2 == 0:   # 앞으로 또는 뒤를 왕복할 필요가 없는 경우
                temp_cnt = max(temp1, temp2)
            move_cnt = min(move_cnt, temp_cnt)
            stack = [] 
    if stack:
        startA, endA = stack[0], stack[len(stack) - 1]
        temp1 = len(name)-1-endA
        temp2 = startA-1

        temp_cnt = 0
        if temp1 > 0 and temp2 > 0:
            temp_cnt = min(temp1, temp2) * 2 + max(temp1, temp2)
        if temp1 == 0 or temp2 == 0:   # 앞으로 또는 뒤를 왕복할 필요가 없는 경우
            temp_cnt = max(temp1, temp2)
        move_cnt = min(move_cnt, temp_cnt)
        stack = [] 
            
    
    return move_cnt + cnt