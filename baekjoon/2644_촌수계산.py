import sys
sys.stdin = open('input.txt')

def dfs(s, count = 0):
    if s == END:
        result_count.append(count)
        return
    #if node_map[s] != []:
    for node in node_map[s]:
        if node not in visited:
            count += 1
            visited.add(node)
            dfs(node, count)
            visited.remove(node)
            count -= 1
N = int(input())
START, END = map(int, input().split())
NODE_NUM = int(input())
node_map = {i:[] for i in range(N+1)}
visited = set()
result_count = []
#인풋
for idx in range(NODE_NUM):
    a, b = map(int, input().split())
    node_map[a].append(b)
    node_map[b].append(a)
dfs(START)
if len(result_count) == 0:
    print(-1)
else:
    print(result_count[0])


