#연속하지 않는 alpabet를 찾는 것이 핵심

#입력받기
N = int(input()) #N은 반복의 개수
count = 0 #결과를 담을 count

# N만큼 문자열
case_li = [None for _ in range(N)] #입력 받을 문자열 리스트
for i in range(N):
    case_li[i] = list(input())
#print(case_li)

#검증
for case in case_li:
    dic = dict()#값을 넣을 dict소환 dict에 key:알파벳 value:index를 넣어 value가 2이상 차이나면 break

    for i in range(len(case) - 1, -1, -1): # ==i[::-1] pop을 할거라, 문자열 뒤쪽부터 
        #print(dic)
        alpa = case.pop()
        if dic.get(alpa) == None:
            dic[alpa] = i
        else:
            #있는데, 통과 되는 경우
            if dic.get(alpa) - i == 1: # 8 6
                dic[alpa] = i
            #있는데, 통과 안되는 경우
            else:
                #dic[alpa] = i
                break
    else:
        count += 1   
print(count)