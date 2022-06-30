import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int,input().split())
lst = []
res = 0
v = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    lst.append(list(map(int,input().split())))

que = deque()


dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]


for i in range(N):
    for j in range(M):
        if lst[i][j] == 1 and not v[i][j]:
            v[i][j] = True
            que.append((i,j))
            
while que:
    x,y = que.popleft()
    for g in range(4):
        nx = x + dx[g]
        ny = y + dy[g]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        
        if lst[nx][ny] == 0 and not v[nx][ny]:
            v[nx][ny] = True
            lst[nx][ny] = lst[x][y] + 1
            que.append((nx,ny))

for i in lst:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res,max(i))
print(res-1)