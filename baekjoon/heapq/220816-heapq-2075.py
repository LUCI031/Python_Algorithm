import sys
import heapq as h
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    nums = list(map(int,input().split()))
    for num in nums:
        h.heappush(lst,-num)
    lst.sort()
    lst = lst[:N+1]
for _ in range(N):
    a = h.heappop(lst)

print(-a)