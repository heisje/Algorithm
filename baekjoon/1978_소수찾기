N = int(input())
list_num = list(map(int, input().split()))

def sosu(a):
    if a == 1 or a == 0:
        return False
    if a == 2:
        return True 

    for i in range(2, a // 2 + 1):
        if a % i == 0 :
            return False
    return True

resulty = list(map(sosu,list_num)).count(True)
print(list(map(sosu,list_num)))
print(resulty)