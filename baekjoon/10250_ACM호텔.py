CASE_N = int(input())

input_li = []
answer = [[1, 0] for _ in range(CASE_N)] #x, y
for _ in range(CASE_N):
    input_li.append(list(map(int, input().split())))

for i, li in enumerate(input_li):
    H, W, num = li
    while True:
        if num <= H:
            answer[i][1] = num
            break
        elif num > H:
            num -= H
            answer[i][0] += 1

for x, y in answer:
    if x < 10:
        print(str(y)+'0'+str(x))
    if x >= 10:
        print(str(y)+str(x))


        
