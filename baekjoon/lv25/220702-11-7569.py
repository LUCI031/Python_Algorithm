import sys
from collections import deque
input = sys.stdin.readline

M,N,H = map(int,input().split())
lst = []
res = 0
v = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

for _ in range(H):
    a = []
    lst.append(a)
    for _ in range(N):
        a.append(list(map(int,input().split())))


que = deque()


dx = [-1, 1, 0, 0, 0, 0] 
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


for i in range(H):
    for j in range(N):
        for k in range(M):
            if lst[i][j][k] == 1 and not v[i][j][k]:
                v[i][j][k] = True
                que.append((i,j,k))
            
while que:
    x,y,z = que.popleft()
    for g in range(6):
        nx = x + dx[g]
        ny = y + dy[g]
        nz = z + dz[g]
        
        if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M:
            continue
        
        if lst[nx][ny][nz] == 0 and not v[nx][ny][nz]:
            v[nx][ny][nz] = True
            lst[nx][ny][nz] = lst[x][y][z] + 1
            que.append((nx,ny,nz))

for i in lst:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        res = max(res,max(j))
print(res-1)