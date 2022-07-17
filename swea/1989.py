num = int(input())
test = list()
for i in range(0, num):
    check = 1
    test.append(0)
    test[i] = str(input()).strip()
    for j in range(0, len(test[i])):
        if test[ i ][ j ] != test[ i ][len(test[ i ]) - j -1 ]:
            check = 0
    if check == 1:
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')