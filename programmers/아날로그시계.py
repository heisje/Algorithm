# 초침 시침 분침이 모두 겹치는 경우의 수는 12시와 24시밖에 없다고 가정한다.
# 그렇다면 60초가 지날 때 마다 2번의 알람이 울리게 된다.
# 초침이 중요한 첫 0초까지, 마지막 0초 이후만 검증하고 나머지는 연산으로 처리한다.
def solution(h1, m1, s1, h2, m2, s2):
    
    # 분 검증
    
    
    # 초 검증
    h1_anc = (h1 % 12) / 12 + m1 / 2
    m1_anc = m1 * 6
    s1_anc = s1 * 6
    
    h2_anc = (h2 % 12) / 12 + m2 / 2
    m2_anc = m2 * 6
    s2_anc = s2 * 6
    
    if h1 == h2 and m1 == m2:
        answer = 0
        if s1_anc <= h1_anc <= s2_anc or s1_anc <= h1_anc <= s2_anc:
            answer += 1
        if s1_anc <= m1_anc <= s2_anc or s1_anc <= m2_anc <= s2_anc:
            answer += 1
        print('2-1', answer)
    else:
        answer = 2 * ((h2 * 60 + m2) - (h1 * 60 + m1) - 1)
        
        if s1_anc <= m1_anc:
            answer += 1
        if s1_anc <= h1_anc:
            answer += 1
        
        if s2_anc >= m2_anc:
            answer += 1
        if s2_anc >= h2_anc:
            answer += 1
        print('2-2', answer)
    
    
    return answer

# def solution(h1, m1, s1, h2, m2, s2):
#     answer = 0
#     startTime = h1 * 3600 + m1 * 60 + s1
#     endTime = h2 * 3600 + m2 * 60 + s2  
    
#     s = 0
#     hBeAnc = (startTime / 120) % 360
#     mBeAnc = (startTime / 10) % 360
#     sBeAnc = (startTime * 6) % 360
#     while startTime < endTime and s < 3:
#         # 시침의 각도, 분침의 각도, 초침의 각도를 구한다.
#         hAnc = (startTime / 120) % 360
#         mAnc = (startTime / 10) % 360
#         sAnc = (startTime * 6) % 360
        
#         if sAnc == mAnc and sAnc == hAnc:
#             answer += 1
#         elif sAnc == mAnc:
#             answer += 1
#         elif sAnc == hAnc:
#             answer += 1
            
#         startTime += 1
#         hBeAnc, mBeAnc, sBeAnc = hAnc, mAnc, sAnc
#         # print(hAnc, mAnc, sAnc)
#         s+= 1
#     return answer