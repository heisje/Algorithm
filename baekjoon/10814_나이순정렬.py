N = int(input())

dic = dict()
for _ in range(N):
    age, name = input().split()
    age = int(age)
    if dic.get(age) == None:
        dic[age] = []
    dic[age].append(name)
li = sorted(dic)
for a in li:
    for value in dic[a]:
        print(a, value)