'''
index:1까지의 총합이 index:2의 숫자보다 2이상 차이나면
sum(0~1)+1이 empty_num


index:n까지의 총합이 index:n+1의 숫자보다 2이상 차이나면
sum(0~n)+1이 empty_num

sum(0) = 1
sum(0~1) = 1,2,3    (li[0]+li[1] + 1)

sum(0~n-1) = 1,2,3,4,5~M-1
sum(0~n) = 	(1,2,3,4,5~M-1)+(M)
		(sum(n-1)+li[n]=M)
'''
import sys

N = int(input())

chu = list(map(int, sys.stdin.readline().split())) ## 입력된 추
chu.sort()
empty_num = -1
num = 0 #현재 리스트의 순서

if num == 0:
    if chu[0] != 1:
        empty_num = 1
    else:    
        num = 1

pushsum = chu[0]
while num:
    pushsum += chu[num]
    #print(pushsum)
    if (num + 1 == N) or (chu[num + 1] >= pushsum + 2):
        empty_num = pushsum + 1
        break
    num += 1
    
print(empty_num)



