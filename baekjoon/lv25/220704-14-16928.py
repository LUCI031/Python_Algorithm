import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

v = [-1 for _ in range(101)]

for _ in range(N+M): # 사다리,뱀
    x,y = map(int,input().split())
    v[x]=(x,y)
que = deque()
que.append(1)
v[1] = 0

dice = [i for i in range(1,7)]

while que:
    if v[-1] > 0:
        break
    start = que.popleft()
    for d in dice:
            cur = start+d
            if cur < 101:
                if type(v[cur]) == tuple:
                    tmp = v[cur][0]
                    cur = v[cur][1]
                    v[tmp] = 0
                if v[cur] == -1:
                    v[cur] = v[start] + 1
                    que.append(cur)
        
print(v[-1])