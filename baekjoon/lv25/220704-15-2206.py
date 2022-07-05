import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
lst = []

for i in range(N):
    lst.append(list(map(int,input().strip())))

v = [[[0]*2 for _ in range(M)] for _ in range(N)]
v[0][0][0] = 1

dx = [0,0,-1,1] 
dy = [1,-1,0,0]

def bfs(x,y,z):
    que = deque()
    que.append((x,y,z))
    
    while que:
        a,b,c = que.popleft()
        if a == N -1 and b == M -1:
            return v[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if lst[nx][ny] == 1 and c == 0:
                v[nx][ny][1] = v[a][b][0] + 1
                que.append((nx,ny,1))
            elif lst[nx][ny] == 0 and v[nx][ny][c] == 0:
                v[nx][ny][c] = v[a][b][c] + 1
                que.append((nx,ny,c))
    return -1

print(bfs(0,0,0))