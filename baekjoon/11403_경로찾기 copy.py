import sys
input = lambda:sys.stdin.readline()
sys.setrecursionlimit(150000)

def dfs(i):
    for jdx, value in enumerate(node[i]):
        if value == 1 and visited[i][jdx] == 0:
            result_temp[jdx] = 1
            visited[i][jdx] = 1
            dfs(jdx)
            visited[i][jdx] = 0
    

N = int(input())
node = []
for _ in range(N):
    node.append(list(map(int, input().split())))

# 노드마다 모두 방문해서, 모든 노드로 출발시켜본다.
result = [[-1 for _ in range(N)] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if result[i][j] == -1:
            dfs(i)
        for j, value in enumerate(result_temp):
            if value == 1:
                result[i][j] = 1

for i in range(N):
    print(*result[i])