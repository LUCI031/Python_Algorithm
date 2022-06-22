import sys
import heapq as h
input=sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    a = int(input())
    if a == 0:
        if lst:
            print(h.heappop(lst))
        else:
            print(0)
    else:
        h.heappush(lst,a)