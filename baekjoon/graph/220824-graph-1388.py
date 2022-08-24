import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lst = []
visit = [[0 for _ in range(M)] for _ in range(N)]
cnt = 0
for _ in range(N):
    lst.append(input().strip())

def dfs(y,x,cnt):
    visit[y][x] = 1
    if x+1 < M and lst[y][x] == '-' and lst[y][x+1] == '-':
        return dfs(y,x+1,cnt)
    elif y+1 < N and lst[y][x] == '|' and lst[y+1][x] == '|':
        return dfs(y+1,x,cnt)
    else:
        return cnt+1

for i in range(N):
    for j in range(M):
        if visit[i][j] == 0:
            cnt = dfs(i,j,cnt)

print(cnt)