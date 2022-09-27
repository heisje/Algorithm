N = int(input())
node = []
result = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    node.append(list(map(int, input().split())))

# 노드마다 모두 방문해서, 모든 노드로 출발시켜본다.

            


for i in range(N):
    print(*result[i])