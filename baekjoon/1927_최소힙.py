<<<<<<< HEAD
import heapq
import sys
N = int(input())

a = []
for _ in range(N):
    value = int(sys.stdin.readline())
    if value == 0:
        if a:
            print(heapq.heappop(a))
        else:
            print(0)
    else:
        heapq.heappush(a, value)
=======
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
>>>>>>> 3873b7129a8a9b96a1277dbad8c4a68aaec7c45f
