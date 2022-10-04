import sys
input = lambda: sys.stdin.readline()
import heapq

def find(i):
    while rep[i] != i:
        i = rep[i]
    return i

def union(i ,j):
    rep[find(i)] = find(j)

V, E = map(int, input().split())
nodes = []
rep = [i for i in range(V+1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    heapq.heappush(nodes, (C, A, B))

result = 0
node_count = 0
while node_count < V - 1:
    w, a, b = heapq.heappop(nodes)
    if find(a) != find(b): # 루프가 아니면
        union(a, b)
        result += w         # 결과
        node_count += 1
    if node_count == V - 1:
        break
print(result)