# from collections import deque
# # 싣는다 : 최대한 먼 곳을 기준으로 최대한 싣는다. 
# # 내린다 : 최대한 먼 곳에서 싣고 최대한 가져온다.

# def solution(cap, n, deliveries, pickups):
#     answer = 0
#     # deliveries에 최대한 먼 곳부터 많이 싣는다.
#     # cap보다 많이 실으면 안된다.
#     dq = deque()
#     dq.append([])
#     tcap = cap  # 남은 공간
#     dcnt = sum(deliveries)
#     pcnt = sum(pickups)
    
#     for target, value in reversed(list(enumerate(deliveries))):
#         while value > 0 :
#             temp = min(value, tcap) # 최대 적재량
#             dq[len(dq) - 1].append((target, temp))  # dq에 적재 쌓기
#             tcap -= temp            # 적재 카운트 및 초기화
#             value -= temp
            
#             if tcap == 0:
#                 tcap = cap
#                 dq.append([])
    
#     new_pickups = []
#     for pickup, value in list(enumerate(pickups)):
#         if value > 0:
#             new_pickups.append([pickup, value])

    
#     last_pickup = [0, 0]
#     if new_pickups:
#         last_pickup = new_pickups.pop()
    
#     while dq:
#         delivery = dq.popleft()
#         if not delivery:
#             continue
        
#         last_delivery = delivery[0]
#         target = last_delivery[0]
#         if new_pickups:
#             target = max(last_pickup[0], last_delivery[0])
#         answer = answer + 2 * (target + 1)
#         tcap = cap  # 빈공간
#         # 회수하러 갈 곳이 남아있고, 빈공간이 꽉 찰 때 까지 
        
#         while new_pickups and tcap > 0:
#             temp = min(new_pickups[-1][1], tcap)
#             tcap -= temp
#             new_pickups[-1][1] -= temp
#             if new_pickups[-1][1] == 0:
#                 last_pickup = new_pickups.pop()
                
#     # 남아있는 new_pickups를 최대지점부터 빼면서 구함
#     tcap = cap
#     print(new_pickups)
#     while new_pickups:
#         temp = min(new_pickups[-1][1], tcap)
#         tcap -= temp
#         print(new_pickups, temp, tcap)
#         new_pickups[-1][1] -= temp
#         answer += new_pickups[-1][0]
        
#         if new_pickups[-1][1] == 0 or tcap == 0:
#             new_pickups.pop()
#             tcap = cap
    
#     return answer
def solution(cap, n, deliveries, pickups):
    d_val, p_val = 0,0
    answer = 0
    for i in range(n):
        d_val += deliveries[n-i-1]
        p_val += pickups[n-i-1]
        while p_val > 0 or d_val > 0:
            d_val -= cap
            p_val -= cap
            answer += 2 * (n-i)
    return answer