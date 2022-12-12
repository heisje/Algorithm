# https://school.programmers.co.kr/learn/courses/30/lessons/67257
from itertools import permutations

def solution(expression):
    answer = 0
    
    used = set()
    list_ex = []
    temp = ""

    # 연산자랑 숫자랑 나눠서 리스트를 생성하는 과정
    for i in expression:
        if i.isdigit():
            temp += i
        else:
            list_ex.append(temp)
            temp = ""
            used.add(i)
            list_ex.append(i)
    list_ex.append(temp)
    
    
    # 결과값 저장
    max_result = 0
    # 우선순위를 만들고
    for crud in permutations(used, len(used)):
        list_ex_copy = list_ex[:]
        result = 0
        # 우선순위 대로 돌면서
        for choice in crud:

            #우선순위에 맞는 연산을 전부 수행시킨다.
            for idx, value in enumerate(list_ex_copy):
                # 연산자를 찾으면
                if choice == value:
                    # 연산을 수행
                    result = 0
                    front = 1
                    back = 1
                    # 비어있으면 왔다리 갔다리 하면서 찾는다.
                    while list_ex_copy[idx-front] == "":
                        front += 1
                    while list_ex_copy[idx+back] == "":
                        back += 1
                    front_val = int(list_ex_copy[idx-front])
                    back_val = int(list_ex_copy[idx+back])
                    
                    # 주어진 연산 시행
                    if choice == "*":
                        result = front_val * back_val
                    if choice == "+":
                        result = front_val + back_val
                    if choice == "-":
                        result = front_val - back_val
                    
                    # 결과를 중간값만 제대로 된걸로 만드러버려!
                    list_ex_copy[idx-front] = ""
                    list_ex_copy[idx] = result
                    list_ex_copy[idx+back] = ""

        if max_result < abs(result):
            max_result = abs(result)
    return max_result

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))