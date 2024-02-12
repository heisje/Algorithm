# from collections import deque

# INF= 12319203910

# def solution(target):
#     dp = [[MAX, -MAX] for _ in range(target+1)]
#     answer = [INF, 0]
    
#     scores = []
#     scores.append((50, -1))
#     for i in range(20, 0, -1):
#         scores.append((i, -1))
#         scores.append((i*3, 0))
#         scores.append((i*2, 0))
        
    
#     print(scores)
#     dq = deque()
#     dq.append((0, 0, 0))
#     while dq:
#         score, dart, single = q.popleft()
        
#     def dfs(t, b):
#         global answer
        
#         for s, bb in scores:
#             if t - s == 0:
#                 answer = min(answer, [t+1, b+bb])
#             elif t - s < 0:
#                 pass
#             elif t - s > 0:
#                 dfs(t-s, b+bb)
                
#     dfs(target, 0)
                
#     return [answer[0], -answer[1]]

def solution(target):
    # 다트 하나를 던졌을 때 나올 수 있는 모든 점수에 대해서,
    # 싱글/불로 만들 수 있으면 1, 없으면 0을 반환하는 딕셔너리 P
    # 를 고려한다.
    P = {}  # {score: sb} 점수, single or bull 인지
    for i in range(1, 21):
        P[2 * i] = 0
        P[3 * i] = 0
		# <최선의 상황만 고려>
		# 싱글/불로 만들 수 있는 점수는 항상 싱글/불로 만든다고 가정한다.
    for i in range(1, 21): # Single일 때를 1로 덮어씌운다.
        P[i] = 1
    P[50] = 1 # bull일 때를 1로 덮어씌운다.
    
    # cnt[i] 는 i를 만드는 최선의 다트 수 (최소한의 다트 수)
    cnt = [100001] * 100001
    # cntBull[i]는 i를 만드는 최선의 조합 중에서 최대의 싱글or불 수
    cntBull = [0] * 100001
		
		# 다트 딱 하나를 던져서 만들 수 있는 점수라면,
		# cnt[i] 는 1이고, 싱글/불 여부는 미리 만들어 놓은 P에서 얻어오면 된다.
    for i, sb in P.items():
        cnt[i] = 1
        cntBull[i] = sb

    for t in range(1, target + 1):
        if cnt[t] != 100001:
            continue
            
        mn, sb = 100001, 0
        for score, _sb in P.items():
            if t - score < 0:
                continue
                
            s = t - score
            if (cnt[s] + 1 < mn) or (cnt[s] + 1 == mn and cntBull[s] + _sb > sb):
                mn = cnt[s] + 1
                sb = cntBull[s] + _sb

        cnt[t] = mn
        cntBull[t] = sb

    return [cnt[target], cntBull[target]]