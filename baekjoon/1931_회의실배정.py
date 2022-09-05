import sys
input = lambda:sys.stdin.readline().strip()

def dfs(n, count):
    if n >= END:
        result.append(count)
        return
    for a in range(len(arr)):
        if visited[a] == 0 and n <= arr[a][0]:
            visited[a] = 1
            dfs(arr[a][1], count + 1)
            visited[a] = 0
    else:
        result.append(count)
        return


N = int(input())
arr = []
for n in range(N):
    s, e = map(int, input().split())
    arr.append([s, e])
arr.sort()
visited = [0]*N
END = max(arr,key=lambda a:a[1])[1]
result = []
dfs(0, 0)
print(max(result))
#수열을 만들어보고 싶은데, dfs 거리로 하는 게 쉽겠다.
