import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())

lst = []
for _ in range(N):
    lst.append(list(map(int,input().split())))
cnt = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a,b):
    q = deque()
    tmp = []
    q.append((a,b))
    tmp.append((a,b))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == 0:
                if L <= abs(lst[nx][ny]-lst[x][y]) <= R:
                    v[nx][ny] = 1
                    q.append((nx,ny))
                    tmp.append((nx,ny))
    return tmp

while 1:
    v = [[0] * (N+1) for _ in range(N+1)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                v[i][j] = 1
                country = bfs(i,j)
    
                if len(country) > 1:
                    flag = 1
                    number = sum([lst[x][y] for x,y in country])//len(country)
                    for x,y in country:
                        lst[x][y] = number

    if flag == 0:
        break
    cnt += 1

print(cnt)