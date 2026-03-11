from collections import deque
import sys
input = sys.stdin.readline

def makeNode(N, nodeInput):
    nodes = [[] for _ in range(N+1)]
    for s, e in nodeInput:
        nodes[s].append(e)
    return nodes 

def leafWrite(N, leafInput):
    values = [0 for _ in range(N+1)]
    for n, value in leafInput:
        values[n] = value

    return values

def dfs(depth, node):
    allData = []
    
    for go in nodes[node]:
        allData.append(dfs(depth+1, go))

    if allData:
        if depth % 2 == 1:
            nodeValues[node] = max(allData)
        else:
            nodeValues[node] = min(allData)
            
    return nodeValues[node]

def display():
    for q in qInput:
        print(nodeValues[q])

N, R = map(int, input().split())
nodeInput = [list(map(int, input().split())) for _ in range(N-1)]
L = int(input())
leafInput = [list(map(int, input().split())) for _ in range(L)]
Q = int(input())
qInput = [int(input()) for _ in range(Q)]

nodes = makeNode(N, nodeInput)
nodeValues = leafWrite(N, leafInput)
dfs(1, R)
display()