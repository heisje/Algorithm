# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 10분
def solution(s):
    answer = True
    
    stack = []
    for ss in s:
        if ss == "(":
            stack.append(1)
        if ss == ")":
            if stack and stack[-1] == 1:
                stack.pop()
            else:
                return False
    else:
        if stack == []:
            return True
    return False


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))