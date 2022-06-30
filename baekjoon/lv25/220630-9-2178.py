import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
lst = []

for i in range(N):
    lst.append(list(map(int,input().strip())))

que = deque()
que.append((0,0))

cnt = 1
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

   
while que:
    x,y = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        
        if lst[nx][ny] == 0:
            continue
        
        if lst[nx][ny] == 1:
            lst[nx][ny] = lst[x][y] + 1
            que.append((nx,ny))
        
print(lst[-1][-1])            