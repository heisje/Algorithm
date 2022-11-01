def solution(n, k):

    # k진수로 변환하기
    arr = []
    while n >= k:
        temp = n % k
        n = (n - temp) // k
        arr.append(str(temp))
    arr.append(str(n))
    arr.reverse()
    nums = ''.join(arr).split('0')

    # 소수인지 확인하기
    answer = 0
    for num in nums:
        if num:  # '' 값도 들어가서
            num = int(num)
            if num > 1:  # 1이랑 0을 안 더해주려고
                answer += 1  # 일단 더하고
                for i in range(2, int(num**(0.5)+1)):
                    if num % i == 0:
                        answer -= 1  # 소수아니면 빼기
                        break
    return answer

print(solution(437674,3))
print('-----')
print(solution(110011,10))

