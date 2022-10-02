import sys
input = lambda : sys.stdin.readline()
import heapq

N = int(input())
M = int(input())
nodes = [[]for _ in range(N+1)]
node_costs = [ 100000000 for _ in range(N+1)]
for m in range(M):
    start, end, cost = map(int, input().split())
    nodes[start].append((cost, end))
START, END = map(int, input().split())
q = []
node_costs[START] = 0
heapq.heappush(q, (0, START))
while q:
    stack_cost, pre = heapq.heappop(q)
    if pre == END:
        break
    for go_cost, go_node in nodes[pre]:
        temp = stack_cost + go_cost
        if temp < node_costs[go_node]:
            node_costs[go_node] = temp
            heapq.heappush(q, (temp, go_node))

#print(node_costs)
print(node_costs[END])

#골드5 / 15분 / 312ms