from heapq import heappush, heappop

N = int(input())
heap = []
for n in range(N):
    a = int(input())
    if a == 0:
        pass
    else:
        heappush(heap, a)
print(heappop(heap)[1])