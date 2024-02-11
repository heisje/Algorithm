# def solution(picks, minerals):
#     global answer
    
#     answer = 50 * 25
#     # y = 곡괭이, x = 광물
#     tired = [
#         [1, 1, 1],
#         [5, 1, 1],
#         [25, 5, 1]
#     ]
#     mineralToNum = {
#         'diamond':0,
#         'iron':1,
#         'stone':2,
#     }
#     N = len(minerals)
#     minsNum = [mineralToNum[m] for m in minerals]
    
#     def dfs(start, result, picksLeft):
#         global answer
        
#         print(start, result, picksLeft)
#         # 종료조건
#         if sum(picksLeft) == 0 or start > N - 1:
#             answer = min(result, answer)
#             return
        
#         # 남은 곡괭이마다 dfs를 돌려줌
#         for p, _ in enumerate(picksLeft):
#             if picksLeft[p] == 0:
#                 continue
            
#             picksLeft[p] -= 1   # 곡괭이 제거
            
#             # 5개 까지 검증 or 끝에 다다르면 멈춤 
#             tempResult = 0      # 결과 저장
#             i = 0 
#             while i < 5 and start + i <= N - 1:
#                 tempResult += tired[picksLeft[p]][minsNum[start + i]]
#                 i += 1
            
#             result += tempResult
#             dfs(start + i, result, picksLeft[:])
#             result -= tempResult
#             picksLeft[p] += 1
            
#     dfs(0, 0, picks[:])
    
#     return answer

def solution(picks, minerals):
    sum = 0
    for x in picks:
        sum += x
    
    # 캘 수 있는 광물의 개수
    num_min = sum * 5
    if len(minerals) > num_min: # 주어진 광물이 캘 수 있는 광물 수보다 크면
        minerals = minerals[:num_min]
        
    # 광물 조사
    cnt_min = [[0, 0, 0]for x in range(10)] # dia, iron, stone
    for i in range(len(minerals)):
        if minerals[i] == 'diamond': 
            cnt_min[i//5][0] += 1
        elif minerals[i] == 'iron': 
            cnt_min[i//5][1] += 1
        else : 
            cnt_min[i//5][2] += 1

    # 피로도가 높은 순서대로 광물 정렬
    sorted_cnt_min = sorted(cnt_min, key = lambda x: (-x[0], -x[1], -x[2]))
    
    # 피로도 계산
    answer = 0
    for mineral in sorted_cnt_min:
        d, i, s = mineral
        for p in range(len(picks)):
            if p == 0 and picks[p]>0: # dia 곡괭이
                picks[p]-=1
                answer += d + i + s
                break
            elif p == 1 and picks[p]>0: # iron 곡괭이
                picks[p]-=1
                answer += 5*d + i + s
                break
            elif p == 2 and picks[p]>0: # stone 곡괭이
                picks[p]-=1
                answer += 25*d + 5*i + s
                break
                
    return answer