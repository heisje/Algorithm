#https://www.acmicpc.net/problem/1244

#문제:   1.스위치를 주고
#        2.성별이 남자일 때
#        3.성별이 여자일 때
N = int(input())
switch = list(map(int, input().split()))
HU_NUM = int(input())

change = lambda a:abs(a-1)
for _ in range(HU_NUM):
    gender, idx = map(int, input().split()) #성별과 바꿀 스위치 값
    if gender == 1:
        for i in range(len(switch)):
            if i % idx == idx - 1:
                switch[i] = change(switch[i])
                #print(switch)

    if gender == 2:
        idx -= 1
        if len(switch) - idx > idx: # 스위치 값이 중앙보다 작으면
            switch[idx] = change(switch[idx])
            for i in range(1, idx + 1): # 0까지만 비교
                if switch[idx - i] == switch[idx + i]: 
                    switch[idx - i] = change(switch[idx - i])
                    switch[idx + i] = change(switch[idx + i])
                    #print(switch)
                else:
                    break
        else:                       # 스위치 값이 중앙보다 크면
            #print('here')
            switch[idx] = change(switch[idx])
            #print(1, N - idx) 
            for i in range(1, N - idx): #HU_NUM까지만 비교
                #print(i)
                #print(switch[idx - i],switch[idx + i])
                if switch[idx - i] == switch[idx + i]:
                    #print('before:',switch)
                    switch[idx - i] = change(switch[idx - i])
                    switch[idx + i] = change(switch[idx + i])
                    #print('after:',switch)
                else:
                    break
for i in range(0,len(switch),10):
    print(*switch[i:i+10])
    
