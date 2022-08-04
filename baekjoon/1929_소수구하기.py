from math import sqrt

min, max = map(int,input().split())
list_num = [i for i in range(min, max + 1) ]#[i if i % 2 != 0 else 1 for i in range(min, max + 1) ]

def sosu(a):
    if a == 1 or a == 0:
        return False
    if a == 2:
        return True 

    for i in range(2, int(sqrt(a)) + 1):
        if a % i == 0 :
            return False
    return True

list_num = list(map(sosu,list_num))
#print(list_num)
for i, value in enumerate(list_num, min):
    if value == True:
        print(i)