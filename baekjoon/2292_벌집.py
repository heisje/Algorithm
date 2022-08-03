N = int(input())
#1 + 6 + 12 + 18 +
#1     -1 
#2~7   1~6   -7
#8~19        1~12   -19
#20~37              1~18
count = 1
while N > 1:
    if 1 <= N <= 6 * count: #범위 안이면 return
        count += 1
        break
    elif 6 * count < N: #범위보다 크면
        N -= (6 * count)
        count += 1 

print(count)
        
