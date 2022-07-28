import sys, heapq
input = sys.stdin.readline

N = int(input())

lst = []
cnt = 0
cand = int(input())
for i in range(N-1):
    heapq.heappush(lst,-int(input()))

if len(lst) == 0:
    print(0)
    exit()
    
while True:
    compe = -(heapq.heappop(lst))
    if cand > compe:
        print(cnt)
        exit()
    else:
        cnt += 1
        cand += 1
        heapq.heappush(lst,-(compe-1))