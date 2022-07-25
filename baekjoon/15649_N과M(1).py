#https://www.acmicpc.net/problem/15649 
#핵심은 O(n!)인가..? 재귀 반복문을 내가 쓸 수 있을까

#첫번째 자리 구하기
def foring(M, N):
    for i in range(1, M + 1):
        if N == 1:
            return str(i)
        else:
            return str(i) + " " + str(foring(M,N - 1)) #마지막 자리까지 

M, N = map(int,input().split()) #M은 숫자 최대크기, N은 길이
result_li = []
print(foring(M, N))
#print(result_li)

