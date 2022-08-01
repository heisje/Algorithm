#https://www.acmicpc.net/source/31450065 << 쉽게 잘 푼 답안

a = int(input())
return_tuple = tuple()
for aa in range(a):
    max_x, max_y, bug_num = map(int,input().split()) # b_n 배추num
    bat = [0] * max_x * max_y
    for i in range(bug_num):
        x, y = map(int, input().split())#지렁이 위치
        bat[x + max_x*(y)] = 1

    count = 2 #숫자 넣을거 보조도구
    roop = True
    while roop == True:
        roop = False
        sub = -1
        for i in range(len(bat)):
            sub = bat[i]
            if bat[i] >= 1:
                check = [0, 0, 0, 0, 0] #상 좌 우 하 본인자리
                check[4] = bat[i]
                low = 1000
                if i // max_x != 0: #상단 모서리가 아니면
                    if bat[i - max_x] != 0: #상단 체크
                        check[0] = bat[i - max_x] #탑 숫자 체크
                        if low > check[0] and check[0] != 1:
                            low = check[0]
                if i % max_x != 0: #좌측 모서리가 아니면
                    if bat[i-1] != 0:
                        check[1] = bat[i-1] 
                        if low > check[1] and check[1] != 1:
                            low = check[1]
                if i % max_x != max_x - 1: #우측변
                    if bat[i + 1] != 0:  
                        check[2] = bat[i + 1]   
                        if low > check[2] and check[2] != 1:
                            low = check[2]
                if i // max_x != max_y - 1: #하단변
                    if bat[i + max_x] != 0: 
                        check[3] = bat[i + max_x] 
                        if low > check[3] and check[3] != 1:
                            low = check[3]

                if check[0] == 0 and check[1] == 0 and bat[i] == 1:
                    count += 1
                    bat[i] = count

                if low == 1000: low = 0

                if low != 0: #2는 한번 처리한 숫자다, 2이상이 있으면
                    bat[i] = low
                    if check[0] >= 2: #위숫자 있으면
                        bat[i - max_x] = low
                    if check[1] >= 2: #좌숫자있으면
                        bat[i - 1] = low
                    if check[2] >= 2: #우숫자있으면
                        bat[i + 1] = low
                    if check[3] >= 2: #하
                        bat[i + max_x] = low
            if sub != bat[i]:
                roop = True

    return_tuple += (len(set(bat)-{0}),)
    #print(return_tuple)

for i in return_tuple:
    print(i)

