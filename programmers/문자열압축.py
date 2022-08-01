from collections import deque
def solution(s):
    N = len(s)      #s길이
    i = 0           #index
    count = 1    #개수로 뽑아냄
    edits = []   #수정된 리스트 전부받음
    len_li = []  #길이 검출을 위함2
    while True:
        edits.append(s[i:i + count])
        i = i + count
        if i + count > N:
            #print(edits)
            len_edit = N  #edit 길이 검출을 위함
            continu = 0
            for idx in range(1, len(edits)):      # 압축
                if edits[idx - 1] == edits[idx]:  # 숫자 붙이기  
                    len_edit -= len(edits[idx]) 
                    if continu > 1:               
                        continu += 1
                        if continu == 10:        #자릿수 검증
                            len_edit += 1
                        elif continu == 100:
                            len_edit += 1
                        elif continu == 1000:
                            len_edit += 1
                    elif continu == 0:
                        continu += 2
                        len_edit += 1
                else:
                    continu = 0
            #print(len_edit)
            #초기화 구문
            len_li.append(len_edit)
            #print(len_li)
            i = 0
            count += 1
            len_edit = N
            continu = 0
            edits.clear()
            
        # count가 N보다 클 필요는 없어 제외
        if count > N // 2:
            break
    
    answer = min(len_li)
    return answer