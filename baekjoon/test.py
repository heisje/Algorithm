from copy import deepcopy


def 음(n, li, 합계, ar):
    if n == N:
        print(li, ar)
        if 합계 > 10:
            print('10보다큼')
            return
        return
    for i in range(1,4):
        #ar2 = deepcopy(ar)
        ar2 = ar
        ar2.append(1)
        음(n+1, li+[i], 합계 + i, ar2)


N = int(input())
arr = [0, 0, 0]
음(0, [], 0, arr)