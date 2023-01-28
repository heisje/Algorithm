from collections import deque

def solution(gems):
    # 모든 보석 찾기
    # 한 개를 지날 때 마다 visited에 인덱스를 추가함
    #
    # 시작점 끝점 구하는 법
    # 시작점을 저장하고, 
    #   다른것이 들어오면 
    #   일단 추가
    #   만약 중복을 찾을 시
    #   맨 앞에 중복이 위치한다면 맨앞을 한 칸뒤로
    #   맨앞이 중복이 없어질 떄 까지 추가
    #
    # 결과 찾기
    # visited가 전부 다 차면 
    #   최대 길이를 체크하고 
    #   시작점 끝 점을 넣는다
    jewelrys = dict()
    for gem in gems:
        jewelrys[gem] = deque()
    N = len(list(jewelrys))
    n = 0
    start = 0 # 시작점
    save = (len(gems), 0, 0) # 결과
    for idx, gem in enumerate(gems):
        jewelrys[gem].append(idx)
        # 중복이면
        if len(jewelrys[gem]) > 1:
            # start가 중복이면 start를 하나씩 미룬다.
            while len(jewelrys[gems[start]]) > 1:
                jewelrys[gems[start]].popleft()
                start += 1
        # 중복한 게 아니면 n + 1
        else:
            n += 1

        # 결과 체크
        if n == N and save[0] > idx-start:
            save = (idx-start, start+1, idx+1)
        
    return [save[1], save[2]]

a = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(a))
a = ["AA", "AB", "AC", "AA", "AC"]
a = ["XYZ", "XYZ", "XYZ"]
a = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]