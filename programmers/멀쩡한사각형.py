import math

def solution(w,h):
    return w*h-(w+h-math.gcd(w,h))

# 0과 1의 차이
# 0, 1 * 3/2 - 1.5, 0~1 삭제
# 1과 2의 차이
# 1.5, 3 - 1~ 3에 딱 맞으므로 2까지 삭제

# 7 * 1.5 , 8 * 1.5
# 10.5, 12
# import math
# def solution(w,h):
#     answer = 0
#     ratio = h / w
#     # h를 최대 공약수로 나누고
    
#     before_save = 0
#     hole_save = 0
    
#         for ww in range(1, w // 2 + 1): 
#             after = ww * ratio
#             hole = math.ceil(after) - math.floor(before_save)
#             before_save = after

#             hole_save += hole
#         hole_save *= 2
    
#     return w * h - hole_save
