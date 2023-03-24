# https://school.programmers.co.kr/learn/courses/30/lessons/42890
from collections import defaultdict
from itertools import combinations
def solution(relation):
    answer = 0
    idxs = len(relation[0])
    rowLen = len(relation)
    # 후보키 체크 완료
    key = [1 for _ in range(idxs)]
    
    li = [defaultdict(int) for _ in range(idxs)]
    for row in relation:
        for idx, col in enumerate(row):
            if li[idx][col] == 0:
                li[idx][col] += 1
            else:
                key[idx] = 0
    

    canIdx = []
    cantIdx = []
    for i in range(len(key)):
        if key[i] == 0:
            canIdx.append(i)
        else:
            cantIdx.append((i,))

    answer += len(cantIdx)

    for num in range(2, idxs):
        # 두 줄을 체크한다.
        # col을 미리 추려낸다.
        canIdxList = []
        
        for combs in combinations(range(idxs), num):
            # 못하는 리스트에 있으면

            setCombs = set(combs)
            for cnt in cantIdx:

                a = set(cnt) - setCombs
                if not a:
                    # 추가하지 않는다.
                    break
            else:
                canIdxList.append(combs)
        
        # 추려낸 col을 사용해서 문자열을 생성한다.
        canList = []
        saveCan = [] # 잠시 저장해둘 공간
        for cols in canIdxList:
            saveCan = cols[:]
            check = defaultdict(int)
            for row in range(rowLen):
                fastBreak = False
                text = ''
                for col in cols:
                    text += relation[row][col]
                # 이미 들어왔던 숫자면
                if check[text] == 1:
                    fastBreak = True
                    break
                else:
                    check[text] = 1
            else:
                canList.append(saveCan[:])
                cantIdx.append(saveCan[:])
            if fastBreak:
                break
        answer += len(canList)
    
    return answer


a = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(a))

