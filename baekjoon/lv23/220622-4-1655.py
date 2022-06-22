import sys
import heapq as h
input=sys.stdin.readline

N = int(input())
lmax = []
rmin = []

for _ in range(N):
    num = int(input())
    if len(lmax) == len(rmin):
        h.heappush(lmax, -num)
    else:
        h.heappush(rmin,num)
    if rmin and rmin[0] < -lmax[0]:
        lval = h.heappop(lmax)
        rval = h.heappop(rmin)
        h.heappush(rmin,-lval)
        h.heappush(lmax,-rval)
    print(-lmax[0])