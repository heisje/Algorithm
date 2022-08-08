import sys
sys.stdin = open('input.txt')

N = int(input())
li = []
for testcase in range(N):
    li.append(list(map(int, input())))
result = []                            #결과값 저장할 리스트
for testcase_li in li:
    check_dict = {}                    #나는 딕셔너리로 풀어야지~~
    check_babygin = 0                  #중요!! 이게 2넘으면 baby인거임

    #모든 테스트 케이스의 리스트를 check_딕셔너리로 바꿈
    for i in testcase_li:
        if check_dict.get(i) == None:
            check_dict[i] = 1
        else:
            check_dict[i] += 1

    #딕셔너리 검증
    for key, value in check_dict.items():
        # 3의 배수이면 3의 배수만큼 빼준다.
        if value % 3 == 0:
            check_dict[key] -= 3 * (value // 3)
            check_babygin += value // 3

        #연속된 숫자 체크
        if check_dict[key] > 0 and check_dict.get(key+1) != None and check_dict.get(key+1) >= 1 and check_dict.get(key+2) != None and check_dict.get(key+2) >= 1:
            check_dict[key] -= 1
            check_dict[key + 1] -= 1
            check_dict[key + 2] -= 1
            check_babygin += 1

        #2이상이면 1누적
        if check_babygin >= 2:
            result.append(1)
            break
    else:
        #1이 누적되지 않았으면, 0누적
        result.append(0)

#결과값 출력
print(result)
for testcase in range(N):
    print(f'#{testcase + 1} {result[testcase]}')