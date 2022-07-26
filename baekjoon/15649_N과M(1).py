#https://www.acmicpc.net/problem/15649 
#핵심은 O(n!)인가..? 재귀 반복문을 내가 쓸 수 있을까
'''
import copy
def sohard(li, count):
    sub_li = copy.deepcopy(li)
    for key in sub_li:
        if count == 0:
            return ' '
        else:
            sub_li.remove(key)
            return str(key) + ' ' + str(sohard(sub_li, count-1))
# M = maxi, N = N(num)
maxi, N = map(int,input().split())

result_li = [[] for _ in range(N)] #결과를 넣을 리스트

count = N
li = [i for i in range(1, maxi)] #숫자로 이루어진 list 생성
print(sohard(li, N))

'''

maxi, N = map(int,input().split()) 
real_result_li = []

for i in range(1, maxi):# 맨 앞자리 구하고
    li = [i for i in range(1, maxi)]
    result_li = [i]
    li.remove(i)
    for i in li:#맨 앞자리에서 쓴거 빼고 구하고
        result_li += i
        li.remove(i)
        for i in li:#빼고 빼고 구하고
            result_li += i
            li.remove(i)
            real_result_li.append(result_li)
print(real_result_li)

    
'''
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
'''
