import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

dx = [2,1,-1,-2,2,1,-1,-2] 
dy = [1,2,2,1,-1,-2,-2,-1]

def bfs(L,v,start,goal):
    que = deque()
    que.append(start)
    v[start[0]][start[1]] = 1

    while que:
        x,y = que.popleft()
        if (x,y) == goal:
            print(v[x][y]-1)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < L and 0 <= ny < L and v[nx][ny] == 0:
                que.append((nx,ny))
                v[nx][ny] = v[x][y] + 1
                

for _ in range(N):
    L = int(input())
    v = [[0 for _ in range(L)] for _ in range(L)]
    start = tuple(map(int,input().split()))
    goal = tuple(map(int,input().split()))
    bfs(L,v,start,goal)