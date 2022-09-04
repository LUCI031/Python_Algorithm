import sys
input = sys.stdin.readline

N = int(input())
lst = []
res = 0
for _ in range(N):
    lst.append(list(input().strip()))


def wid(x):
    word = lst[x][0]
    cnt = 1
    ans = [0]
    for i in range(1,N):
        if lst[x][i] == word:
            cnt += 1
        else:
            ans.append(cnt)
            word = lst[x][i]
            cnt = 1
    ans.append(cnt)
    return max(ans)

def dep(y):
    word = lst[0][y]
    cnt = 1
    ans = [0]
    for i in range(1,N):
        if lst[i][y] == word:
            cnt += 1
        else:
            ans.append(cnt)
            word = lst[i][y]
            cnt = 1
    ans.append(cnt)
    return max(ans)

def switch(x,y):
    res = [0]
    tmp = lst[x][y]
    if y+1 < N:
        lst[x][y] = lst[x][y+1]
        lst[x][y+1] = tmp
        res.append(max(wid(x),dep(y),dep(y+1)))
        lst[x][y+1] = lst[x][y]
        lst[x][y] = tmp
    if x+1 < N:
        lst[x][y] = lst[x+1][y]
        lst[x+1][y] = tmp
        res.append(max(wid(x),wid(x+1),dep(y)))
        lst[x+1][y] = lst[x][y]
        lst[x][y] = tmp
    return max(res)
    
for i in range(N):
    for j in range(N):
        res = max(res,wid(i),dep(j),switch(i,j))

print(res)