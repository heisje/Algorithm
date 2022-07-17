a = list(str(input()))
if '0' not in a:
    print(-1)
else:
    ''' 
    10ms 정도 차이나게 해준 코드
    sum = 0
    for i in a:
        sum += i
    '''
    suma = sum(map(int,a))
    if suma % 3 == 0:
        a.sort(reverse=True)
        '''
        40ms 정도 차이나게 해준 코드
        for i in a:
            print(i, end="")
        '''
        print(''.join(a))
    else:
        print(-1)