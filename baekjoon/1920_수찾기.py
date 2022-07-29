N = int(input())

li_top = set(input().split())

NN = int(input())

li_under = list(input().split())

for li_t in li_under:
    if li_t in li_top:
        print(1)
    else:
        print(0)
