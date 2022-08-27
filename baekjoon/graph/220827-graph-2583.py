import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M,N,K = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = []

def dfs(x,y):
    global cnt
    v[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and v[nx][ny]==0 and square[nx][ny] == 1:
            cnt += 1
            dfs(nx,ny)
    return
    

square = [[1 for _ in range(N)] for _ in range(M)]
v = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x_s, y_s, x_e, y_e = map(int,input().split())
    for i in range(y_s,y_e):
        for j in range(x_s,x_e):
            square[i][j] = 0

for i in range(M):
    for j in range(N):
        if v[i][j] == 0 and square[i][j]==1:
            cnt = 1
            dfs(i,j)
            ans.append(cnt)
        else:
            v[i][j] = 1

ans.sort()
print(len(ans))
print(*ans)