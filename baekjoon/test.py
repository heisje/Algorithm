a = list(str(input()))
if '0' not in a:
    print(-1)
else:
    suma = sum(map(int,a))
    if suma % 3 == 0:
        a.sort(reverse=True)
        print(''.join(a))
    else:
        print(-1)