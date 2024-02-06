def solution(e, starts):
    answer = []
    divisors = [0 for i in range(e+1)]
    answers = [0 for i in range(e+1)]
    temp = 0

    for n in range(1, int(e**0.5)+1):
        divisors[n*n] += 1
        for i in range(n*(n+1), e+1, n):
            divisors[i] += 2
            
    for i in reversed(range(e+1)):
        if divisors[i] >= temp:
            temp = divisors[i]
            answers[i] = i
        else:
            divisors[i] = temp
            answers[i] = answers[i+1]

    for i in starts:
        answer.append(answers[i])

    return answer
# 출처: https://inspirer9.tistory.com/436 [DeveloperUnknown:티스토리]