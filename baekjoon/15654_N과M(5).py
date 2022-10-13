def dfs(m, li):
    if m == M:
        print(*li)
        return
    for idx in range(len(arr)):
        if visited[idx] == 0:
            visited[idx] = 1
            dfs(m+1, li + [arr[idx]])
            visited[idx] = 0

N, M = map(int, input().split())
arr= sorted(list(map(int, input().split())))
visited = [0] * len(arr)
dfs(0,[])

#실버3 / 10분