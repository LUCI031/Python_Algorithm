import sys
import heapq as h
input = sys.stdin.readline

heaps = []

N, M = map(int,input().split())
lst = list(map(int,input().split()))
for i in range(N):
    h.heappush(heaps,lst[i])


for _ in range(M):
   a = h.heappop(heaps)
   b = h.heappop(heaps)
   h.heappush(heaps,a+b)
   h.heappush(heaps,a+b)

print(sum(heaps))