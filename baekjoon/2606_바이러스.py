N = int(input())
cntNodes = int(input())
nodes = [[] for _ in range(N+1)]
for _ in range(cntNodes):
    matchA, matchB = map(int, input().split())
    nodes[matchA].append(matchB)
    nodes[matchB].append(matchA)


stack = [1]
visited = set([1])
while stack:
    node = stack.pop()
    
    for goNode in nodes[node]:
        if goNode not in visited:
            visited.add(goNode)
            stack.append(goNode)

answer = len(visited-set([1])) 
print(answer)