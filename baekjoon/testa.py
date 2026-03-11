import heapq

N = int(input())
heights = list(map(int, input().split()))

maxHeight = 0
saveHeight = []

for n in range(N):
	heapq.heappush(saveHeight, heights[n])
	
print(list(heapq))
