import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs (start,end,cnt):
    togo = []
    for x in route[start]:
        if x == dest:
            return cnt
        if len(h[x])==1 and not vis.get(x):
            vis[x] = 1
        else:
            if not vis.get(x):
                vis[x] = 1
                togo.append(x)
    for x in togo:
        return dfs(x,dest,cnt+1)

N = int(input())
vis={}
vis[0] = 1
h = {}
route = {}

for x in range(1,N+1):
    l = list(map(int,input().split()))
    for y in l[1:]:
        if h.get(y):
            h[y].extend([x])
        else:
            h[y] = list()
            h[y].extend([x])
        if route.get(y):
            route[y].extend(l[1:])
        else:
            route[y] = l[1:]

dest = int(input())
c = dfs(0,dest,0)
if c == None:
    print(-1)
else:
    print(c)