import sys
import heapq as h
input = sys.stdin.readline

days, sum_likes, kind = map(int,input().split())
find = False
n_alch = 0
s = 0
lst = []
hq = []

for _ in range(kind):
    likes, alch = map(int,input().split())
    lst.append((likes,alch))
lst.sort(key=lambda x:(x[1],x[0]))

for i in range(kind):
    h.heappush(hq, lst[i][0])
    s += lst[i][0]
    n_alch = lst[i][1]
    if len(hq) == days:
        if s >= sum_likes:
            find = True
            print(n_alch)
            break
        else:
            s -= h.heappop(hq)

if not find:
    print(-1)