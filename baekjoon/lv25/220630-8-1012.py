import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

answer = []

def dfs(y,x):
    lst[y][x] = '0'
    if x+1 < M:
        if lst[y][x+1] == '1': # east
            dfs(y,x+1)
    if y+1 < N:
        if lst[y+1][x] == '1': # south
            dfs(y+1,x)
    if x-1 > -1:
        if lst[y][x-1] == '1': # west
            dfs(y,x-1)
    if y-1 > -1:
        if lst[y-1][x] == '1': # north
            dfs(y-1,x)
    else:
        return        

N = int(input())

for _ in range(N):
    cnt = 0
    M,N,K = map(int,input().split())
    lst = [['0' for _ in range(M)] for _ in range(N)]
    
    for _ in range(K):
        x,y = map(int,input().split())
        lst[y][x] = '1'

    for i in range(N):
        for j in range(M):
            if lst[i][j] == '1':
                cnt += 1
                dfs(i,j)
    answer.append(cnt)
                
for i in answer:
    print(i)
