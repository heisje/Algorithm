N = int(input())
# li = [0]*N
# for i in range(N):
#     li[i] = int(input())
# for i in range(N):
#     for j in range(N):
#         if i != j and li[i] < li[j]:
#             li[j], li[i] = li[i] ,li[j]

dic = {} 
for i in range(N):
    a = int(input())
    if dic.get(a) == None:
        dic[a] = 1
    else:
        dic[a] += 1
for a in range(0, 10001):
    if dic.get(a) == None:
        pass
    else:
        print(str(a) * dic.get(a))
