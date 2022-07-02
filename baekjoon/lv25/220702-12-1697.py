import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())

maxi = 10 ** 5
v = [0 for _ in range(maxi+1)]

que = deque()
que.append(N)

while que:
    x = que.popleft()
    if x == K:
        print(v[K])
        break
    for nx in (x-1,x+1,x*2):
        if 0 <= nx <= maxi and not v[nx]:
            v[nx] = v[x] + 1
            que.append(nx)