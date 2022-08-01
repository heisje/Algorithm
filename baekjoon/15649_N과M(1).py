#https://www.acmicpc.net/problem/15649 
#핵심은 O(n!)인가..? 재귀 반복문을 내가 쓸 수 있을까

#DFS랑 BFS가 뭔데!

#재귀 함수 (N = 최대크기, m = 순열개수, check_box = 숫자가 사용되었는지, result_li = 결과, max_len = 최대길이)
def foring(N, m, check_box, result_li, max_len):
    if m == 0:
        print(*result_li)
        return
    for i in range(1, N + 1):
        if check_box[i] == False:
            result_li[max_len - m] = i
            check_box[i] = True
            foring(N,m - 1,check_box, result_li, max_len)
            result_li[max_len - m] = None
            check_box[i] = False
    return

#N은 숫자 최대크기, M은 길이
N, M = map(int,input().split()) 

check_box = {i:False for i in range(1, N + 1)} #숫자가 들어있는지 확인
result_li = [None for _ in range(M)] #결과값
max_len = M #최대길이
foring(N, M, check_box, result_li, max_len)
