case_num = int(input())# 
case = [0]*case_num #케이스 리스트를 생성
case[0] = list(input()) #비교할 첫 번째 텍스트
for num in range(1, case_num): # 두 번째 부터 반복
    case[num] = list(input()) 
    for i in range(len(case[0])): #단어가 다 똑같은지 판별
        if case[num][i] != case[0][i]:
            case[0][i] = '?'#다르면 0번째에 ?대입
print(''.join(case[0]))