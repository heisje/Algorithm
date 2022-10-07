def nm(m, li):
    if m == M:
        print(*li[1:])
        return
    for a in arr:
        if a > li[-1]:
            nm(m+1,li+[a])
N, M = map(int, input().split())
arr = list(range(1,N+1))
nm(0, [0])