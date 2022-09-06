from math import sqrt
N = int(input())

if sqrt(N) % 1 == 0:
    print(1)
else:
    plus = 0
    for i in range(int(sqrt(N))+1): 
        for j in range(int(sqrt(N))+1): 
            for k in range(int(sqrt(N))+1): 
                # i=0, j=0, k=정수인 경우 plus가 0이여서 총 합이 1부터 다 찾고
                # i=0, j=정수, k=정수인 경우 plus가 1이여서 총 합이 2를 다 찾고 ...
                find = i**2 + j**2 + k**2
                if find == N: 
                    print(1+plus)     
                    exit()
                if find > N:
                    break
            if plus == 0:
                plus = 1
        plus = 2 
    print(4)