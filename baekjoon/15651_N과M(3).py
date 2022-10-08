def nPm(m, li):
    if m == 0:
        print(*li)
        return
    for n in range(1,N+1):
        nPm(m-1, li+[n])


N, M = map(int, input().split())
arr = list(range(1, N+1))
nPm(M, [])
