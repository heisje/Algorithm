from copy import deepcopy
def dfs(target, n, N, a_info, b_info, total):
    #print(target, n, N, a_info, b_info, total)
    global max_total
    global answer
    if n > N:  # 초과한 경우
        return
    elif n == N:  # 딱 맞춰 한 경우
        if max_total < total:
            max_total = total
            answer = deepcopy(b_info)
        return
    if target > 10:  # 멈춰!
        if max_total < total:
            max_total = total
            answer = deepcopy(b_info)
        return
    if a_info[target] == 0:
        # 비긴 경우
        dfs(target + 1, n + 0, N, a_info, b_info+[0], total + 0)
    else:
        # 진 경우
        dfs(target + 1, n + 0, N, a_info, b_info+[0], total - (10-target))
        # 비긴 경우
        if n + a_info[target] <= N:
            dfs(target + 1, n + a_info[target], N, a_info, b_info+[a_info[target]], total + 0)    
    # 이긴 경우
    if n + a_info[target] + 1 <= N:
        dfs(target + 1, n + a_info[target] + 1, N, a_info, b_info+[a_info[target]], total + (10-target))
def solution(n, info):
    global max_total
    global answer
    max_total = 0
    answer = []
    dfs(0, 0, n, info, [], 0)
    
    return max_total, answer

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))