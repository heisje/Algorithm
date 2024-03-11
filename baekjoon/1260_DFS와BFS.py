# https://www.acmicpc.net/problem/1260
from collections import deque

def dfs(pre):
    for go in nodes[pre]:
        if visitedDfs[go] is False:
            visitedDfs[go] = True
            answerDfs.append(go)
            dfs(go)
    
def bfs(start):
    answer = []
    queue = deque([start])
    visited = set([start])
    while queue:
        pre = queue.popleft()
        answer.append(pre)

        for go in nodes[pre]:
            if go not in visited:
                visited.add(go)
                queue.append(go)
    
    return answer
N, M, V = map(int, input().split())
nodes = [[] for _ in range(N+1)]
for _ in range(M):
    from_, to_ = map(int, input().split())
    nodes[from_].append(to_)
    nodes[to_].append(from_)

for i in range(len(nodes)):
    nodes[i].sort() # reverse=True

visitedDfs = [False for _ in range(N + 1)]
visitedDfs[V] = True
answerDfs = []
dfs(V)
print(f'{V} '+ " ".join(map(str, answerDfs)))
print(" ".join(map(str, bfs(V))))
    