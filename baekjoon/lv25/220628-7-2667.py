import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

answer = []
t_cnt = 0
cnt = 0


def dfs(x,y):
    global cnt
    if lst[x][y] == '1':
        cnt += 1
    lst[x][y] = '0'
    
    
    if y+1 < N:
        if lst[x][y+1] == '1': # east
            dfs(x,y+1)
    if x+1 < N:
        if lst[x+1][y] == '1': # south
            dfs(x+1,y)
    if y-1 > -1:
        if lst[x][y-1] == '1': # west
            dfs(x,y-1)
    if x-1 > -1:
        if lst[x-1][y] == '1': # north
            dfs(x-1,y)
    else:
        return        

lst = []
N = int(input())

for i in range(N):
    lst.append(list(input().strip()))

for i in range(N):
    for j in range(N):
        if lst[i][j] == '1':
            t_cnt += 1
            dfs(i,j)
            answer.append(cnt)
            cnt = 0
            
print(t_cnt)
answer.sort()
for i in answer:
    print(i)
