#나는야 포켓몬 마스터
import sys
input = sys.stdin.readline

case_num, question_num = map(int, input().rstrip().split()) #포켓몬 케이스의 개수, 질문의 개수

case_li = [None for i in range(case_num)]
dic = {}
ques_li = [None for i in range(question_num)]
answ_li = [None for i in range(question_num)]
for a in range(case_num): #케이스 num만큼 리스트에 저장
    case_li[a] = input().rstrip()
    dic[case_li[a]] = a+1

for b in range(question_num): #질문 num만큼 리스트에 저장
    ques_li[b] = str(input().rstrip())
    
    check = ord(ques_li[b][0]) 
    if check < 65: #숫자 질문
        answ_li[b] = case_li[int(ques_li[b])-1]
    elif check >= 65: #문자 질문
        answ_li[b] = dic[ques_li[b]]
    '''
    try:
        answ_li[b] = case_li[int(ques_li[b])-1]
    except:
        answ_li[b] = dic[ques_li[b]]
    '''

for d in answ_li: #답리스트 표현
    print(d)
