import sys
sys.stdin = open('input.txt')

for testcase in range(10):#10번 반복
    N = int(input()) #건물 개수
    buliding = list(map(int, input().split())) #빌딩 리스트

    results = 0 #결과값
    for i in range(2, len(buliding)-2): #i는 체크중인 아파트 index
        check = max(buliding[i - 2], buliding[i - 1], buliding[i + 1], buliding[i + 2])
        if buliding[i] > check: #만약, 좌우 두칸만큼보다 i가 크면
            results += buliding[i] - check
    print(f'#{testcase + 1} {results}') #출력