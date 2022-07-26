#https://www.acmicpc.net/problem/1259
result_li = []
while True:
    a = str(input())
    if a == '0':
        break
    # a = 5 -> 2    a = 6 -> 3
    # 01 2 34       012 345
    if a[:len(a) // 2] == a[len(a) - 1:len(a) - 1 - len(a)//2:-1]:
        result_li.append('yes')
    else:
        result_li.append('no')

for string in result_li:
    print(string)