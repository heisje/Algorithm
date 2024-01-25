# def solution(scores):
#     answer = 1
#     scr_li = sorted(scores[1:], key = lambda x:-x[0]-x[1])
#     whn = sorted(scores[0])
#     whn_sum = whn[0] + whn[1]
#     # 앞이 큰 것, 뒤가 큰 것
#     check = [[0, 0], [0, 0]]
    
#     for score in scr_li:
#         # score.sort()
        
#         # 완호와 비교해서 합이 같거나 작은 경우 = 정답 도출
#         if whn_sum >= score[0] + score[1]:
#             break
#         # 완호 보다 큰 경우
#         else:
#             # 둘다 작지 않은 경우
#             if not ((score[0] < check[0][0] and score[1] < check[0][1]) or (score[0] < check[1][0] and score[1] < check[1][1])):
#                 answer += 1
            
#             # 앞자리가 큰 경우 -> check 1과 대치
#             if score[0] > check[0][0]:
#                 if check[0][1] > check[1][1]:
#                     check[1] = check[0][:]
#                 check[0] = score[:]

#             # 뒷자리가 큰 경우 -> check 2와 대치
#             if score[1] > check[1][1]:
#                 if check[0][0] < check[1][0]:
#                     check[0] = check[1][:]
#                 check[1] = score[:]
        
#     if (whn[0] < check[0][0] and whn[1] < check[0][1]) or (whn[0] < check[1][0] and whn[1] < check[1][1]):
#         return -1
#     return answer

def solution(scores):
    answer = 1

    target = scores[0]
    target_score = sum(scores[0])
    scores.sort(key=lambda x: (-x[0], x[1]))

    threshold = 0
    for score in scores:
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        if threshold <= score[1]:
            if target_score < score[0] + score[1]:
                answer += 1
            threshold = score[1]
    return answer
    
    